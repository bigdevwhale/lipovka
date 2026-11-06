package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.Phase
import java.time.DayOfWeek
import java.time.LocalDate
import kotlin.math.roundToInt
import kotlin.math.sin

/**
 * The post office's tear-off calendar close up, as you stand in front of it to read today's sheet: the red board
 * on its string against the flowered wallpaper, the big day, a sprig of rowan tucked behind, in the light of the hour.
 */
class CalendarScene(private val e: Env, private val date: LocalDate) : Scene(170, 112) {
    override val key: Any = listOf(e.phase, e.sky.grey, date)

    private val dim = when (e.phase) {
        Phase.NIGHT -> .62f
        Phase.EVENING -> .52f
        Phase.DUSK, Phase.DAWN -> .28f
        else -> if (e.sky.grey) .1f else 0f
    }
    private val sunny = !e.sky.grey && (e.phase == Phase.MORNING || e.phase == Phase.DAY)

    override fun base(b: Buf) {
        wall(b)
        // the board's shadow on the wall, then the board, the block and today's sheet
        for (y in BY + 3 until BY + BH + 3) for (x in BX + 3 until BX + BW + 3) b.mul(x, y, rgb(0x6a4a30), .35f)
        board(b)
        page(b, 0)
        rowan(b)
        if (sunny) b.glow(28, 6, 120, rgb(0xfff0c0), .22f, 6)
        if (dim > 0f) for (y in 0 until h) for (x in 0 until w) b.mul(x, y, rgb(0x3a3050), dim)
        // after dark the wall lamp is lit just out of the picture, to the left
        if (e.phase.lamps) { b.glow(-10, 50, 150, rgb(0xffc060), .4f, 7); b.glow(-4, 50, 50, rgb(0xfff0b0), .25f, 5) }
        b.vignette(rgb(0x4a2a1a), .5f)
    }

    private fun wall(b: Buf) {
        for (y in 0 until h) for (x in 0 until w) {
            var c = if (x % 14 < 3) rgb(0xdcc08e) else rgb(0xe6cd9c)
            if (hash(x, y) > .93) c = rgb(0xdfc592)
            b.p(x, y, c)
        }
        for (j in 0 until 9) for (i in 0 until 13) {
            val fx = i * 14 + 7
            val fy = j * 14 + (i % 2) * 7 + 5
            for ((a, c) in listOf(0 to -1, -1 to 0, 1 to 0, 0 to 1)) b.p(fx + a, fy + c, rgb(0xd08a6a))
            b.p(fx, fy, rgb(0xa8463a)); b.p(fx - 2, fy + 2, rgb(0x8a9a5a)); b.p(fx + 2, fy + 2, rgb(0x8a9a5a)); b.p(fx - 1, fy + 3, rgb(0x6a7a44))
        }
        b.vgrad(0, 0, w, 5, intArrayOf(rgb(0x6e4426), rgb(0x9a683c), rgb(0x5a3820)))
    }

    private fun board(b: Buf) {
        // the nail and the string
        b.line(85, 9, BX + 6, BY + 1, rgb(0x6a5a4a)); b.line(85, 9, BX + BW - 7, BY + 1, rgb(0x6a5a4a))
        b.ball(85, 8, 1, R.brass, rgb(0x2a170e))
        b.r(BX - 1, BY - 1, BW + 2, BH + 2, rgb(0x2a1a10))
        for (y in BY until BY + BH) for (x in BX until BX + BW) b.p(x, y, if (hash(x, y) > .9) rgb(0x84261e) else rgb(0x8e2a22))
        b.r(BX, BY, BW, 1, rgb(0xb84a36)); b.r(BX, BY, 1, BH, rgb(0xa23a2c))
        // gilt ornament and the year in the header
        for (x in BX + 3 until BX + BW - 3) {
            b.p(x, BY + 3, rgb(0xc8952e)); b.p(x, BY + 12, rgb(0xc8952e))
            if (x % 4 == 0) b.p(x, BY + 4, rgb(0xe8bf58))
            if (x % 4 == 2) b.p(x, BY + 11, rgb(0xe8bf58))
        }
        val year = date.year.toString()
        b.digits(year, 85 - (year.length * 4 - 1) / 2, BY + 5, rgb(0xe8bf58))
        // the block, thinner as the year runs out, and the gilt lip at the bottom
        val thick = 2 + (date.lengthOfYear() - date.dayOfYear) * 5 / 365
        for (i in 0 until thick) b.r(PX + 1, PY + PH + i, PW - 2, 1, if (i % 2 == 0) rgb(0xd8ccb0) else rgb(0xb8ab90))
        b.r(PX + 1, PY + PH + thick, PW - 2, 1, rgb(0x5a1a14))
        for (x in BX + 4 until BX + BW - 4) if (x % 3 == 0) b.p(x, BY + BH - 3, rgb(0xc8952e))
        // scraps of the sheets torn before, caught under the header
        for (x in PX until PX + PW) {
            if (hash(x, 5) > .4) b.p(x, PY - 1, rgb(0xe6dabd))
            if (hash(x, 9) > .75) b.p(x, PY - 2, rgb(0xd8ccb0))
        }
    }

