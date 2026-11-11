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
        val delivered = c.sync()
        Notes.delivered(applicationContext, delivered)
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

    /** Steps that show the person is up and about, not just turning over in bed. */
    private const val AWAKE_STEPS = 150

    /** An alarm clock set to ring within this long means the person is still asleep. */
    private const val ALARM_WINDOW_MS = 4 * 60 * 60 * 1000L

    private fun channel(context: Context) {
        val m = context.getSystemService(NotificationManager::class.java)
        if (m.getNotificationChannel(CHANNEL) == null) {
            m.createNotificationChannel(NotificationChannel(CHANNEL, context.localized().getString(R.string.channel_post), NotificationManager.IMPORTANCE_DEFAULT))
        }
    }

    fun allowed(context: Context) = Build.VERSION.SDK_INT < 33 ||
        ContextCompat.checkSelfPermission(context, Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED

    /** The things that happen once in the game and are worth a word: Bublik joining, a district opening. */
    private val MILESTONES = listOf("dog", "d1", "d2", "d3", "d4", "d5")

    suspend fun check(context: Context) {
        val c = context.container
        val set = c.settings.now()
        val s = c.post.state.value ?: return
        milestones(context, s, set)
        if (!set.notify || !allowed(context)) return
        val now = LocalDateTime.now()
        val day = c.game.mailDay(now).toEpochDay()
        val r = context.localized()
        val bag = s.bag
        val desk = s.mail.count { it.state == St.DESK }
        // The morning post waits for the person to be up: the first steps of the day, or ten o'clock if the
        // phone hasn't counted any (left on the table). Never before an alarm clock that hasn't rung yet.
        val alarm = runCatching { context.getSystemService(android.app.AlarmManager::class.java).nextAlarmClock?.triggerTime }.getOrNull()
        val sleeping = alarm != null && alarm - System.currentTimeMillis() in 0..ALARM_WINDOW_MS
        val up = !sleeping && ((s.days[now.toLocalDate().toEpochDay()] ?: 0) >= AWAKE_STEPS || now.hour >= 10)
        if (set.notifiedMorning < day && now.hour in 7..11 && up && s.morning == day && (bag.isNotEmpty() || desk > 0)) {
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

    /** Tells of each milestone reached since last looked; the first look only remembers what's there already. */
    private suspend fun milestones(context: Context, s: app.lipovka.domain.GameState, set: app.lipovka.data.Settings) {
        val reached = MILESTONES.filter { s.has(it) }.toSet()
        val seen = set.milestonesSeen
        if (seen != null && reached.all { it in seen }) return
        if (seen != null && set.notify && allowed(context)) {
            val r = context.localized()
            for (k in MILESTONES.filter { it in reached && it !in seen }) {
                if (k == "dog") show(context, 10, r.getString(R.string.n_dog_title), r.getString(R.string.n_dog))
                else {
                    val d = k.removePrefix("d").toInt()
                    val text = r.resources.getStringArray(R.array.n_district).getOrElse(d - 1) { "" }
                    show(context, 10 + d, r.getString(R.string.n_district_title, app.lipovka.ui.Words.district(d, r.ru)), text)
                }
            }
        }
        context.container.settings.update { it.copy(milestonesSeen = (it.milestonesSeen ?: emptySet()) + reached) }
    }

    /** "Handed over at the gate": for the letters just delivered, if the person asked for it. */
    suspend fun delivered(context: Context, mail: List<app.lipovka.data.Mail>) {
        val out = mail.filter { it.to != "me" }
        if (out.isEmpty()) return
        val c = context.container
        val set = c.settings.now()
        if (!set.notify || !set.notifyDelivered || !allowed(context)) return
        val r = context.localized()
        val s = c.post.state.value ?: return
        val year = ((c.game.mailDay(LocalDateTime.now()).toEpochDay() - s.start) / 365 + 1).toInt().coerceAtLeast(1)
        val lines = out.map { m ->
            val t = app.lipovka.ui.Words.mail(r, c.content, m, r.ru, year)
            t.brief.ifBlank { "${app.lipovka.ui.Words.kind(r, Kind.of(m.kind))} · ${t.title}" }
        }
        // what's still ahead, so the walk can go on without opening the app
        val next = c.game.plan(s).firstOrNull()
        val ahead = next?.let { n ->
            val who = n.mail.firstNotNullOfOrNull { c.content.resident(it.to) }?.name?.invoke(r.ru) ?: ""
            r.getString(R.string.n_delivered_next, who, (n.leg - s.leg).coerceAtLeast(0))
        } ?: r.getString(R.string.n_delivered_done)
        show(context, 3, r.resources.getQuantityString(R.plurals.n_delivered, out.size, out.size), (lines + ahead).joinToString("\n"))
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

