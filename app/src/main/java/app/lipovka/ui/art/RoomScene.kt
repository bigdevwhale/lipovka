package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.Look
import app.lipovka.domain.Season
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.hypot
import kotlin.math.roundToInt
import kotlin.math.sin

/** A gift as the room shows it. */
data class Gift(val family: String, val variant: String)

/**
 * The postman's attic room above the post office. Gifts from the village find their places: jars and
 * things on the shelves, cards and photos on the wall, knitted things on the line under the window.
 */
class RoomScene(private val e: Env, private val gifts: List<Gift>, private val dog: Boolean) : Scene(170, 236) {
    override val key = listOf(e.copy(minute = e.minute / 10), gifts, dog)

    private val wx = 128
    private val wy = 58
    private val wr = 24
    private val night = e.phase.lamps
    private fun inWin(x: Int, y: Int) = hypot((x - wx).toDouble(), (y - wy).toDouble()) <= wr - .5

    private val shelfSpots = listOf(14, 27, 40, 53, 66, 79).map { it to 124 } + listOf(104, 117, 130, 143).map { it to 140 }
    private val wallSpots = listOf(12 to 80, 28 to 82, 44 to 80, 60 to 84, 76 to 82, 18 to 102, 34 to 104, 50 to 102, 66 to 104, 82 to 100)
    private val lineSpots = listOf(96, 110, 124, 138, 152)

    override fun base(b: Buf) {
        for (y in 0 until 200) for (x in 0 until 170) {
            val k = x % 11
            b.p(x, y, if (k == 0) rgb(0x1e120a) else rp(R.wood, .42 + (fbm(x * .06, y * .25) - .5) * .2 + if (k == 1) .12 else 0.0, x, y))
        }
        for (x in 0 until 170) {
            val yy = (70 - x * .42).toInt()
            for (y in 0 until yy) b.p(x, y, rp(R.wood, .26 + if ((x + y * 2) % 9 == 0) -.08 else 0.0, x, y))
            for (j in 0 until 4) b.p(x, yy + j, rp(R.wood, .55 - j * .12, x, yy))
        }
        window(b)
        herbs(b)
        // floor and the braided rug
        for (y in 196 until 236) for (x in 0 until 170) {
            val k = (y - 196) % 6
            b.p(x, y, if (k == 0) rgb(0x1e100a) else rp(R.wood, .48 + (fbm(x * .04 + k * 3, y * .5) - .5) * .2, x, y))
        }
        val rug = intArrayOf(rgb(0xc05638), rgb(0xe8bf58), rgb(0x304e36), rgb(0xa33a2c), rgb(0xd8c4a0), rgb(0x405890), rgb(0x842a24))
        for (j in -14..14) for (i in -56..56) {
            val d = hypot(i / 56.0, j / 14.0)
            if (d > 1) continue
            b.p(84 + i, 222 + j, rug[(d * 7).toInt().coerceAtMost(6)])
            if ((i + j * 3) % 5 == 0) b.mul(84 + i, 222 + j, rgb(0x806050), .5f)
        }
        shelves(b)
        bed(b)
        desk(b)
        placeGifts(b)
        // valenki by the bed
        for ((x, y) in listOf(100 to 206, 110 to 208)) {
            b.vol(x, y - 14, 7, 16, { u, v -> if (v < 10) u < 6 else true }, { u, _ -> .6 - u * .06 }, R.felt, rgb(0x141212))
            b.vol(x, y - 2, 11, 5, ell(5.0, 2.5, 5.5, 2.5), sph(4.0, 1.0, 6.0, 3.0, .4), R.felt, rgb(0x141212))
            b.r(x, y - 14, 6, 2, rgb(0xa33a2c))
        }
        light(b)
    }

