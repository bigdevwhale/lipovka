package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.Phase
import app.lipovka.domain.Sky
import java.time.LocalDate
import kotlin.math.PI
import kotlin.math.abs
import kotlin.math.cos
import kotlin.math.floor
import kotlin.math.roundToInt
import kotlin.math.sin

/** The sky, the light of the hour and the weather falling over a scene. */
object Air {
    fun skyRamp(e: Env): IntArray {
        if (e.sky.grey) return when (e.phase) {
            Phase.NIGHT -> R.night.copyOfRange(1, 5)
            Phase.EVENING -> intArrayOf(rgb(0x1a2234), rgb(0x283248), rgb(0x3a445a))
            Phase.DUSK, Phase.DAWN -> intArrayOf(rgb(0x4a4a62), rgb(0x6a6478), rgb(0x8a7c88), rgb(0xa4949a))
            else -> R.overcast
        }
        return when (e.phase) {
            Phase.NIGHT -> R.night.copyOfRange(0, 5)
            Phase.EVENING -> R.night.copyOfRange(2, 7)
            Phase.DUSK -> R.dusk
            Phase.DAWN -> R.dawn
            Phase.MORNING -> R.morning
            Phase.DAY -> R.day
        }
    }

    /** The colour the whole outdoors is tinted with at this hour, and how strongly. */
    fun tint(e: Env): Pair<Int, Float> = when (e.phase) {
        Phase.NIGHT -> rgb(0x2a3866) to .80f
        Phase.EVENING -> rgb(0x3a4278) to .66f
        Phase.DUSK -> rgb(0xb07a98) to .34f
        Phase.DAWN -> rgb(0xc08ca8) to .30f
        Phase.MORNING -> rgb(0xfff0d8) to .10f
        Phase.DAY -> if (e.sky.grey) rgb(0xc4c8d0) to .22f else 0 to 0f
    }

    /** Tints a region (an outdoor scene, or a window) for the hour and the weather. */
    fun grade(b: Buf, e: Env, x0: Int = 0, y0: Int = 0, w: Int = b.w, h: Int = b.h, inside: ((Int, Int) -> Boolean)? = null) {
        val (c, a) = tint(e)
        if (a <= 0f) return
        for (y in y0 until y0 + h) for (x in x0 until x0 + w) if (inside == null || inside(x, y)) b.mul(x, y, c, a)
        if (e.sky.grey && e.phase == Phase.DAY) for (y in y0 until y0 + h) for (x in x0 until x0 + w) if (inside == null || inside(x, y)) b.scr(x, y, rgb(0x707884), .08f)
    }

    fun stars(b: Buf, x0: Int, y0: Int, w: Int, h: Int, t: Int, n: Int = 24, inside: ((Int, Int) -> Boolean)? = null) {
        for (i in 0 until n) {
            val x = x0 + (rnd(i + 3) * w).toInt()
            val y = y0 + (rnd(i + 33) * h).toInt()
            if (inside != null && !inside(x, y)) continue
            val tw = (sin(t * .2 + i * 2.1) + 1) / 2
            if (tw > .25) b.p(x, y, if (i % 4 == 0) rgb(0xfffbe8) else rgb(0xc8d0e8), tw.toFloat())
        }
    }

    /** The moon's age in days (0 new … 14.8 full … 29.5). */
    fun moonAge(d: LocalDate): Double {
        val days = d.toEpochDay() - LocalDate.of(2000, 1, 6).toEpochDay()
        return ((days % 29.530588) + 29.530588) % 29.530588
    }

    /** The moon in its real phase. */
    fun moon(b: Buf, cx: Int, cy: Int, r: Int, d: LocalDate, bg: Int) {
        b.glow(cx, cy, r * 3, rgb(0xe8e4d4), .18f, 4)
        val age = moonAge(d)
        val k = cos(age / 29.53 * 2 * PI) // 1 new, -1 full
        for (j in -r..r) for (i in -r..r) {
            if (i * i + j * j > r * r + r * .6) continue
            val half = kotlin.math.sqrt((r * r - j * j).coerceAtLeast(0).toDouble())
            val edge = k * half
            val lit = if (age < 14.77) i > edge else i < -edge
            b.p(cx + i, cy + j, if (lit) (if (hash(i, j) > .85) rgb(0xd8d2c0) else rgb(0xf4eedc)) else mix(bg, rgb(0x8890a8), .18f))
        }
    }

    /** Soft drifting clouds. */
    fun clouds(b: Buf, x0: Int, y0: Int, w: Int, h: Int, t: Int, e: Env, n: Int = 4, inside: ((Int, Int) -> Boolean)? = null) {
        val (top, bottom) = when {
            e.phase == Phase.NIGHT || e.phase == Phase.EVENING -> rgb(0x2a3450) to rgb(0x1e2640)
            e.phase == Phase.DUSK -> rgb(0x8a6a90) to rgb(0xe89a84)
            e.phase == Phase.DAWN -> rgb(0xb08aa0) to rgb(0xf4b8a0)
            e.sky.grey -> rgb(0xb4b8be) to rgb(0x8c929c)
            else -> rgb(0xffffff) to rgb(0xd8e0ea)
        }
        for (k in 0 until n) {
            val cw = 18 + (rnd(k + 50) * 26).toInt()
            val ch = 3 + (rnd(k + 60) * 3).toInt()
            val cx = x0 + ((rnd(k + 70) * (w + cw) + t * .05 * (1 + k % 2)) % (w + cw)).toInt() - cw
            val cy = y0 + (rnd(k + 80) * (h - ch)).toInt()
            for (j in 0 until ch) for (i in 0 until cw) {
                val ex = abs(i - cw / 2.0) / (cw / 2.0)
                if (ex > 1 - j * .1 - hash(i + k * 31, j) * .12) continue
                val x = cx + i
                val y = cy + j
                if (inside != null && !inside(x, y)) continue
                b.p(x, y, if (j >= ch - 1) bottom else top, .92f)
            }
        }
    }

