package app.lipovka.work

import android.Manifest
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.core.content.ContextCompat
import androidx.work.CoroutineWorker
import androidx.work.ExistingPeriodicWorkPolicy
import androidx.work.PeriodicWorkRequestBuilder
import androidx.work.WorkManager
import androidx.work.WorkerParameters
import app.lipovka.MainActivity
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Kind
import app.lipovka.data.St
import app.lipovka.localized
import app.lipovka.ru
import java.time.LocalDateTime
import java.util.concurrent.TimeUnit

/** Every quarter of an hour: read the step counter, sort the morning post, refresh the weather and the widget. */
class PostWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        val c = applicationContext.container
        runCatching { c.refreshWeather() }
        c.sync()
        Notes.check(applicationContext)
        PostWidget.updateAll(applicationContext)
        return Result.success()
    }
}

object Alarms {
    fun schedule(context: Context) {
        val req = PeriodicWorkRequestBuilder<PostWorker>(15, TimeUnit.MINUTES).build()
        WorkManager.getInstance(context).enqueueUniquePeriodicWork("post", ExistingPeriodicWorkPolicy.KEEP, req)
    }
}

/** The two gentle notifications: the morning post, and an evening "almost there". */
object Notes {
    private const val CHANNEL = "post"

    private fun channel(context: Context) {
        val m = context.getSystemService(NotificationManager::class.java)
        if (m.getNotificationChannel(CHANNEL) == null) {
            m.createNotificationChannel(NotificationChannel(CHANNEL, context.localized().getString(R.string.channel_post), NotificationManager.IMPORTANCE_DEFAULT))
        }
    }

    fun allowed(context: Context) = Build.VERSION.SDK_INT < 33 ||
        ContextCompat.checkSelfPermission(context, Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED

    suspend fun check(context: Context) {
        val c = context.container
        val set = c.settings.now()
        if (!set.notify || !allowed(context)) return
        val s = c.post.state.value ?: return
        val now = LocalDateTime.now()
        val day = c.game.mailDay(now).toEpochDay()
        val r = context.localized()
        val bag = s.bag
        val desk = s.mail.count { it.state == St.DESK }
        if (set.notifiedMorning < day && now.hour in 7..11 && s.morning == day && (bag.isNotEmpty() || desk > 0)) {
            val tele = bag.firstOrNull { it.kind == Kind.TELEGRAM.name }
            val text = when {
                tele != null -> r.getString(R.string.n_telegram, c.content.resident(tele.to)?.name?.invoke(r.ru) ?: "")
                desk > 0 -> r.getString(R.string.n_desk)
                else -> r.resources.getQuantityString(R.plurals.n_bag, bag.size, bag.size)
            }
            show(context, 1, r.getString(R.string.n_morning_title), text)
            c.settings.update { it.copy(notifiedMorning = day) }
        }
        if (set.notifiedEvening < day && now.hour in 17..20 && bag.isNotEmpty()) {
            val next = c.game.plan(s).firstOrNull() ?: return
            val left = (next.leg - s.leg).coerceAtLeast(0)
            if (left in 1..1500) {
                val who = next.mail.firstNotNullOfOrNull { c.content.resident(it.to) }?.name?.invoke(r.ru) ?: ""
                show(context, 2, r.getString(R.string.n_evening_title), r.getString(R.string.n_evening, who, left))
                c.settings.update { it.copy(notifiedEvening = day) }
            }
        }
    }

    private fun show(context: Context, id: Int, title: String, text: String) {
        channel(context)
        val open = PendingIntent.getActivity(
            context, 0, Intent(context, MainActivity::class.java).addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
        )
        val n = NotificationCompat.Builder(context, CHANNEL)
            .setSmallIcon(R.drawable.ic_note)
            .setContentTitle(title)
            .setContentText(text)
            .setStyle(NotificationCompat.BigTextStyle().bigText(text))
            .setContentIntent(open)
            .setAutoCancel(true)
            .build()
        @Suppress("MissingPermission")
        NotificationManagerCompat.from(context).notify(id, n)
    }
}