    private fun window(b: Buf) {
        val wall = IntArray(4 * wr * wr) { b.get(wx - wr + it % (2 * wr), wy - wr + it / (2 * wr)) }
        for (j in -wr - 4..wr + 4) for (i in -wr - 4..wr + 4) {
            val d = hypot(i.toDouble(), j.toDouble())
            if (d > wr + 4) continue
            if (d > wr) b.p(wx + i, wy + j, rp(R.wood, .6 - (i + j) / 60.0, wx + i, wy + j))
        }
        b.vgrad(wx - wr, wy - wr, 2 * wr, 2 * wr, Air.skyRamp(e).let { if (e.phase.dark) it else it })
        // the sky is drawn as a square: put the frame and the wall back outside the glass
        frame(b, wall)
        if (e.phase.dark && !e.sky.grey) Air.moon(b, wx + 10, wy - 10, 4, e.date, rgb(0x151d34))
        if (!e.phase.dark && !e.sky.grey) b.disc(wx - 10, wy - 12, 3, rgb(0xfffbe8))
        for (i in -wr..wr) {
            val hgt = (5 + fbm(i * .15, 5.0) * 6).roundToInt()
            for (j in 0 until hgt) {
                val y = wy + wr - j - 2
                if (inWin(wx + i, y)) b.p(wx + i, y, if (e.snow && j > hgt - 2) R.snow[3] else if (e.phase.dark) rgb(0x0a0e18) else rgb(0x3a5a3a))
            }
        }
        for ((i, j) in listOf(-14 to 16, -6 to 14, 6 to 17, 14 to 15)) {
            b.p(wx + i, wy + j, if (night) rgb(0xf6d77a) else rgb(0x8aa0b0))
            b.p(wx + i + 1, wy + j, if (night) rgb(0xf6d77a) else rgb(0x8aa0b0))
        }
        Air.grade(b, e, wx - wr, wy - wr, 2 * wr, 2 * wr) { x, y -> inWin(x, y) }
        Air.frost(b, e, wx - wr, wy - wr, 2 * wr, 2 * wr)
        frame(b, wall)
        b.r(wx - wr, wy - 1, 2 * wr, 2, rgb(0x3a2214))
        b.r(wx - 1, wy - wr, 2, 2 * wr, rgb(0x3a2214))
        for (a in 0 until 64) {
            val an = a / 64.0 * 2 * PI
            b.p((wx + cos(an) * (wr + 4)).roundToInt(), (wy + sin(an) * (wr + 4)).roundToInt(), rgb(0x140a06))
        }
        if (!night && !e.sky.grey) for (y in wy until 236) for (x in 60 until 170) {
            val t = y - wy
            val cx = wx - t * .45
            if (kotlin.math.abs(x - cx) < wr * .7 - t * .02 && bay(x, y) < 6) b.scr(x, y, rgb(0xfff0c0), .1f)
        }
    }

    /** Outside the glass: the round frame, and beyond it the wall as it was before the window. */
    private fun frame(b: Buf, wall: IntArray) {
        for (j in -wr until wr) for (i in -wr until wr) {
            val x = wx + i
            val y = wy + j
            if (inWin(x, y)) continue
            b.p(x, y, if (hypot(i.toDouble(), j.toDouble()) <= wr + 4) rp(R.wood, .6 - (i + j) / 60.0, x, y) else wall[(j + wr) * 2 * wr + i + wr])
        }
    }

    private fun herbs(b: Buf) {
        val cols = listOf(rgb(0x5c7e50) to rgb(0xa8bc7a), rgb(0x8e6c9c) to rgb(0xb494bc), rgb(0xd0a040) to rgb(0xf0d070), rgb(0x7e9c62) to rgb(0x4a6a3a))
        for ((i, p) in listOf(24 to 52, 40 to 45, 56 to 38, 72 to 31).withIndex()) {
            val (x, y) = p
            b.line(x, y, x, y + 5, rgb(0xc8b080))
            for (k in 0 until 26) {
                val xx = x + ((hash(k, i) - .5) * (2 + k * .25)).roundToInt()
                b.p(xx, y + 5 + (k * .5).roundToInt(), if (k % 2 == 0) cols[i].first else cols[i].second)
            }
            b.r(x - 1, y + 5, 3, 2, rgb(0x8a3a2a))
        }
    }

