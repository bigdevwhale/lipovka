package app.lipovka.work

import android.app.AlarmManager
import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Paint
import android.widget.RemoteViews
import androidx.core.content.res.ResourcesCompat
import app.lipovka.MainActivity
import app.lipovka.R
import app.lipovka.container
import app.lipovka.localized
import app.lipovka.ru
import app.lipovka.ui.Words
import app.lipovka.domain.GameState
import app.lipovka.domain.Phase
import app.lipovka.ui.art.EveningScene
import app.lipovka.ui.art.Icons
import app.lipovka.ui.art.PostOffice
import app.lipovka.ui.art.toBitmap
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.ZoneId

/**
 * The bag on the home screen: who the next letter is for and how many steps are left. Drawn as one
 * bitmap so the pixel font and the art look the same as in the app.
 */
class PostWidget : AppWidgetProvider() {
    override fun onUpdate(context: Context, manager: AppWidgetManager, ids: IntArray) {
        val pending = goAsync()
        CoroutineScope(Dispatchers.Default).launch {
            try { updateAll(context) } finally { pending.finish() }
        }
    }

    companion object {
        suspend fun updateAll(context: Context) {
            val manager = AppWidgetManager.getInstance(context)
            val ids = manager.getAppWidgetIds(ComponentName(context, PostWidget::class.java))
            if (ids.isEmpty()) return
            val c = context.container
            if (c.post.state.value == null) c.post.refresh()
            val s = c.post.state.value ?: return
            val r = context.localized()
            val plan = c.game.plan(s)
            val next = plan.firstOrNull()
            val who = next?.mail?.firstNotNullOfOrNull { c.content.resident(it.to) }?.name?.invoke(r.ru)
            val left = next?.let { (it.leg - s.leg).coerceAtLeast(0) } ?: 0
            val today = s.days[LocalDate.now().toEpochDay()] ?: 0
            val title = if (who != null) who else r.getString(R.string.bag_empty)
            val big = if (who != null) r.resources.getQuantityString(R.plurals.steps_n, Words.q(left), Words.num(left)) else ""
            val small = "${Words.num(today)} ${r.resources.getQuantityString(R.plurals.steps_today, Words.q(today))}"
            val walked = next?.let { if (it.leg > 0) s.leg.toFloat() / it.leg else 0f }
            val pic = picture(context, s)
            val bmp = render(context, title, big, small, s.bag.size, walked, pic)
            val open = PendingIntent.getActivity(context, 0, Intent(context, MainActivity::class.java), PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
            for (id in ids) {
                val views = RemoteViews(context.packageName, R.layout.widget_post)
                views.setImageViewBitmap(R.id.widget_image, bmp)
                views.setOnClickPendingIntent(R.id.widget_image, open)
                manager.updateAppWidget(id, views)
            }
            atMidnight(context, ids)
        }

        /** The step count is today's, so the widget redraws itself just after midnight even if nothing else wakes it. */
        private fun atMidnight(context: Context, ids: IntArray) {
            val intent = Intent(context, PostWidget::class.java)
                .setAction(AppWidgetManager.ACTION_APPWIDGET_UPDATE)
                .putExtra(AppWidgetManager.EXTRA_APPWIDGET_IDS, ids)
            val pending = PendingIntent.getBroadcast(context, 1, intent, PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
            val at = LocalDate.now().plusDays(1).atStartOfDay(ZoneId.systemDefault()).toInstant().toEpochMilli() + 60_000
            context.getSystemService(AlarmManager::class.java).setAndAllowWhileIdle(AlarmManager.RTC, at, pending)
        }

        /**
         * The picture on the right, as the hour goes: by day the post office, the cat asleep on the letters
         * still to go out; from dusk the evening table with the kerosene lamp, out if it was put out tonight.
         */
        private suspend fun picture(context: Context, s: GameState): Bitmap {
            val c = context.container
            val now = LocalDateTime.now()
            val set = c.settings.now()
            val env = c.env(now, set, s)
            val evening = env.phase == Phase.DUSK || env.phase == Phase.EVENING || env.phase == Phase.NIGHT
            val scene = if (evening) EveningScene(env, lit = set.lampOut != now.toLocalDate().toEpochDay())
                else PostOffice(env, s.bag.size, s.has("dog"))
            val key = listOf(evening, scene.key)
            cached?.let { (k, bmp) -> if (k == key) return bmp }
            val full = scene.frame().toBitmap()
            // the post office is taller than the widget: its window, clock, kettle and cat, without the floor
            val crop = if (evening) full else Bitmap.createBitmap(full, 0, OFFICE_TOP, full.width, OFFICE_H)
            return Bitmap.createScaledBitmap(crop, crop.width * PIC_SCALE, crop.height * PIC_SCALE, false).also { cached = key to it }
        }

        /** The last picture drawn and what it showed: the scene is redrawn only when the weather, hour or house changes. */
        @Volatile private var cached: Pair<Any, Bitmap>? = null

        /** How much the picture is scaled up (whole pixels only, so it stays crisp). */
        private const val PIC_SCALE = 2
        /** The rows of the post office the widget shows: the evening table is 148 high, so this matches it. */
        private const val OFFICE_TOP = 10
        private const val OFFICE_H = 148

        private fun render(context: Context, title: String, big: String, small: String, bag: Int, walked: Float?, pic: Bitmap): Bitmap {
            val w = 1080
            val h = 360
            val out = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888)
            val cv = Canvas(out)
            val paper = Paint().apply { color = 0xFFF2E2BB.toInt() }
            val ink = Paint().apply { color = 0xFF22160F.toInt() }
            val p = 9f
            // the card: paper with a pixel-cut ink border
            cv.drawRect(p, 0f, w - p, h.toFloat(), ink); cv.drawRect(0f, p, w.toFloat(), h - p, ink)
            cv.drawRect(2 * p, p, w - 2 * p, h - p, paper); cv.drawRect(p, 2 * p, w - p, h - 2 * p, paper)
            // the picture on the right, in its own frame, with a thin lighter mat inside like a window
            val pw = pic.width
            val ph = pic.height
            val px = w - 2 * p.toInt() - 30 - pw
            val py = (h - ph) / 2
            cv.drawRect((px - 9).toFloat(), (py - 9).toFloat(), (px + pw + 9).toFloat(), (py + ph + 9).toFloat(), ink)
            cv.drawRect((px - 3).toFloat(), (py - 3).toFloat(), (px + pw + 3).toFloat(), (py + ph + 3).toFloat(), Paint().apply { color = 0xFFB8925E.toInt() })
            cv.drawBitmap(pic, px.toFloat(), py.toFloat(), null)
            // the bag with its count
            val icon = Icons.bag().toBitmap()
            val s = 9
            val bx = 36
            val by = 64
            cv.drawBitmap(Bitmap.createScaledBitmap(icon, icon.width * s, icon.height * s, false), bx.toFloat(), by.toFloat(), null)
            val font = ResourcesCompat.getFont(context, R.font.m6x11)
            fun text(t: String, x: Float, y: Float, size: Float, color: Int) {
                cv.drawText(t, x, y, Paint().apply { typeface = font; textSize = size; this.color = color; isAntiAlias = false })
            }
            if (bag > 0) text(bag.toString(), bx + 72f, by + 155f, 66f, 0xFFFBF3DC.toInt())
            // the words, fitted to the room left of the picture
            val tx = 250f
            val room = px - 24 - tx
            fun fit(t: String, size: Float): Float {
                val m = Paint().apply { typeface = font; textSize = size }.measureText(t)
                return if (m <= room) size else size * room / m
            }
            text(title, tx, 110f, fit(title, 60f), 0xFF26375E.toInt())
            if (big.isNotEmpty()) text(big, tx, 200f, fit(big, 90f), 0xFF22160F.toInt())
            text(small, tx, 262f, fit(small, 48f), 0xFF7A5A3E.toInt())
            // the way to the next gate: a dirt road, walked part trodden darker, a dot for the postman
            if (walked != null) {
                val y = 296f
                val len = room
                val road = Paint().apply { color = 0xFFD9C08E.toInt() }
                val trod = Paint().apply { color = 0xFFA9814E.toInt() }
                cv.drawRect(tx, y, tx + len, y + 15, road)
                val done = (len * walked.coerceIn(0f, 1f) / 15).toInt() * 15f
                cv.drawRect(tx, y, tx + done, y + 15, trod)
                var x = tx + done + 9
                while (x < tx + len - 15) { cv.drawRect(x, y + 6, x + 6, y + 9, trod); x += 21 }
                cv.drawRect(tx + done - 3, y - 6, tx + done + 9, y + 21, Paint().apply { color = 0xFF26375E.toInt() })
                cv.drawRect(tx + len - 12, y - 9, tx + len, y + 24, ink)
            }
            return out
        }
    }
}
