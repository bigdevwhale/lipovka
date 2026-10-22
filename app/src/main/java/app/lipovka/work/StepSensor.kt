package app.lipovka.work

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.os.Build
import androidx.core.content.ContextCompat
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.withTimeoutOrNull

/**
 * The phone's own step counter: a hardware sensor that counts every step since the last reboot,
 * even while the app is closed. The app only needs to read it now and then.
 */
class StepSensor(private val context: Context) {
    private val manager = context.getSystemService(Context.SENSOR_SERVICE) as SensorManager
    private val sensor: Sensor? = manager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER)

    val present: Boolean get() = sensor != null

    val allowed: Boolean
        get() = Build.VERSION.SDK_INT < Build.VERSION_CODES.Q ||
            ContextCompat.checkSelfPermission(context, Manifest.permission.ACTIVITY_RECOGNITION) == PackageManager.PERMISSION_GRANTED

    /** The counter as it changes; the first value comes right after subscribing. */
    fun counts(): Flow<Long> = callbackFlow {
        val s = sensor
        if (s == null || !allowed) {
            close()
            return@callbackFlow
        }
        val l = object : SensorEventListener {
            override fun onSensorChanged(e: SensorEvent) {
                trySend(e.values[0].toLong())
            }

            override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) = Unit
        }
        manager.registerListener(l, s, SensorManager.SENSOR_DELAY_NORMAL)
        awaitClose { manager.unregisterListener(l) }
    }

    /** One reading, or null if the sensor is missing, not allowed or silent. */
    suspend fun read(timeoutMs: Long = 10_000): Long? {
        if (sensor == null || !allowed) return null
        return withTimeoutOrNull(timeoutMs) { counts().first() }
    }
}
