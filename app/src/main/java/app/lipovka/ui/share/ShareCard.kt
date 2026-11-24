package app.lipovka.ui.share

import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Rect
import android.graphics.Typeface
import android.text.Layout
import android.text.StaticLayout
import android.text.TextPaint
import android.text.TextUtils
import androidx.core.content.FileProvider
import androidx.core.content.res.ResourcesCompat
import app.lipovka.R
import app.lipovka.ui.art.Scene
import app.lipovka.ui.art.toBitmap
import java.io.File

/**
 * A picture to post: a scene from the village, a title, a few numbers or a few lines of a letter, and at the
 * bottom the game's name with a small QR code of its Google Play page.
 */
class Card(
    val title: String,
    val sub: String,
    /** Big number and what it counts, two to a row. */
    val stats: List<Pair<String, String>> = emptyList(),
    /** Words in place of numbers: a letter's lines. */
    val quote: String? = null,
    val scene: Scene? = null,
    /** The rows of the scene shown, in art pixels: the interesting band of it. */
    val rows: IntRange = 0..0,
    /** A drawn illustration (assets/cards, by tools/card_art.py) in place of a scene. */
    val art: String? = null,
    /** One thing held up large on paper in place of a scene: a stamp, a gift. */
    val picture: app.lipovka.ui.art.Buf? = null,
)

object ShareCard {
    const val W = 1080
    const val H = 1350
    const val PLAY = "https://play.google.com/store/apps/details?id=app.lipovka"

    private const val PAPER = 0xFFF2E2BB.toInt()
    private const val PAPER2 = 0xFFE1CB9B.toInt()
    private const val LIGHT = 0xFFFBF3DC.toInt()
    private const val INK = 0xFF22160F.toInt()
    private const val MUTED = 0xFF7A5A3E.toInt()
    private const val RED = 0xFFA33A2C.toInt()
    private const val BLUE = 0xFF26375E.toInt()

    private const val M = 60
    private const val SCENE_H = 620

    /** The QR code of the Play page, as rows of on/off modules (made by tools/qr.py). */
    private val qr: List<String> by lazy {
        ShareCard::class.java.getResourceAsStream("/qr_play.txt")?.bufferedReader()?.readLines()?.filter { it.isNotBlank() } ?: emptyList()
    }