    /** Today's sheet; [lift] curls its bottom right corner up a few pixels, as if in a draught. */
    private fun page(b: Buf, lift: Int) {
        for (j in 0 until PH) for (i in 0 until PW) {
            if (lift > 0 && (PW - 1 - i) + (PH - 1 - j) < lift) continue
            b.p(PX + i, PY + j, if (j == PH - 1) rgb(0xe8dcc0) else if (hash(i, j) > .96) rgb(0xf4ead0) else rgb(0xfbf3dc))
        }
        val red = date.dayOfWeek == DayOfWeek.SUNDAY || date.dayOfWeek == DayOfWeek.SATURDAY
        val ink = if (red) rgb(0xa33a2c) else rgb(0x2a2420)
        // the month printed on top
        for (i in 0 until 26) if (i % 9 != 8) b.p(PX + PW / 2 - 13 + i, PY + 4, rgb(0xa33a2c))
        b.r(PX + 4, PY + 7, PW - 8, 1, rgb(0xe0d2b4))
        // the day, big
        val d = date.dayOfMonth.toString()
        val s = 5
        val dw = d.length * 3 * s + (d.length - 1) * s
        var x = PX + (PW - dw) / 2
        for (ch in d) {
            val g = BIG[ch] ?: continue
            for (j in 0 until 5) for (i in 0 until 3) if (g[j * 3 + i] == '1') b.r(x + i * s, PY + 11 + j * s, s, s, ink)
            x += 4 * s
        }
        // the weekday, then the small print: sunrise and sunset, the moon
        for (i in 0 until 22) b.p(PX + PW / 2 - 11 + i, PY + 40, ink)
        b.r(PX + 4, PY + 44, PW - 8, 1, rgb(0xe0d2b4))
        b.disc(PX + 8, PY + 49, 2, rgb(0xd9973a))
        for (i in 0 until 14) if (i % 5 != 4) b.p(PX + 13 + i, PY + 49, rgb(0x8e857a))
        b.disc(PX + PW - 9, PY + 49, 2, rgb(0x26375e)); b.p(PX + PW - 8, PY + 48, rgb(0xfbf3dc)); b.p(PX + PW - 8, PY + 49, rgb(0xfbf3dc))
        for (i in 0 until 14) if (i % 5 != 4) b.p(PX + PW - 28 + i, PY + 49, rgb(0x8e857a))
        for (k in 0 until 2) for (i in 0 until PW - 10) if (hash(i, k) > .25) b.p(PX + 5 + i, PY + 53 + k * 2, rgb(0xb8ae9a))
    }

    /** A sprig of rowan tucked behind the board's left side, hanging out over the wallpaper. */
    private fun rowan(b: Buf) {
        val x0 = BX + 3
        val y0 = BY + 22
        b.line(x0, y0, x0 - 20, y0 + 12, rgb(0x5a3a1e))
        for (k in 0 until 6) {
            val x = x0 - 4 - k * 3
            val y = y0 + 2 + k * 2
            b.p(x, y - 2, rgb(0x5c7e50)); b.p(x - 1, y - 3, rgb(0x4a6a3e)); b.p(x + 1, y + 2, rgb(0x6a8a54)); b.p(x, y + 3, rgb(0x4a6a3e))
        }
        for ((u, v) in listOf(0 to 0, 2 to 1, 1 to 3, 3 to -1, -1 to 2, 3 to 3, 5 to 1, 0 to 5, 2 to 5)) {
            b.disc(x0 - 18 + u, y0 + 12 + v, 1, rgb(0xd04a2a)); b.p(x0 - 18 + u, y0 + 11 + v, rgb(0xf08a5a))
        }
    }

    override fun anim(b: Buf, t: Int) {
        // a draught from the door lifts the sheet's corner now and then
        val lift = ((sin(t * .13) - .55) * 7).roundToInt().coerceIn(0, 3)
        if (lift > 0) {
            for (j in 0..lift) for (i in 0..lift) if (i + j <= lift) {
                val x = PX + PW - 1 - i
                val y = PY + PH - 1 - j
                // the wall's red board shows where the corner came up, and the curl shows its pale back
                b.p(x, y, rgb(0x8e2a22))
                if (dim > 0f) b.mul(x, y, rgb(0x3a3050), dim)
                if (i + j == lift || i + j == lift - 1) {
                    b.p(x - lift + i + j, y, rgb(0xd8ccb0)); if (dim > 0f) b.mul(x - lift + i + j, y, rgb(0x3a3050), dim)
                }
            }
        }
        // dust in the sun
        if (sunny) for (i in 0 until 14) {
            val x = ((rnd(i) * 170 + t * .2 * (.5 + rnd(i + 9))) % 170).roundToInt()
            val y = ((rnd(i + 40) * 112 + sin(t * .08 + i) * 3 + t * .06) % 112).roundToInt()
            if ((t + i) % 9 > 1) b.p(x, y, rgb(0xfff8e0), .6f)
        }
    }

    private companion object {
        const val BX = 48
        const val BY = 14
        const val BW = 74
        const val BH = 92
        const val PX = 53
        const val PY = 32
        const val PW = 64
        const val PH = 62
    }
}
