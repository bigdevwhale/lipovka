package app.lipovka.work

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Rect
import android.widget.RemoteViews
import androidx.core.content.res.ResourcesCompat
import app.lipovka.MainActivity
import app.lipovka.R
import app.lipovka.container
import app.lipovka.localized
import app.lipovka.ru
import app.lipovka.ui.Words
import app.lipovka.ui.art.Icons
import app.lipovka.ui.art.toBitmap
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import java.time.LocalDate

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
            val big = if (who != null) r.getString(R.string.steps_n, Words.num(left)) else ""
            val small = "${Words.num(today)} ${r.getString(R.string.steps_today)}"
            val bmp = render(context, title, big, small, s.bag.size)
            val open = PendingIntent.getActivity(context, 0, Intent(context, MainActivity::class.java), PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
            for (id in ids) {
                val views = RemoteViews(context.packageName, R.layout.widget_post)
                views.setImageViewBitmap(R.id.widget_image, bmp)
                views.setOnClickPendingIntent(R.id.widget_image, open)
                manager.updateAppWidget(id, views)
            }
        }

        private fun render(context: Context, title: String, big: String, small: String, bag: Int): Bitmap {
            val w = 720
            val h = 240
            val out = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888)
            val cv = Canvas(out)
            val paper = Paint().apply { color = 0xFFF2E2BB.toInt() }
            val ink = Paint().apply { color = 0xFF22160F.toInt() }
            val p = 6f
            cv.drawRect(p, 0f, w - p, h.toFloat(), ink); cv.drawRect(0f, p, w.toFloat(), h - p, ink)
            cv.drawRect(2 * p, p, w - 2 * p, h - p, paper); cv.drawRect(p, 2 * p, w - p, h - 2 * p, paper)
            val icon = Icons.bag().toBitmap()
            cv.drawBitmap(Bitmap.createScaledBitmap(icon, icon.width * 8, icon.height * 8, false), null, Rect(28, 48, 28 + 160, 48 + 144), null)
            val font = ResourcesCompat.getFont(context, R.font.m6x11)
            fun text(s: String, x: Float, y: Float, size: Float, color: Int) {
                val t = Paint().apply { typeface = font; textSize = size; this.color = color; isAntiAlias = false }
                cv.drawText(s, x, y, t)
            }
            text(title.take(22), 210f, 78f, 44f, 0xFF26375E.toInt())
            if (big.isNotEmpty()) text(big, 210f, 144f, 64f, 0xFF22160F.toInt())
            text(small, 210f, 200f, 36f, 0xFF7A5A3E.toInt())
            if (bag > 0) text(bag.toString(), 92f, 170f, 48f, 0xFFFBF3DC.toInt())
            return out
        }
    }
}
