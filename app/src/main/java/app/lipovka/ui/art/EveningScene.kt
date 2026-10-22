package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.Look
import kotlin.math.roundToInt
import kotlin.math.sin

/** The evening table: the kerosene lamp, tea with jam, the open diary, the cat on the windowsill. */
class EveningScene(private val e: Env) : Scene(170, 148) {
    override val key = e.copy(minute = e.minute / 10)

    private val x0 = 92
    private val y0 = 8
    private val ww = 70
    private val wh = 78
    private fun inWin(x: Int, y: Int) = x >= x0 && y >= y0 && x < x0 + ww && y < y0 + wh && !(x in x0 + ww / 2 - 1..x0 + ww / 2 + 1) && y !in y0 + 36..y0 + 38

    override fun base(b: Buf) {
        for (y in 0 until 100) for (x in 0 until 170) {
            val k = x % 11
            b.p(x, y, if (k == 0) rgb(0x140a06) else rp(R.wood, .22 + (fbm(x * .06, y * .25) - .5) * .15, x, y))
        }
        b.r(x0 - 4, y0 - 4, ww + 8, wh + 8, rgb(0x3a2214))
        b.r(x0 - 3, y0 - 3, ww + 6, 1, rgb(0x714528))
        b.vgrad(x0, y0, ww, wh, Air.skyRamp(e))
        if (e.phase.dark && !e.sky.grey) Air.moon(b, x0 + 50, y0 + 18, 5, e.date, rgb(0x151d34))
        for (x in x0 until x0 + ww) {
            val h = (10 + fbm(x * .08, 4.0) * 12).roundToInt()
            for (y in y0 + wh - h until y0 + wh) b.p(x, y, when { e.snow && y < y0 + wh - h + 2 -> R.snow[2]; e.phase.dark -> rgb(0x070a12); e.snow -> R.snow[1]; else -> rp(R.green, .3 + (y - (y0 + wh - h)) / 40.0, x, y) })
        }
        for ((x, y) in listOf(x0 + 10 to y0 + wh - 12, x0 + 24 to y0 + wh - 9, x0 + 46 to y0 + wh - 13, x0 + 58 to y0 + wh - 8)) {
            b.r(x, y, 3, 2, if (e.phase.lamps) rgb(0xf6c04a) else rgb(0x5c7480))
            if (e.phase.lamps) b.glow(x + 1, y + 1, 5, rgb(0xf8b040), .3f, 3)
        }
        if (!e.phase.dark) Air.grade(b, e, x0, y0, ww, wh)
        Air.frost(b, e, x0, y0, ww, wh)
        b.r(x0 + ww / 2 - 1, y0, 3, wh, rgb(0x2a170e))
        b.r(x0, y0 + 36, ww, 3, rgb(0x2a170e))
        for (y in y0 - 6 until y0 + wh + 6) for (i in 0 until 9) {
            val f = sin(i * 1.3 + y * .06)
            b.p(x0 - 6 + i, y, rp(R.red, .35 + f * .15, x0 + i, y))
            b.p(x0 + ww + 5 - i, y, rp(R.red, .3 + f * .15, x0 + i, y))
        }
        b.vgrad(x0 - 8, y0 + wh + 4, ww + 16, 5, intArrayOf(rgb(0xc88e58), rgb(0x8e5a34), rgb(0x3a2214)))
        // the checked tablecloth
        for (y in 98 until 148) for (x in 0 until 170) {
            val cx = x / 6
            val cy = (y - 98) / 4
            val c = if ((cx + cy) % 2 != 0) rgb(0xead8b4) else rgb(0xa33a2c)
            b.p(x, y, if (cx % 2 != 0 && cy % 2 != 0) rgb(0x842a24) else c)
        }
        for (x in 0 until 170) { b.p(x, 98, rgb(0xfbf3dc)); b.p(x, 99, rgb(0xc8b48c)) }
        // kerosene lamp
        b.vol(8, 118, 26, 14, { u, v -> kotlin.math.abs(u - 13) <= 8 + v * .4 }, { u, _ -> .5 - (u - 13) / 30.0 }, R.brass, rgb(0x2a1a08))
        b.vol(10, 98, 22, 22, ell(11.0, 12.0, 10.0, 10.0), sph(8.0, 8.0, 10.0, 10.0, .35), R.glass, rgb(0x1e3036))
        b.vol(16, 64, 10, 36, { u, v -> kotlin.math.abs(u - 5) <= 2.5 + kotlin.math.max(0, v - 24) * .25 }, { u, _ -> if (u < 3) .95 else .55 }, R.glass, rgb(0x1e3036))
        b.r(18, 96, 6, 3, rgb(0x6a4614))
        // the diary and a pen
        b.vol(96, 112, 56, 20, { _, _ -> true }, { _, v -> .85 - v * .01 }, R.paper, rgb(0x3a2a1a))
        b.r(123, 112, 2, 20, rgb(0xc8b48c))
        for (i in 0 until 5) { b.r(100, 116 + i * 3, 20, 1, rgb(0x7a8aa8)); b.r(128, 116 + i * 3, 18 - i * 2, 1, rgb(0x7a8aa8)) }
        for (i in 0 until 14) b.p(100 + i, 116 + (sin(i.toDouble()) * .8).roundToInt(), rgb(0x26375e))
        for (i in 0 until 12) b.p(129 + i, 119 + (sin(i * 1.3) * .8).roundToInt(), rgb(0x26375e))
        b.line(140, 124, 156, 108, rgb(0x141c34)); b.line(141, 124, 157, 108, rgb(0x2c3c64)); b.p(140, 125, rgb(0xc8952e))
        Props.jar(b, 78, 108, R.jam, rgb(0xe8bf58))
        b.line(84, 104, 88, 96, rgb(0xc4c0b8))
        if (e.has(Look.NEWYEAR)) for (k in 0 until 6) b.ball(150 + (k % 3) * 6, 136 + (k / 3) * 5, 2, if (k % 2 == 0) R.apple else R.gold)
        else if (e.has(Look.MASLENITSA)) b.vol(130, 134, 24, 8, ell(12.0, 4.0, 12.0, 4.0), { _, v -> .7 - v * .08 }, R.honey, rgb(0x5a3006))
        b.glow(21, 84, 140, rgb(0xffc060), .42f, 7)
        b.glow(21, 84, 40, rgb(0xfff0b0), .32f, 5)
        b.vignette(rgb(0x1a0a14), .7f, 30.0, 80.0, 170.0, 130.0)
    }