    private fun shelves(b: Buf) {
        b.vgrad(4, 126, 84, 4, intArrayOf(rgb(0xe0ac74), rgb(0x8e5a34), rgb(0x3a2214)))
        b.line(10, 130, 14, 135, rgb(0x3a2214)); b.line(80, 130, 84, 135, rgb(0x3a2214))
        b.vgrad(96, 142, 58, 3, intArrayOf(rgb(0xe0ac74), rgb(0x8e5a34), rgb(0x3a2214)))
        // the line under the window
        for (x in 86 until 170) b.p(x, (92 + sin((x - 86) / 84.0 * PI) * 6).roundToInt(), rgb(0xc8b080))
    }

    private fun bed(b: Buf) {
        b.vol(154, 124, 16, 84, { _, _ -> true }, { u, _ -> .6 - u * .04 }, R.wood, rgb(0x140a06))
        b.ball(162, 122, 3, R.wood, rgb(0x140a06))
        b.vol(96, 178, 60, 26, { _, _ -> true }, { _, _ -> .5 }, R.wood, rgb(0x140a06))
        b.vol(100, 152, 30, 14, ell(15.0, 7.0, 15.0, 7.0), sph(12.0, 5.0, 16.0, 8.0, .45), R.cream, rgb(0x4a3a2a))
        b.vol(124, 150, 30, 14, ell(15.0, 7.0, 15.0, 7.0), sph(12.0, 5.0, 16.0, 8.0, .45), R.cream, rgb(0x4a3a2a))
        val patch = intArrayOf(rgb(0xa33a2c), rgb(0xe0ac74), rgb(0x3c6c44), rgb(0xe8bf58), rgb(0x405890), rgb(0xd8c4a0), rgb(0x8e2434), rgb(0x7e9c62), rgb(0xc05638))
        for (y in 160 until 192) for (x in 94 until 156) {
            val pi = (x - 94) / 8
            val pj = (y - 160) / 8
            var c = patch[(hash(pi, pj) * patch.size).toInt()]
            val lx = (x - 94) % 8
            val ly = (y - 160) % 8
            if (lx == 0 || ly == 0) c = rgb(0x2a1a10) else if ((lx == 1 || ly == 1) && bay(x, y) < 8) c = rgb(0xfbf3dc)
            b.p(x, y, c)
            if (y > 184) b.mul(x, y, rgb(0x604030), .4f)
        }
        var x = 94
        while (x < 156) { b.p(x, 192, rgb(0xfbf3dc)); b.p(x + 1, 193, rgb(0xfbf3dc)); x += 2 }
    }

    private fun desk(b: Buf) {
        b.vgrad(0, 168, 76, 6, intArrayOf(rgb(0xe0ac74), rgb(0xab7244), rgb(0x55331e), rgb(0x3a2214)))
        for (y in 174 until 200) for (x in 0 until 76) b.p(x, y, rp(R.wood, .32 + (fbm(x * .05, y * .3) - .5) * .15, x, y))
        b.r(70, 174, 6, 26, rgb(0x22130b))
        for ((x, y, c) in listOf(Triple(42, 154, rgb(0x842a24)), Triple(42, 149, rgb(0x304474)), Triple(44, 145, rgb(0x426442)))) {
            b.r(x, y, 26, 5, c); b.r(x, y + 1, 25, 3, rgb(0xf2e2bb)); b.r(x + 24, y + 1, 2, 3, c)
        }
        b.r(22, 163, 22, 6, rgb(0x0e0806)); b.r(22, 162, 10, 6, rgb(0xfbf3dc)); b.r(33, 162, 10, 6, rgb(0xf2e2bb))
        for (i in 0 until 3) { b.r(23, 164 + i * 2, 8, 1, rgb(0xa8906a)); b.r(34, 164 + i * 2, 7, 1, rgb(0xa8906a)) }
        b.line(40, 160, 46, 166, rgb(0x2a2a34))
        Props.kettle(b, 48, 145, .8)
        b.r(6, 166, 14, 3, rgb(0x1e2a1a))
        b.r(12, 138, 2, 28, rgb(0xc8952e)); b.r(13, 138, 1, 28, rgb(0xfbe4a0))
        b.vol(0, 124, 26, 16, { u, v -> kotlin.math.abs(u - 12.5) <= 5 + v * .55 }, { u, v -> .6 - (u - 12) / 30.0 - v * .02 }, R.lampG, rgb(0x08140c))
        b.r(1, 139, 24, 1, if (night) rgb(0xfff0b0) else rgb(0xa8bca0))
        if (e.has(Look.NEWYEAR)) { Props.spruce(b, 52, 104, 18); for (k in 0 until 5) b.p(56 + (hash(k, 9) * 8).toInt(), 108 + (hash(9, k) * 10).toInt(), intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[k % 3]) }
    }

