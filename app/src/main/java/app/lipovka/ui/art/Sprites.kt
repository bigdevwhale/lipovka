package app.lipovka.ui.art

import java.io.DataInputStream
import java.util.zip.InflaterInputStream

/**
 * A drawn picture cut from the art sheets (tools/art_gen.py, tools/sprites.py): residents, gifts, the houses
 * at the gate and the buildings on the map. It is [scale] times finer than art pixels, [w] × [h] fine pixels,
 * so it keeps its detail in a [Buf] of the same density. [px] is ARGB with 0 for empty; [glass] marks the
 * window panes, which light up at night.
 */
class Sprite(val w: Int, val h: Int, val scale: Int, val px: IntArray, val glass: BooleanArray) {
    /** Its size in art pixels. */
    val lw get() = (w + scale - 1) / scale
    val lh get() = (h + scale - 1) / scale
}

object Sprites {
    private val cache = HashMap<String, Sprite?>()

    /** The sprite at resources/sprites/[name].spr, or null when there's none and the art draws it itself. */
    fun get(name: String): Sprite? = synchronized(cache) {
        if (name in cache) cache[name] else load(name).also { cache[name] = it }
    }

    private fun load(name: String): Sprite? {
        val stream = Sprites::class.java.getResourceAsStream("/sprites/$name.spr") ?: return null
        return DataInputStream(stream.buffered()).use { s ->
            val magic = ByteArray(4).also { s.readFully(it) }
            if (String(magic, Charsets.US_ASCII) != "SPR2") return null
            val w = s.readUnsignedShort()
            val h = s.readUnsignedShort()
            val scale = s.readUnsignedByte()
            val pal = IntArray(s.readUnsignedByte()) { s.readInt() }
            val glassIdx = IntArray(s.readUnsignedByte()) { s.readUnsignedByte() }.toSet()
            val packed = ByteArray(s.readInt()).also { s.readFully(it) }
            val ix = InflaterInputStream(packed.inputStream()).use { it.readBytes() }
            val px = IntArray(w * h)
            val glass = BooleanArray(w * h)
            for (i in 0 until w * h) {
                val k = ix[i].toInt() and 0xFF
                if (k == 0) continue
                px[i] = pal[k - 1]
                glass[i] = k in glassIdx
            }
            Sprite(w, h, scale, px, glass)
        }
    }
}

/**
 * Where a drawn house's chimney tops out, in art pixels from the sprite's top left: a narrow run of columns
 * standing clear above the roof on both sides of it. Null when the house has no chimney.
 */
fun chimneyTop(s: Sprite): Pair<Int, Int>? {
    val top = IntArray(s.w) { x -> (0 until s.h).firstOrNull { s.px[it * s.w + x] != 0 } ?: s.h }
    val k = s.scale
    var best: Triple<Int, Int, Int>? = null
    for (a in 2 * k until s.w - 2 * k) for (wd in 3 * k..12 * k) {
        val b = a + wd - 1
        if (b + 2 * k >= s.w) break
        val peak = (a..b).maxOf { top[it] }
        val clear = minOf(top[a - 2 * k], top[b + 2 * k]) - peak
        if (clear >= 4 * k && (best == null || clear > best.third)) best = Triple((a + b) / 2, (a..b).minOf { top[it] }, clear)
    }
    return best?.let { it.first / k to it.second / k }
}

/**
 * Draws [s] standing on art row by - 1, centred on art pixel cx, mirrored when [flip], at the buffer's own density
 * (picking the nearest of the sprite's pixels when the two differ). Every window pane it paints is handed to
 * [pane] in fine pixels, so a scene can light the windows after it has darkened the evening. [dy] nudges it down
 * by fine pixels, for a gentle bob.
 */
fun Buf.blit(s: Sprite, cx: Int, by: Int, flip: Boolean = false, dy: Int = 0, pane: ((Int, Int) -> Unit)? = null) {
    val ow = s.w * this.s / s.scale
    val oh = s.h * this.s / s.scale
    val x0 = cx * this.s + this.s / 2 - ow / 2
    val y0 = by * this.s - oh + dy
    val f = s.scale / this.s
    for (j in 0 until oh) for (i in 0 until ow) {
        val sx = i * s.scale / this.s
        val sy = j * s.scale / this.s
        val k = sy * s.w + (if (flip) s.w - 1 - sx else sx)
        val c = if (f > 1) average(s, sx, sy, f, flip) else s.px[k]
        if (c == 0) continue
        fine(x0 + i, y0 + j, c)
        if (pane != null && s.glass[k]) pane(x0 + i, y0 + j)
    }
}

/** The colour of an f×f block of a sprite drawn into a coarser buffer: its average, or empty if mostly empty. */
private fun average(s: Sprite, x: Int, y: Int, f: Int, flip: Boolean): Int {
    var r = 0
    var g = 0
    var b = 0
    var n = 0
    for (j in y until minOf(y + f, s.h)) for (i in x until minOf(x + f, s.w)) {
        val c = s.px[j * s.w + (if (flip) s.w - 1 - i else i)]
        if (c == 0) continue
        r += (c shr 16) and 0xFF; g += (c shr 8) and 0xFF; b += c and 0xFF; n++
    }
    if (n * 2 < f * f) return 0
    return (0xFF shl 24) or ((r / n) shl 16) or ((g / n) shl 8) or (b / n)
}