    /** Rain, snow or sleet falling; [x0..] bounds the region, [inside] masks it (a window). */
    fun precip(b: Buf, e: Env, t: Int, x0: Int, y0: Int, w: Int, h: Int, density: Double = 1.0, still: Boolean = false, inside: ((Int, Int) -> Boolean)? = null) {
        val tt = if (still) 7 else t
        val night = e.phase.dark
        if (e.sky.rain) {
            val n = ((if (e.sky == Sky.DRIZZLE) 40 else if (e.sky == Sky.STORM) 160 else 110) * density * w * h / 20000.0).toInt().coerceAtLeast(6)
            val c = if (night) rgb(0x6a7a9c) else rgb(0xc8d8e4)
            val slant = 1 + (e.wind / 8).coerceAtMost(2.0)
            for (i in 0 until n) {
                val x = x0 + floor(((rnd(i) * (w + 20) - tt * 1.2 * slant) % (w + 20) + (w + 20)) % (w + 20)).toInt() - 10
                val y = y0 + floor((rnd(i + 90) * (h + 10) + tt * 5) % (h + 10)).toInt() - 5
                for (k in 0..2) {
                    val px = (x - k * slant * .5).roundToInt()
                    val py = y + k
                    if (px < x0 || py < y0 || px >= x0 + w || py >= y0 + h) continue
                    if (inside != null && !inside(px, py)) continue
                    b.p(px, py, c, .5f - k * .12f)
                }
            }
        }
        if (e.sky.snow) {
            val n = (90 * density * w * h / 20000.0).toInt().coerceAtLeast(6)
            for (i in 0 until n) {
                val sp = .5 + rnd(i + 7) * .8
                val x = x0 + (((rnd(i) * w + sin(tt * .1 + i) * 3 + tt * .3 * e.wind / 4) % w + w) % w).toInt()
                val y = y0 + ((rnd(i + 40) * h + tt * sp) % h).toInt()
                if (inside != null && !inside(x, y)) continue
                b.p(x, y, rgb(0xffffff), .9f)
                if (i % 3 == 0) b.p(x + 1, y, rgb(0xe8eef6), .6f)
            }
        }
        if (e.sky == Sky.STORM && !still && (t % 97) in 0..1) {
            for (y in y0 until y0 + h) for (x in x0 until x0 + w) if (inside == null || inside(x, y)) b.scr(x, y, rgb(0xe8ecff), .35f)
        }
    }

    /** Fog lying in drifting bands. */
    fun fog(b: Buf, e: Env, t: Int, x0: Int, y0: Int, w: Int, h: Int, strength: Float = .5f, inside: ((Int, Int) -> Boolean)? = null) {
        if (e.sky != Sky.FOG) return
        val c = if (e.phase.dark) rgb(0x4a5068) else rgb(0xe6e6e0)
        for (y in y0 until y0 + h) for (x in x0 until x0 + w) {
            if (inside != null && !inside(x, y)) continue
            val f = fbm(x * .04 + t * .01, y * .09) - .3
            if (f <= 0) continue
            val lv = floor(f * 10 + (bay(x, y) / 16.0 - .5)) / 4
            if (lv > 0) b.p(x, y, c, (lv * strength).toFloat().coerceAtMost(strength))
        }
    }

    /** Raindrops sliding down window glass. */
    fun glassDrops(b: Buf, e: Env, t: Int, x0: Int, y0: Int, w: Int, h: Int, inside: ((Int, Int) -> Boolean)? = null) {
        if (!e.sky.rain) return
        val n = if (e.sky == Sky.DRIZZLE) 8 else 18
        for (i in 0 until n) {
            val x = x0 + (rnd(i) * w).toInt()
            val y = y0 + ((rnd(i + 20) * h + t * (.4 + rnd(i + 5) * .6)) % h).toInt()
            if (inside != null && !inside(x, y)) continue
            b.p(x, y, rgb(0xb8c8e0), .7f)
            b.p(x, y - 1, rgb(0x8898b8), .45f)
        }
    }

    /** Frost patterns creeping in from the corners of window glass on a cold day. */
    fun frost(b: Buf, e: Env, x0: Int, y0: Int, w: Int, h: Int) {
        if (e.temp > -6) return
        val strength = ((-e.temp - 6) / 14.0).coerceIn(.2, 1.0)
        for (y in y0 until y0 + h) for (x in x0 until x0 + w) {
            val dx = minOf(x - x0, x0 + w - 1 - x).toDouble() / w
            val dy = minOf(y - y0, y0 + h - 1 - y).toDouble() / h
            val d = minOf(dx, dy) + fbm(x * .3, y * .3) * .12
            if (d < .12 * strength) b.p(x, y, rgb(0xeef4fa), (.65 - d * 4).toFloat().coerceIn(.1f, .7f))
        }
    }
}