    fun render(ctx: Context, card: Card): Bitmap {
        val font = ResourcesCompat.getFont(ctx, R.font.m6x11) ?: Typeface.DEFAULT_BOLD
        val bmp = Bitmap.createBitmap(W, H, Bitmap.Config.ARGB_8888)
        val cv = Canvas(bmp)
        cv.drawColor(PAPER)
        val fill = Paint()
        fun box(l: Int, t: Int, r: Int, b: Int, c: Int) { fill.color = c; cv.drawRect(l.toFloat(), t.toFloat(), r.toFloat(), b.toFloat(), fill) }
        fun text(size: Float, color: Int) = TextPaint().apply { typeface = font; textSize = size; this.color = color; isAntiAlias = false }

        // a dark frame, the way the game's panels are drawn
        box(24, 24, W - 24, H - 24, INK); box(32, 32, W - 32, H - 32, PAPER)

        // the illustration, or the scene in hard pixels, framed
        val scene = card.scene
        val drawn = card.art?.let { a -> runCatching { ctx.assets.open("cards/$a.webp").use { android.graphics.BitmapFactory.decodeStream(it) } }.getOrNull() }
        val pic = card.picture
        if (pic != null) {
            // the thing alone on a paper panel, as large as whole pixels allow
            val dx = M
            box(dx - 8, M - 8, W - M + 8, M + SCENE_H + 8, INK); box(dx, M, W - M, M + SCENE_H, PAPER2)
            val img = pic.toBitmap()
            val k = minOf((W - 2 * M - 120) / img.width, (SCENE_H - 120) / img.height).coerceAtLeast(1)
            val pw = img.width * k
            val ph = img.height * k
            cv.drawBitmap(img, Rect(0, 0, img.width, img.height), Rect((W - pw) / 2, M + (SCENE_H - ph) / 2, (W + pw) / 2, M + (SCENE_H + ph) / 2), Paint().apply { isFilterBitmap = false })
        }
        val frame = if (pic != null) null else drawn ?: scene?.frame(9)?.toBitmap() ?: Bitmap.createBitmap(1, 1, Bitmap.Config.ARGB_8888)
        val dh = SCENE_H
        if (frame != null) {
            val src = if (drawn != null || scene == null) Rect(0, 0, frame.width, frame.height)
                else (frame.width / scene.w).let { k -> Rect(0, card.rows.first * k, frame.width, (card.rows.last + 1) * k) }
            // a fixed height, so the words below always have their room; centred, with paper either side if narrower
            val dw = minOf(W - 2 * M, dh * src.width() / src.height())
            val dx = (W - dw) / 2
            box(dx - 8, M - 8, dx + dw + 8, M + dh + 8, INK)
            cv.drawBitmap(frame, src, Rect(dx, M, dx + dw, M + dh), Paint().apply { isFilterBitmap = drawn != null })
        }

        // a line that must stay on the card: smaller type when long, and cut with an ellipsis past the smallest
        fun line(s: String, size: Float, min: Float, color: Int, x: Float, y: Float) {
            val room = (W - M - x)
            val p = text(size, color)
            while (p.textSize > min && p.measureText(s) > room) p.textSize -= 2f
            cv.drawText(TextUtils.ellipsize(s, p, room, TextUtils.TruncateAt.END).toString(), x, y, p)
        }

        var y = M + dh + 84f
        line(card.title, 80f, 52f, INK, M.toFloat(), y)
        y += 48f
        line(card.sub, 40f, 32f, MUTED, M.toFloat(), y)
        y += 28f

        val footTop = H - 32 - 200
        if (card.quote != null) {
            val p = text(44f, INK)
            val inner = W - 2 * M - 56
            val lines = ((footTop - 24 - y.toInt() - 48) / (p.fontSpacing)).toInt().coerceAtLeast(1)
            val layout = StaticLayout.Builder.obtain(card.quote, 0, card.quote.length, p, inner)
                .setAlignment(Layout.Alignment.ALIGN_NORMAL).setMaxLines(lines).setEllipsize(TextUtils.TruncateAt.END).build()
            // the paper only as tall as the words on it
            box(M, y.toInt(), W - M, minOf(footTop - 24, y.toInt() + layout.height + 48), LIGHT)
            cv.save(); cv.translate(M + 28f, y + 24f); layout.draw(cv); cv.restore()
        } else {
            // two numbers to a row, each in its own little panel
            val gap = 16
            val cw = (W - 2 * M - gap) / 2
            val ch = 112
            card.stats.take(4).forEachIndexed { i, (big, label) ->
                val x = M + (i % 2) * (cw + gap)
                val top = y.toInt() + (i / 2) * (ch + gap)
                box(x, top, x + cw, top + ch, INK); box(x + 6, top + 6, x + cw - 6, top + ch - 12, PAPER2)
                cv.drawText(big, x + 24f, top + 62f, text(64f, INK))
                cv.drawText(label, x + 24f, top + 94f, text(36f, MUTED))
            }
        }

        // the foot: the game's name and where to get it, and the code that goes there
        val n = qr.size
        if (n > 0) {
            val mod = 5
            val side = (n + 4) * mod
            val qx = W - M - side
            val qy = H - 32 - 24 - side
            box(qx - 6, qy - 6, qx + side + 6, qy + side + 6, INK)
            box(qx, qy, qx + side, qy + side, LIGHT)
            qr.forEachIndexed { r, row -> row.forEachIndexed { c, ch -> if (ch == '1') box(qx + (c + 2) * mod, qy + (r + 2) * mod, qx + (c + 3) * mod, qy + (r + 3) * mod, INK) } }
        }
        cv.drawText(ctx.getString(R.string.app_name), M.toFloat(), H - 32 - 110f, text(64f, RED))
        cv.drawText(ctx.getString(R.string.share_tagline), M.toFloat(), H - 32 - 66f, text(40f, MUTED))
        cv.drawText("Google Play", M.toFloat(), H - 32 - 26f, text(40f, BLUE))
        return bmp
    }

    /** Hands the card to whatever the person shares with, with a line and the Play link to go with it. */
    fun share(ctx: Context, card: Card) = send(ctx, render(ctx, card))

    /** Hands a card already drawn (as shown in the preview) to the share sheet. */
    fun send(ctx: Context, bmp: Bitmap) {
        val dir = File(ctx.cacheDir, "share").apply { mkdirs() }
        val f = File(dir, "lipovka.png")
        f.outputStream().use { bmp.compress(Bitmap.CompressFormat.PNG, 100, it) }
        val uri = FileProvider.getUriForFile(ctx, ctx.packageName + ".share", f)
        val send = Intent(Intent.ACTION_SEND).setType("image/png")
            .putExtra(Intent.EXTRA_STREAM, uri)
            .putExtra(Intent.EXTRA_TEXT, ctx.getString(R.string.share_text, PLAY))
            .addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        ctx.startActivity(Intent.createChooser(send, ctx.getString(R.string.share)).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
    }
}
