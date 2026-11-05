package app.lipovka.work

import android.content.Context
import android.content.Intent
import android.util.Log
import app.lipovka.BuildConfig
import com.huawei.hmf.tasks.Task
import com.huawei.hms.api.ConnectionResult
import com.huawei.hms.api.HuaweiApiAvailability
import com.huawei.hms.hihealth.HuaweiHiHealth
import com.huawei.hms.hihealth.data.DataType
import com.huawei.hms.hihealth.data.Field
import com.huawei.hms.hihealth.data.SampleSet
import com.huawei.hms.hihealth.data.Scopes
import kotlinx.coroutines.suspendCancellableCoroutine
import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import java.util.concurrent.TimeUnit
import kotlin.coroutines.resume
import kotlin.coroutines.resumeWithException

/**
 * Steps from Huawei Health, which keeps them to itself rather than sharing with Health Connect.
 * Read through Huawei Health Kit (part of HMS Core) as totals per day, just like Health Connect's,
 * so steps a Huawei watch or band hands over late still arrive.
 */
class HuaweiSteps(private val context: Context) {
    /** The build knows its AppGallery Connect id; without it Health Kit won't talk to the app at all. */
    val configured: Boolean get() = BuildConfig.HUAWEI_APP_ID.isNotBlank()

    /** HMS Core is on the phone and ready. */
    val services: Boolean
        get() = runCatching { HuaweiApiAvailability.getInstance().isHuaweiMobileServicesAvailable(context) == ConnectionResult.SUCCESS }
            .getOrDefault(false)

    /** The Huawei Health app is installed: it's what holds the steps. */
    val app: Boolean
        get() = runCatching { context.packageManager.getPackageInfo(APP, 0); true }.getOrDefault(false)

    /** Worth offering here: built for it, and the phone has Huawei's services or its health app. */
    val offered: Boolean get() = configured && (services || app)

    /** Ready to ask for the steps. */
    val available: Boolean get() = configured && services && app

    /** Huawei's own screens: sign in with a HUAWEI ID and allow reading steps. */
    fun requestIntent(): Intent? = runCatching {
        HuaweiHiHealth.getSettingController(context).requestAuthorizationIntent(arrayOf(Scopes.HEALTHKIT_STEP_READ), true)
    }.onFailure { Log.w(TAG, "intent", it) }.getOrNull()

    /** Did the screens from [requestIntent] end with reading allowed? */
    fun granted(result: Intent?): Boolean = runCatching {
        HuaweiHiHealth.getSettingController(context).parseHealthKitAuthResultFromIntent(result)?.isSuccess == true
    }.onFailure { Log.w(TAG, "result", it) }.getOrDefault(false)

    /** Reading is allowed: a quiet try at today's steps tells, since Health Kit has no plain question for it. */
    suspend fun allowed(): Boolean {
        if (!available) return false
        return runCatching { HuaweiHiHealth.getDataController(context).readTodaySummation(DataType.DT_CONTINUOUS_STEPS_DELTA).await() }
            .onFailure { Log.w(TAG, "allowed", it) }.isSuccess
    }

    /** Steps per day from [from] to [to], keyed by epoch day; null if Huawei Health can't be read now. */
    suspend fun days(from: LocalDate, to: LocalDate): Map<Long, Long>? {
        if (!available) return null
        return runCatching {
            val data = HuaweiHiHealth.getDataController(context)
            val out = HashMap<Long, Long>()
            data.readDailySummation(DataType.DT_CONTINUOUS_STEPS_DELTA, from.ymd(), to.ymd()).await().into(out)
            // The day's sum may lag behind what the band has just handed over; today's own sum is the freshest.
            if (to == LocalDate.now()) runCatching { data.readTodaySummation(DataType.DT_CONTINUOUS_STEPS_DELTA).await().into(out) }
                .onFailure { Log.w(TAG, "today", it) }
            for (d in from.toEpochDay()..to.toEpochDay()) out.putIfAbsent(d, 0L)
            out as Map<Long, Long>
        }.onFailure { Log.w(TAG, "read", it) }.getOrNull()
    }

    /** Adds each point's steps to its day, keeping the larger where two reads cover the same day. */
    private fun SampleSet.into(out: MutableMap<Long, Long>) {
        val zone = ZoneId.systemDefault()
        val sums = HashMap<Long, Long>()
        for (p in samplePoints) {
            val day = Instant.ofEpochMilli(p.getStartTime(TimeUnit.MILLISECONDS)).atZone(zone).toLocalDate().toEpochDay()
            val n = runCatching { p.getFieldValue(Field.FIELD_STEPS_DELTA).asIntValue().toLong() }.getOrDefault(0L)
            sums[day] = (sums[day] ?: 0L) + n
        }
        for ((day, n) in sums) out[day] = maxOf(out[day] ?: 0L, n)
    }

    private fun LocalDate.ymd(): Int = format(DateTimeFormatter.BASIC_ISO_DATE).toInt()

    companion object {
        private const val TAG = "HuaweiSteps"
        const val APP = "com.huawei.health"
    }
}

/** Waits for a Huawei task the way coroutines wait for anything else. */
private suspend fun <T> Task<T>.await(): T = suspendCancellableCoroutine { cont ->
    addOnSuccessListener { cont.resume(it) }
    addOnFailureListener { cont.resumeWithException(it) }
}
