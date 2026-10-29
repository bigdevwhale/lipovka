package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.Leaves
import app.lipovka.domain.Look
import app.lipovka.domain.Phase
import app.lipovka.domain.Season
import app.lipovka.domain.Sky
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.roundToInt
import kotlin.math.sin

/**
 * The post office in the morning (or whenever it is): the window onto the village, the wall clock with
 * the cat face, the pigeonholes, the desk with the kettle, the letters and the sleeping cat.
 */
class PostOffice(
    private val e: Env,
    /** Letters lying on the desk: 0 hides the pile. */
    private val letters: Int,
    private val dog: Boolean,
) : Scene(170, 214) {
    override val key = listOf(e.copy(minute = e.minute / 5), letters.coerceAtMost(6), dog)

    private val wx = 12
    private val wy = 20
    private val ww = 56
    private val wh = 72

    /** Where the sky shows through the window, and where the view outside does, past the frame and the curtains. */
    private var skyShows = Mask(0, 0)
    private var outShows = Mask(0, 0)
    private val dark = e.phase.dark
    private val dim = when (e.phase) {
        Phase.NIGHT -> .72f
        Phase.EVENING -> .62f
        Phase.DUSK, Phase.DAWN -> .32f
        else -> if (e.sky.grey) .12f else 0f
    }
    private val sunny = !e.sky.grey && (e.phase == Phase.MORNING || e.phase == Phase.DAY)

    private fun inWindow(x: Int, y: Int) = x >= wx && y >= wy && x < wx + ww && y < wy + wh

    private fun inBeam(x: Int, y: Int): Boolean {
        for (t in 0..90) {
            val px = x - t * .95
            val py = y - t * .7
            if (px >= wx + 2 && px < wx + ww - 2 && py >= wy + 2 && py < wy + wh - 2) return true
            if (py < wy) return false
        }
        return false
    }

    override fun base(b: Buf) {
        wall(b)
        view(b)
        b.cover(skyShows, outShows) {
            curtains(b)
            sill(b)
            clock(b)
            calendar(b)
            pigeonholes(b)
            hooks(b)
            desk(b)
        }
        if (sunny) for (y in wy until 214) for (x in wx until 170) if (inBeam(x, y)) {
            val edge = !inBeam(x + 2, y) || !inBeam(x - 2, y)
            if (!edge || bay(x, y) > 7) b.scr(x, y, rgb(0xfff0c0), if (y in 138..151) .32f else .16f)
        }
        b.cover(skyShows, outShows) { props(b) }
        // The room darkens with the hour; the lamp takes over.
        if (dim > 0f) {
            for (y in 0 until 214) for (x in 0 until 170) if (!inWindow(x, y)) b.mul(x, y, rgb(0x3a3050), dim)
        }
        if (e.phase.lamps) lamp(b)
        b.vignette(rgb(0x4a2a1a), if (dark) .4f else .55f)
    }

    private fun wall(b: Buf) {
        for (y in 0 until 116) for (x in 0 until 170) {
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
        b.vgrad(0, 0, 170, 5, intArrayOf(rgb(0x6e4426), rgb(0x9a683c), rgb(0x5a3820)))
        for (y in 112 until 140) for (x in 0 until 170) {
            val k = x % 10
            b.p(x, y, when (k) {
                0 -> rgb(0x3a2214)
                1 -> rp(R.wood, .78, x, y)
                else -> rp(R.wood, .55 + fbm(x * .1, y * .4) * .15, x, y)
            })
        }
        b.vgrad(0, 110, 170, 4, intArrayOf(rgb(0xc88e58), rgb(0x8e5a34), rgb(0x55331e)))
    }

    /** The village through the window: sky, hills, roofs, birches, the weather. */
    private fun view(b: Buf) {
        b.r(wx - 4, wy - 4, ww + 8, wh + 8, rgb(0x55331e))
        b.r(wx - 3, wy - 3, ww + 6, wh + 6, rgb(0x8e5a34))
        b.r(wx - 3, wy - 3, ww + 6, 1, rgb(0xc88e58))
        b.r(wx - 1, wy - 1, ww + 2, wh + 2, rgb(0x3a2214))
        b.vgrad(wx, wy, ww, wh - 16, Air.skyRamp(e))
        val sunX = wx + 8 + ((e.minute - 360).coerceIn(0, 720) / 720.0 * (ww - 16)).roundToInt()
        if (!e.sky.grey && !dark && e.phase != Phase.NIGHT) {
            val sy = wy + 26 - (sin((e.minute - 360) / 720.0 * PI) * 16).roundToInt()
            b.glow(sunX, sy, 20, rgb(0xfff6d0), .6f, 6)
            b.disc(sunX, sy, 4, rgb(0xfffbe8))
        }
        if (dark && !e.sky.grey) Air.moon(b, wx + 40, wy + 14, 4, e.date, rgb(0x151d34))
        skyShows = Mask(w, h).apply { open(wx, wy, ww, wh) }
        outShows = Mask(w, h).apply { open(wx, wy, ww, wh) }
        b.cover(skyShows) {
            // far hills
            for (x in wx until wx + ww) {
                val h1 = wy + 44 + (fbm(x * .15, 1.0) * 6).roundToInt()
                for (y in h1 until wy + 56) b.p(x, y, rp(if (e.snow) intArrayOf(rgb(0xa8b4c8), rgb(0xbac4d4), rgb(0xd0d8e2)) else intArrayOf(rgb(0x6a8a94), rgb(0x7c9aa0), rgb(0x90aaa8)), (y - h1) / 12.0, x, y))
            }
            val ground = when {
                e.snow -> R.snow
                e.season == Season.SUMMER -> R.grassSummer
                e.season == Season.SPRING -> R.grassSpring
                else -> R.grass
            }
            for (x in wx until wx + ww) {
                val h2 = wy + 54 + (sin(x * .12) * 2).roundToInt()
                for (y in h2 until wy + wh) b.p(x, y, rp(ground, .75 - (y - h2) / 24.0, x, y))
            }
            for ((x, y, c) in listOf(Triple(wx + 8, wy + 52, rgb(0xa83e28)), Triple(wx + 20, wy + 54, rgb(0x7c4e30)), Triple(wx + 34, wy + 51, rgb(0xa83e28)))) {
                for (j in 0 until 4) b.r(x - j, y + j, 2 + j * 2, 1, if (e.snow && j < 2) R.snow[4] else c)
                b.r(x - 3, y + 4, 8, 3, rgb(0xc4a272))
                b.p(x - 1, y + 5, if (e.phase.lamps) rgb(0xffd060) else rgb(0x6a8090))
            }
            Props.birch(b, wx + 44, wy + 36, 26, e.leaves)
            Props.birch(b, wx + 3, wy + 42, 20, e.leaves, alt = true)
            var x = wx
            while (x < wx + ww) { b.r(x, wy + 62, 1, 5, rgb(0x8a6a44)); x += 3 }
            b.r(wx, wy + 63, ww, 1, rgb(0x8a6a44))
            if (e.has(Look.CRANES) && !dark) for (i in 0 until 7) {
                val cx = wx + 14 + i * 3
                val cy = wy + 12 + kotlin.math.abs(i - 3) * 2
                b.p(cx, cy, rgb(0x2a2a30)); b.p(cx - 1, cy - 1, rgb(0x2a2a30)); b.p(cx + 1, cy - 1, rgb(0x2a2a30))
            }
        }
        Air.grade(b, e, wx, wy, ww, wh)
        if (e.phase.lamps) for ((xx, yy) in listOf(wx + 7 to wy + 57, wx + 33 to wy + 56)) b.glow(xx, yy, 4, rgb(0xffc860), .5f, 3)
        Air.frost(b, e, wx, wy, ww, wh)
        for (i in 0 until 10) b.line((wx + 8 + i).toDouble(), (wy + wh - 4).toDouble(), (wx + 20 + i).toDouble(), (wy + 8).toDouble(), rgb(0xffffff), .06f)
        b.cover(skyShows, outShows) {
            b.r(wx + ww / 2 - 1, wy, 2, wh, rgb(0x55331e))
            b.r(wx, wy + 30, ww, 2, rgb(0x55331e))
            b.r(wx + ww / 2 - 1, wy, 1, wh, rgb(0x8e5a34))
        }
    }

    private fun curtains(b: Buf) {
        for (x in wx - 6 until wx + ww + 6) for (y in wy - 6 until wy + 6) {
            if (y > wy + 3 + (kotlin.math.abs(sin(x * .4)) * 2).roundToInt()) continue
            b.p(x, y, if ((x + y) % 3 == 0) rgb(0xe8dcc4) else rgb(0xfbf6ea))
        }
        fun side(x0: Int, dir: Int) {
            for (y in wy + 4 until wy + wh + 8) {
                val tie = wy + 52
                val wd = if (y < tie) 10 - ((y - wy).toDouble() / (tie - wy) * 5).roundToInt() else 5 + ((y - tie) * .35).roundToInt()
                for (i in 0 until wd) {
                    val x = if (dir > 0) x0 + i else x0 - i
                    val f = sin(i * 1.4 + y * .05)
                    b.p(x, y, when {
                        f > .3 -> rgb(0xfbf6ea)
                        f > -.4 -> rgb(0xece2cc)
                        else -> rgb(0xd4c6aa)
                    })
                }
            }
            val tx = if (dir > 0) x0 + 3 else x0 - 4
            b.r(tx, wy + 51, 3, 3, rgb(0xb03030)); b.p(tx + 1, wy + 54, rgb(0xb03030))
        }
        side(wx - 5, 1)
        side(wx + ww + 4, -1)
    }

    private fun sill(b: Buf) {
        b.vgrad(wx - 6, wy + wh + 3, ww + 12, 4, intArrayOf(rgb(0xe0ac74), rgb(0xab7244), rgb(0x55331e)))
        // geranium
        b.vol(wx + 6, wy + wh - 6, 10, 9, { u, v -> kotlin.math.abs(u - 4.5) <= 4.5 - v * .15 }, { u, _ -> .6 - u * .05 }, R.brick, rgb(0x2a0e0a))
        b.r(wx + 5, wy + wh - 7, 12, 2, rgb(0x8e3a24))
        for (k in 0 until 26) {
            val x = wx + 5 + (hash(k, 3) * 12).roundToInt()
            val y = wy + wh - 18 + (hash(k, 9) * 11).roundToInt()
            b.p(x, y, rp(R.green, .4 + hash(k, 1) * .4, x, y)); b.p(x + 1, y, rp(R.green, .55, x, y))
        }
        for ((x, y) in listOf(wx + 7 to wy + wh - 18, wx + 13 to wy + wh - 20, wx + 16 to wy + wh - 15)) {
            b.disc(x, y, 2, rgb(0xd8303a)); b.p(x - 1, y - 1, rgb(0xff7a70)); b.p(x + 1, y + 1, rgb(0x8a1420))
        }
        // a glass with whatever the season puts in it
        b.vol(wx + 40, wy + wh - 8, 6, 11, { _, _ -> true }, { u, _ -> if (u == 1) .95 else .45 }, R.glass, rgb(0x2a4048))
        when {
            e.has(Look.NEWYEAR) -> Props.spruce(b, wx + 38, wy + wh - 24, 16)
            e.has(Look.LILAC) -> for (k in 0 until 14) b.p(wx + 41 + (hash(k, 5) * 6).toInt(), wy + wh - 20 + (hash(k, 6) * 9).toInt(), if (k % 3 == 0) rgb(0x6a4a7a) else rgb(0xb494bc))
            e.has(Look.MUSHROOMS) || e.season == Season.AUTUMN -> {
                b.line(wx + 43, wy + wh - 8, wx + 46, wy + wh - 20, rgb(0x5a3a1e))
                for ((u, v) in listOf(46 to 21, 44 to 17, 45 to 14)) b.p(wx + u, wy + wh - v, if (e.leaves == Leaves.FALLING) rgb(0xc04a2a) else rgb(0xe8b443))
            }
            e.season == Season.SPRING -> { b.line(wx + 43, wy + wh - 8, wx + 44, wy + wh - 20, rgb(0x5a4a3a)); for (j in 0 until 4) b.p(wx + 44 + j % 2, wy + wh - 19 + j * 3, rgb(0xe8e4d8)) }
            else -> for (k in 0 until 8) b.p(wx + 42 + (hash(k, 2) * 4).toInt(), wy + wh - 16 + (hash(k, 4) * 7).toInt(), if (k % 2 == 0) rgb(0x4a7aca) else rgb(0x5c7e50))
        }
    }

    private fun clock(b: Buf) {
        val cx = 92
        for (j in 0 until 7) b.r((cx - 2 - j * 1.6).roundToInt(), 10 + j, (4 + j * 3.2).roundToInt(), 1, rp(R.wood, .7 - j * .04, cx, 10 + j))
        b.p(cx, 8, rgb(0xc8952e)); b.p(cx, 9, rgb(0xc8952e))
        b.vol(cx - 12, 17, 25, 26, { _, _ -> true }, { u, v -> .62 - u * .012 - if (v > 22) .15 else 0.0 }, R.wood, rgb(0x1e100a))
        b.ball(cx, 28, 8, intArrayOf(rgb(0xb4a282), rgb(0xd6c6a4), rgb(0xecdfc0), rgb(0xf8f0da)), rgb(0x2a1a10))
        for (a in 0 until 12) {
            val an = a / 12.0 * PI * 2
            b.p((cx + cos(an) * 7).roundToInt(), (28 + sin(an) * 7).roundToInt(), rgb(0x4a3a2a))
        }
        for ((x, y) in listOf(cx - 4 to 22, cx - 3 to 21, cx + 3 to 21, cx + 4 to 22)) b.p(x, y, rgb(0x3a2a1a))
        // the real time
        val m = e.minute % 60
        val h = (e.minute / 60) % 12 + m / 60.0
        val ma = m / 60.0 * 2 * PI - PI / 2
        val ha = h / 12.0 * 2 * PI - PI / 2
        b.line(cx.toDouble(), 28.0, cx + cos(ma) * 6, 28 + sin(ma) * 6, rgb(0x1e100a))
        b.line(cx.toDouble(), 28.0, cx + cos(ha) * 4, 28 + sin(ha) * 4, rgb(0x1e100a))
        b.r(cx - 10, 38, 20, 4, rgb(0x55331e))
        var i = 0
        while (i < 20) { b.p(cx - 10 + i, 39, rgb(0xc8952e)); i += 4 }
    }

    private fun calendar(b: Buf) {
        b.r(106, 22, 13, 20, rgb(0x2a1a10))
        b.r(107, 23, 11, 18, rgb(0xfbf3dc))
        b.r(107, 23, 11, 4, rgb(0xa33a2c))
        b.p(109, 22, rgb(0x8e857a)); b.p(115, 22, rgb(0x8e857a))
        val d = e.date.dayOfMonth.toString()
        b.digits(d, if (d.length == 1) 111 else 108, 29, rgb(0xa33a2c))
        b.r(108, 36, 9, 1, rgb(0x55504c)); b.r(108, 38, 7, 1, rgb(0x8e857a))
    }

    private fun pigeonholes(b: Buf) {
        b.vol(120, 6, 50, 132, { _, _ -> true }, { u, _ -> .6 - (if (u > 46) .25 else 0.0) + (if (u < 2) .15 else 0.0) }, R.wood, rgb(0x1e100a))
        for (c in 0 until 4) for (r in 0 until 7) {
            val x = 122 + c * 12
            val y = 20 + r * 15
            b.r(x, y, 10, 12, rgb(0x1e120a)); b.r(x, y, 10, 2, rgb(0x120a06)); b.r(x, y, 1, 12, rgb(0x160c08))
            val k = hash(c, r)
            if (k > .25) {
                val ec = intArrayOf(rgb(0xf8eed4), rgb(0xdce8f0), rgb(0xf4dcd4), rgb(0xecdcb6))[(hash(r, c) * 4).toInt()]
                val lean = if (k > .6) 1 else 0
                b.r(x + 2 - lean, y + 4, 7, 7, rgb(0x3a2a1a)); b.r(x + 3 - lean, y + 5, 5, 5, ec); b.p(x + 5 - lean, y + 7, rgb(0xa33a2c))
                if (k > .75) { b.r(x + 5, y + 3, 4, 8, rgb(0x3a2a1a)); b.r(x + 6, y + 4, 2, 6, rgb(0xecdcb6)) }
            } else if (k > .12) {
                b.vol(x + 2, y + 6, 7, 5, { _, _ -> true }, { _, v -> .6 - v * .1 }, R.paper)
                b.line(x + 5, y + 6, x + 5, y + 10, rgb(0x7a4a2a))
            }
            b.r(x + 3, y + 12, 4, 1, rgb(0xe8bf58))
        }
        for ((x, y, w) in listOf(Triple(124, 0, 14), Triple(140, 1, 12), Triple(154, -1, 12))) {
            val h = 6
            b.vol(x, y, w, h, { _, _ -> true }, { u, v -> .7 - u.toDouble() / w * .3 - v * .05 }, R.paper, rgb(0x3a2a1a))
            b.line(x + w / 2, y, x + w / 2, y + h, rgb(0x7a4a2a)); b.line(x, y + h / 2, x + w, y + h / 2, rgb(0x7a4a2a))
        }
        if (e.has(Look.NEWYEAR)) for (x in 0 until 170) {
            val y = 6 + (sin(x * .12) * 3).roundToInt()
            b.p(x, y, rgb(0x3c6c44))
            if (x % 9 == 0) b.disc(x, y + 2, 1, intArrayOf(rgb(0xd83a3a), rgb(0xe8bf58), rgb(0x4a7aca))[(x / 9) % 3])
        }
    }

    private fun hooks(b: Buf) {
        b.vgrad(76, 80, 40, 4, intArrayOf(rgb(0xc88e58), rgb(0x8e5a34), rgb(0x3a2214)))
        for (x in listOf(80, 94, 108)) b.ball(x, 84, 1, R.brass, rgb(0x2a170e))
        b.vol(73, 86, 16, 8, { u, v -> if (v < 5) ((u - 8) / 7.0).let { it * it } + ((v - 5) / 5.0).let { it * it } <= 1 else kotlin.math.abs(u - 8) < 7.6 },
            sph(6.0, 2.0, 9.0, 6.0, .2), R.coat, rgb(0x06080e))
        b.r(73, 92, 17, 2, rgb(0x08080c)); b.r(79, 88, 4, 2, rgb(0xe8bf58))
        // the bag is on its hook only when there's nothing to carry
        if (letters == 0) {
            b.line(94, 84, 102, 96, rgb(0x3e2416)); b.line(108, 84, 104, 96, rgb(0x3e2416))
            b.vol(90, 95, 24, 24, { u, v -> !(v > 20 && (u < 2 || u > 21)) }, { u, v -> .6 - u * .012 - v * .008 + (fbm(u * .5, v * .5) - .5) * .2 }, R.leather, rgb(0x140a06))
            b.vol(90, 95, 24, 12, { u, v -> v < 10 - if (kotlin.math.abs(u - 12) > 9) 2 else 0 }, { u, v -> .72 - u * .01 - v * .02 }, R.leather, rgb(0x140a06))
            b.r(100, 103, 4, 5, rgb(0xe8bf58)); b.r(101, 104, 2, 3, rgb(0x6a4614))
        }
    }

    private fun desk(b: Buf) {
        for (y in 138 until 152) for (x in 0 until 170) {
            val pl = (y - 138) / 5
            b.p(x, y, if ((y - 138) % 5 == 0) rgb(0x6e4426) else rp(R.wood, .78 - (y - 138) * .012 + (fbm(x * .08 + pl * 9, y * .6) - .5) * .25, x, y))
        }
        b.vgrad(0, 151, 170, 3, intArrayOf(rgb(0xe0ac74), rgb(0xab7244), rgb(0x714528)))
        for (y in 154 until 214) for (x in 0 until 170) b.p(x, y, rp(R.wood, .48 + (fbm(x * .05, y * .3) - .5) * .2 - (y - 154) * .003, x, y))
        for ((x, y, w, h) in listOf(listOf(8, 160, 72, 24), listOf(90, 160, 72, 24), listOf(8, 190, 154, 22))) {
            b.r(x, y, w, 1, rgb(0x3a2214)); b.r(x, y, 1, h, rgb(0x3a2214)); b.r(x, y + h - 1, w, 1, rgb(0xc88e58)); b.r(x + w - 1, y, 1, h, rgb(0xc88e58)); b.r(x + 1, y + 1, w - 2, 1, rgb(0x55331e))
        }
        b.ball(44, 171, 2, R.brass, rgb(0x2a170e)); b.ball(126, 171, 2, R.brass, rgb(0x2a170e))
        b.r(43, 175, 3, 3, rgb(0x2a170e)); b.r(125, 175, 3, 3, rgb(0x2a170e))
    }

    private fun props(b: Buf) {
        // hot plate and kettle
        b.vol(4, 128, 34, 12, { _, _ -> true }, { u, v -> .55 - u * .01 - v * .03 + if (v < 2) .25 else 0.0 }, R.iron, rgb(0x080606))
        b.r(8, 132, 26, 1, rgb(0x0a0808))
        for (i in 0 until 5) b.r(10 + i * 5, 134, 3, 3, rgb(0x3a1a0a))
        b.r(6, 140, 3, 2, rgb(0x100c0c)); b.r(34, 140, 3, 2, rgb(0x100c0c))
        Props.kettle(b, 5, 99)
        Props.cup(b, 44, 133)
        b.r(41, 145, 3, 2, rgb(0xfffbf0)); b.r(54, 145, 3, 2, rgb(0xf8f0da))
        Props.jar(b, 62, 134, R.jam)
        b.line(68, 131, 72, 126, rgb(0xb4b0a8)); b.p(72, 125, rgb(0xd6d2ca)); b.p(73, 125, rgb(0xd6d2ca))
        // the pile of today's letters, its height telling how many
        val pile = letters.coerceIn(0, 4)
        val colors = intArrayOf(rgb(0xf8eed4), rgb(0xdce8f0), rgb(0xf4dcd4), rgb(0xecdcb6), rgb(0xf8eed4), rgb(0xf6dc84))
        if (pile > 0) {
            for (i in 0 until pile) Props.envelope(b, 73 + (i % 2) * 2, 140 - i * 3, 40, 8, colors[i])
            // string tied round the stack, only as tall as the stack
            val top = pileTop()
            b.r(92, top, 2, 148 - top, rgb(0x8a5a2a))
            for (i in 0 until pile) b.r(73 + (i % 2) * 2, 140 - i * 3 + 4, 40, 1, rgb(0x8a5a2a))
        } else {
            Props.envelope(b, 76, 140, 36, 8, rgb(0xecdcb6))
        }
        if (e.has(Look.APPLES) || e.has(Look.HARVEST)) for ((x, y) in listOf(116 to 142, 120 to 140, 118 to 144)) b.ball(x, y, 2, R.apple, rgb(0x2a0808))
        if (e.has(Look.MASLENITSA)) { b.vol(112, 140, 14, 5, ell(7.0, 2.5, 7.0, 2.5), { _, v -> .7 - v * .1 }, R.honey, rgb(0x5a3006)) }
        // postal scale
        b.vol(124, 136, 24, 8, { _, _ -> true }, { u, v -> .7 - v * .06 - u * .008 }, R.wood, rgb(0x1e100a))
        b.r(134, 124, 4, 12, rgb(0x9a6a1c)); b.r(135, 124, 1, 12, rgb(0xe8bf58))
        b.ball(136, 128, 6, R.cream, rgb(0x3e270c))
        b.line(136, 128, 139, 124, rgb(0xa33a2c))
        b.vol(126, 116, 20, 3, { _, _ -> true }, { _, v -> .85 - v * .25 }, R.brass, rgb(0x3e270c))
        b.vol(130, 110, 12, 6, { _, _ -> true }, { u, _ -> .7 - u * .02 }, R.paper, rgb(0x3a2a1a))
        b.line(136, 110, 136, 116, rgb(0x7a4a2a))
        // ink pad and rubber stamp
        b.vol(150, 140, 18, 5, { _, _ -> true }, { _, v -> .6 - v * .1 }, R.coat, rgb(0x06080e))
        b.r(152, 141, 14, 2, rgb(0x141c34))
        b.r(156, 131, 6, 3, rgb(0x1e2a4a)); b.r(158, 126, 2, 5, rgb(0x8e5a34)); b.ball(159, 124, 3, R.wood, rgb(0x1e100a))
    }

    /** The y of the top envelope on the desk (one lies there even when the bag is empty). */
    private fun pileTop() = 140 - (letters.coerceIn(1, 4) - 1) * 3

    /** A wall lamp by the clock, lit at dusk. */
    private fun lamp(b: Buf) {
        b.r(70, 44, 2, 8, rgb(0x2a1a10))
        b.vol(64, 50, 14, 8, { u, v -> kotlin.math.abs(u - 6.5) <= 3 + v * .5 }, { u, _ -> .7 - u * .03 }, R.lampG, rgb(0x08140c))
        b.r(65, 57, 12, 1, rgb(0xfff0b0))
        b.glow(70, 64, 110, rgb(0xffc060), .42f, 7)
        b.glow(70, 60, 30, rgb(0xfff0b0), .3f, 5)
    }

    override fun anim(b: Buf, t: Int) {
        val wait = Art.still
        // pendulum, and the clock cat's eyes swinging with it
        val an = sin(t * .5) * .32
        val ex = 92 + sin(an) * 28
        val ey = 42 + cos(an) * 28
        b.line(92.0, 42.0, ex, ey, rgb(0x9a6a1c))
        b.ball(ex.roundToInt(), ey.roundToInt(), 3, R.brass, rgb(0x3e270c))
        val eo = sin(t * .5).roundToInt()
        b.p(89 + eo, 25, rgb(0x1e100a)); b.p(95 + eo, 25, rgb(0x1e100a))
        for ((x, y) in listOf(86 to 62, 98 to 70)) {
            b.line(x, 42, x, y, rgb(0x8e857a))
            b.vol(x - 2, y, 5, 9, ell(2.5, 4.5, 2.5, 4.5), { u, _ -> .6 - u * .08 }, R.brass, rgb(0x2a170e))
            var j = 1
            while (j < 8) { b.p(x - 1 + if (j % 4 != 0) 1 else 0, y + j, rgb(0x6a4614)); j += 2 }
        }
        // the hot plate glowing
        for (i in 0 until 5) {
            val f = .5 + .5 * sin(t * .9 + i * 1.7)
            b.r(10 + i * 5, 134, 3, 3, if (f > .6) rgb(0xf8c050) else if (f > .25) rgb(0xe07a28) else rgb(0xa03a14))
        }
        b.glow(22, 136, 16, rgb(0xff9a40), (.18 + .06 * sin(t * .7)).toFloat(), 4)
        Props.steam(b, 38, 108, t, 6, 20, .8f)
        Props.steam(b, 50, 130, t + 4, 4, 12, .55f)
        // weather in the window
        Air.clouds(b, wx, wy, ww, 30, t, e, if (e.sky == Sky.CLEAR) 1 else 3) { x, y -> skyShows(x, y) }
        Air.precip(b, e, t, wx, wy, ww, wh, .8, still = wait) { x, y -> outShows(x, y) }
        Air.glassDrops(b, e, t, wx, wy, ww, wh) { x, y -> outShows(x, y) }
        Air.fog(b, e, t, wx, wy + 20, ww, wh - 20, .45f) { x, y -> outShows(x, y) }
        if (e.phase.dark && !e.sky.grey) Air.stars(b, wx, wy, ww, 28, t, 10) { x, y -> skyShows(x, y) && !(x in wx + 36..wx + 44 && y in wy + 10..wy + 18) }
        // dust in the sunbeam
        if (sunny) for (i in 0 until 34) {
            val x = (wx + 10 + (rnd(i) * 120 + t * .18 * (.5 + rnd(i + 9))) % 120).roundToInt()
            val y = (wy + 10 + (rnd(i + 40) * 120 + sin(t * .08 + i) * 4 + t * .05) % 120).roundToInt()
            if (inBeam(x, y) && (t + i) % 9 > 1) b.p(x, y, rgb(0xfff8e0), .75f)
        }
        if (dog) People.dogLying(b, 16, 192, (sin(t * .2) + 1) / 2)
        // the cat asleep on the letters (or on the desk when there are none)
        // the cat lies right on top of the stack: its belly (row 25 of the sprite) on the top envelope
        val catY = pileTop() - 24
        Props.cat(b, 72, catY, (sin(t * .18) + 1) / 2)
        if (dim > .3f) {
            b.glow(70, 64, 18, rgb(0xfff0b0), (.05 + .03 * sin(t * .6)).toFloat(), 3)
        }
    }
}