    private fun placeGifts(b: Buf) {
        var shelf = 0
        var wall = 0
        var line = 0
        for (g in gifts) {
            when (ItemArt.slot(g.family)) {
                ItemArt.Slot.SHELF -> if (shelf < shelfSpots.size) { val (x, y) = shelfSpots[shelf++]; ItemArt.draw(b, g.family, g.variant, x, y + 2) }
                ItemArt.Slot.WALL -> if (wall < wallSpots.size) {
                    val (x, y) = wallSpots[wall++]
                    ItemArt.draw(b, g.family, g.variant, x, y)
                    b.ball(x, y - ItemArt.H + 3, 1, R.red)
                }
                ItemArt.Slot.LINE -> if (line < lineSpots.size) {
                    val x = lineSpots[line++]
                    val y = (92 + sin((x - 86) / 84.0 * PI) * 6).roundToInt()
                    ItemArt.draw(b, g.family, g.variant, x, y + ItemArt.H)
                    b.r(x - 1, y - 1, 3, 2, rgb(0x8e5a34))
                }
            }
        }
        // until the village fills them, a few things of the postman's own
        if (shelf == 0) { Props.jar(b, 8, 113, R.jam); Props.jar(b, 19, 113, R.honey, rgb(0x3c6c44)) }
        if (wall == 0) { ItemArt.draw(b, "postcard", "sea", 16, 82); ItemArt.draw(b, "photo", "old", 34, 82) }
    }

    private fun light(b: Buf) {
        if (night) {
            for (y in 0 until 236) for (x in 0 until 170) if (!inWin(x, y)) b.mul(x, y, rgb(0x3a2a48), .55f)
            b.glow(13, 150, 120, rgb(0xffc060), .5f, 7)
            b.glow(13, 146, 40, rgb(0xfff0b0), .35f, 5)
            b.vignette(rgb(0x1a0a14), .75f, 40.0, 140.0, 150.0, 170.0)
        } else {
            if (e.sky.grey) for (y in 0 until 236) for (x in 0 until 170) if (!inWin(x, y)) b.mul(x, y, rgb(0xb8b8c8), .25f)
            b.glow(wx, wy + 40, 110, rgb(0xfff0d0), .18f, 5)
            b.vignette(rgb(0x2a1a14), .55f)
        }
    }

    override fun anim(b: Buf, t: Int) {
        if (e.phase.dark && !e.sky.grey) Air.stars(b, wx - wr, wy - wr, 2 * wr, wr, t, 10) { x, y -> inWin(x, y) && !(x in wx + 5..wx + 15 && y in wy - 15..wy - 5) }
        Air.clouds(b, wx - wr, wy - wr, 2 * wr, wr, t, e, 2) { x, y -> inWin(x, y) }
        Air.precip(b, e, t, wx - wr, wy - wr, 2 * wr, 2 * wr, .6, still = Art.still) { x, y -> inWin(x, y) }
        Air.glassDrops(b, e, t, wx - wr, wy - wr, 2 * wr, 2 * wr) { x, y -> inWin(x, y) }
        Props.steam(b, 74, 148, t, 4, 14, .55f)
        if (night) b.glow(13, 150, 30, rgb(0xfff0b0), (.05 + .04 * sin(t * .5)).toFloat(), 3)
        Props.cat(b, 104, 146, (sin(t * .18) + 1) / 2)
        if (dog) People.dogLying(b, 30, 214, (sin(t * .2) + 1) / 2)
        if (e.season == Season.WINTER && night) b.glow(wx, wy, 10, rgb(0xc8d0e8), .05f, 3)
    }
}