    override fun anim(b: Buf, t: Int) {
        val fl = if (Art.still) 0 else sin(t * .9).roundToInt()
        b.vol(18, 80 + fl, 6, 12, { u, v -> kotlin.math.abs(u - 3.0) <= if (v < 4) v * .6 else 3 - (v - 4) * .25 }, { _, v -> 1 - v / 14.0 },
            intArrayOf(rgb(0xd08c24), rgb(0xf8b040), rgb(0xfff0a0), rgb(0xffffff)))
        b.glow(21, 86, 16, rgb(0xfff0b0), (.12 + .05 * sin(t * .7)).toFloat(), 4)
        Props.kettle(b, 36, 90, .85)
        Props.steam(b, 64, 96, t, 5, 16, .55f)
        Props.cup(b, 64, 106)
        Props.steam(b, 70, 104, t + 5, 4, 12, .5f)
        if (e.phase.dark && !e.sky.grey) Air.stars(b, x0, y0, ww, 40, t, 12) { x, y -> inWin(x, y) && !(x in x0 + 44..x0 + 56 && y in y0 + 12..y0 + 24) }
        Air.clouds(b, x0, y0, ww, 40, t, e, 2) { x, y -> inWin(x, y) }
        Air.precip(b, e, t, x0, y0, ww, wh, .8, still = Art.still) { x, y -> inWin(x, y) }
        Air.glassDrops(b, e, t, x0, y0, ww, wh) { x, y -> inWin(x, y) }
        Air.fog(b, e, t, x0, y0 + 30, ww, wh - 30, .4f) { x, y -> inWin(x, y) }
        Props.cat(b, 112, 62, (sin(t * .18) + 1) / 2)
    }
}
