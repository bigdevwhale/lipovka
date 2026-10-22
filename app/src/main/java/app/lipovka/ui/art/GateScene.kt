package app.lipovka.ui.art

import app.lipovka.data.Resident
import app.lipovka.domain.Env
import app.lipovka.domain.House
import app.lipovka.domain.Leaves
import app.lipovka.domain.Look
import app.lipovka.domain.Phase
import app.lipovka.domain.Season
import kotlin.math.abs
import kotlin.math.roundToInt
import kotlin.math.sin

/** At the gate: the resident's house up close, the resident with the opened letter, the postman. */
class GateScene(private val e: Env, private val house: House, private val who: Resident?, private val dog: Boolean) : Scene(170, 190) {
    override val key = listOf(e.copy(minute = e.minute / 10), house.id, who?.id, dog)

    private val winter = e.snow
    private val lit = e.phase.lamps
    private val town = house.id == "museum" || house.id == "newspaper"
    private val planks = house.id in setOf("halt", "stationhouse", "meteo", "painter")
    private val hx = 66
    private val hy = 78
    private val hw = 94
    private val hh = 72

    private fun roof() = when (house.roof) {
        'R' -> R.roofR
        'B' -> R.roofB
        'G' -> R.roofG
        'T' -> R.thatch
        'S' -> R.roofS
        else -> R.roofW
    }

    private fun frame() = when (house.frame) {
        'B' -> rgb(0x7aa0d8) to rgb(0xe8e2d4)
        'G' -> rgb(0x8ac08a) to rgb(0x2a5a3a)
        'Y' -> rgb(0xf0d070) to rgb(0x405890)
        else -> rgb(0xe8e2d4) to rgb(0x405890)
    }

    override fun base(b: Buf) {
        sky(b)
        hills(b)
        if (town) townHouse(b) else izba(b)
        ground(b)
        if (!town) fence(b) else street(b)
        props(b)
        Air.grade(b, e)
        if (lit) lights(b)
        b.vignette(if (e.phase.dark) rgb(0x14182a) else rgb(0x2a1a3a), .55f)
    }

    private fun sky(b: Buf) {
        b.vgrad(0, 0, 170, 124, Air.skyRamp(e))
        if (e.phase.dark && !e.sky.grey) Air.moon(b, 30, 24, 6, e.date, rgb(0x151d34))
        if (!e.phase.dark && !e.sky.grey) {
            val sx = 20 + ((e.minute - 360).coerceIn(0, 720) / 720.0 * 130).roundToInt()
            val sy = 40 - (sin((e.minute - 360) / 720.0 * Math.PI) * 26).roundToInt()
            if (e.phase == Phase.DUSK || e.phase == Phase.DAWN) { b.glow(sx, 70, 30, rgb(0xffd8a0), .45f, 6); b.disc(sx, 72, 6, rgb(0xfff0c8)) }
            else { b.glow(sx, sy, 22, rgb(0xfff6d0), .45f, 5); b.disc(sx, sy, 5, rgb(0xfffbe8)) }
        }
    }

    private fun hills(b: Buf) {
        val far = if (winter) rgb(0x8a94ac) else when (e.season) {
            Season.SUMMER -> rgb(0x4a6a54)
            Season.SPRING -> rgb(0x5a7a5a)
            else -> rgb(0x5a5a6a)
        }
        for (x in 0 until 170) {
            val h = 96 + (fbm(x * .08, 2.0) * 10).roundToInt()
            for (y in h until 124) b.p(x, y, far)
            if (hash(x, 3) > .6) { val th = (hash(x, 9) * 6).toInt() + 3; for (j in 0 until th) b.p(x, h - j, far) }
        }
        for ((x, y) in listOf(14 to 108, 30 to 110, 148 to 106)) {
            val c = far.dim(.25f)
            b.r(x, y, 8, 6, c)
            for (j in 0 until 4) b.r(x + 2 - j, y - j, 4 + j * 2, 1, c)
            if (lit) { b.p(x + 2, y + 2, rgb(0xf6d77a)); b.p(x + 5, y + 2, rgb(0xf6d77a)) }
        }
        val g = when {
            winter -> R.snow
            e.season == Season.SUMMER -> R.grassSummer
            e.season == Season.SPRING -> R.grassSpring
            else -> R.grass
        }
        for (x in 0 until 170) {
            val h = 116 + (sin(x * .05) * 3).roundToInt()
            for (y in h until 190) b.p(x, y, rp(g, .25 + (y - h) / 90.0 + fbm(x * .1, y * .1) * .3, x, y))
        }
    }

    private fun izba(b: Buf) {
        // walls: logs, or painted planks for the halt and the station houses
        for (y in hy until hy + hh) for (x in hx until hx + hw) {
            if (planks) {
                val k = (x - hx) % 6
                val base = if (house.id == "halt") rgb(0xc8b070) else if (house.id == "meteo") rgb(0x9ab0a0) else rgb(0x8aa0c0)
                b.p(x, y, if (k == 0) base.dim(.45f) else base.dim(((x - hx) / hw.toFloat()) * .2f + (fbm(x * .2, y * .3) * .1).toFloat()))
            } else {
                val k = (y - hy) % 5
                val l = when (k) { 0 -> .78; 1 -> .66; 2 -> .55; 3 -> .44; else -> .22 }
                b.p(x, y, rp(R.wood, l + (fbm(x * .15, y * .6) - .5) * .18 - (x - hx) / hw.toDouble() * .12, x, y))
            }
        }
        if (!planks) {
            var y = hy
            while (y < hy + hh) {
                for (x in listOf(hx - 3, hx + hw - 1)) {
                    b.vol(x, y, 4, 5, ell(2.0, 2.5, 2.0, 2.5), sph(1.5, 2.0, 2.0, 2.5, .3), R.wood, rgb(0x1e100a))
                    b.p(x + 2, y + 2, rgb(0x55331e))
                }
                y += 5
            }
        }
        // roof with a carved bargeboard
        val ax = hx + hw / 2
        val ay = 26
        val roof = roof()
        for (y in ay until hy + 2) {
            val half = ((y - ay) * 1.05).roundToInt() + 2
            for (x in ax - half until ax + half) {
                var l = if (x < ax) .62 else .36
                l += (if ((y - ay) % 4 == 0) -.14 else 0.0) + (if ((x + (y - ay) / 4 * 2) % 6 == 0) -.08 else 0.0)
                b.p(x, y, if (winter && hash(x, y) > .1 && (y - ay) % 4 != 0) rp(R.snow, l + .2, x, y) else rp(roof, l, x, y))
            }
            b.p(ax - half - 1, y, R.INK); b.p(ax + half, y, R.INK)
        }
        if (winter) for (x in ax - 50 until ax + 50) { val y = hy + 2; if (hash(x, 1) > .3) b.p(x, y, R.snow[5]) }
        val (fr, acc) = frame()
        for (y in ay + 4 until hy + 2) {
            val half = ((y - ay) * 1.05).roundToInt() + 2
            b.p(ax - half + 1, y, fr); b.p(ax + half - 2, y, fr.dim(.15f))
            if (y % 3 == 0) { b.p(ax - half + 2, y + 1, fr); b.p(ax + half - 3, y + 1, fr.dim(.15f)) }
        }
        for (y in ay + 10 until hy) {
            val half = ((y - ay - 10) * 1.05).roundToInt()
            for (x in ax - half until ax + half) b.p(x, y, if (planks) rgb(0x8a7a62) else rp(R.wood, .5 + (if (x < ax) .12 else 0.0) + (if ((x - ax + 50) % 4 == 0) -.15 else 0.0), x, y))
        }
        b.ball(ax, 62, 4, R.wood, rgb(0x1e100a))
        b.disc(ax, 62, 3, if (lit) rgb(0xf6d77a) else rgb(0x8aa0b0))
        b.r(ax, 59, 1, 7, rgb(0x3a2214)); b.r(ax - 3, 62, 7, 1, rgb(0x3a2214))
        if (!planks) b.spr(listOf("..kk....", ".kWWk...", "kWkWWk..", "...kWWk.", "....kWWk", "....kWWk"), ax - 4, ay - 6, mapOf('k' to R.INK, 'W' to fr))
        if (house.id != "meteo") {
            b.vol(ax + 20, 34, 8, 26, { _, _ -> true }, { u, v -> .6 - u * .05 + if (v % 3 == 0) -.15 else 0.0 }, R.brick, rgb(0x1a0806))
            b.r(ax + 19, 33, 10, 2, rgb(0x2a0e0a))
            if (winter) b.r(ax + 19, 32, 10, 1, R.snow[5])
        }
        window(b, hx + 12, hy + 20, fr, acc)
        window(b, hx + 60, hy + 20, fr, acc)
        for (x in hx - 3 until hx + hw + 1 step 6) b.vol(x, hy + hh, 6, 5, { _, _ -> true }, { u, v -> .6 - u * .06 - v * .05 }, R.stone, rgb(0x1a1614))
        when (house.id) {
            "halt" -> { b.r(hx + 30, hy + 4, 34, 9, rgb(0xfbf3dc)); b.r(hx + 32, hy + 7, 30, 1, rgb(0x26375e)); b.r(hx + 32, hy + 9, 22, 1, rgb(0x26375e)) }
            "shop" -> { b.r(hx + 28, hy + 4, 38, 9, rgb(0x2a4a2a)); b.r(hx + 30, hy + 7, 34, 1, rgb(0xf2ece0)); b.r(hx + 30, hy + 9, 26, 1, rgb(0xf2ece0)) }
            "club" -> { b.r(hx + 30, hy + 4, 34, 9, rgb(0x842a24)); b.r(hx + 32, hy + 7, 30, 1, rgb(0xf8d070)); b.r(hx + 32, hy + 9, 18, 1, rgb(0xf8d070)) }
        }
    }

    private fun window(b: Buf, x: Int, y: Int, fr: Int, acc: Int) {
        if (lit) b.glow(x + 10, y + 14, 34, rgb(0xffc860), .32f, 5)
        b.r(x - 3, y - 8, 26, 8, fr)
        for (i in 0 until 26 step 3) { b.p(x - 3 + i, y - 9, fr); b.p(x - 2 + i, y - 10, fr) }
        b.r(x + 6, y - 12, 8, 4, fr); b.r(x, y - 6, 20, 2, acc); b.p(x + 10, y - 11, acc)
        b.r(x - 3, y, 3, 28, fr); b.r(x + 20, y, 3, 28, fr)
        for (j in 2 until 28 step 4) { b.p(x - 2, y + j, acc); b.p(x + 21, y + j, acc) }
        b.r(x - 5, y + 28, 30, 3, fr); b.r(x - 3, y + 31, 26, 2, fr.dim(.18f))
        if (winter) b.r(x - 5, y + 27, 30, 1, R.snow[5])
        if (lit) b.vgrad(x, y, 20, 28, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040), rgb(0xd08c24)))
        else {
            b.vgrad(x, y, 20, 28, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
            for (j in 0 until 28) b.mul(x + 9 - (j % 3), y + j, rgb(0x404860), .3f)
        }
        for (j in 0 until 20) {
            val w1 = (6 - j / 4).coerceAtLeast(0)
            for (i in 0 until w1) {
                val c = if ((i + j) % 2 == 0) rgb(0xfbf6ea) else rgb(0xe8dcc4)
                b.p(x + i, y + j, c); b.p(x + 19 - i, y + j, c)
            }
        }
        b.r(x + 9, y, 2, 28, rgb(0x55331e)); b.r(x, y + 12, 20, 2, rgb(0x55331e))
        // pot plants on the sill inside
        b.vol(x + 2, y + 22, 6, 6, { u, v -> v > 2 || abs(u - 3) < 2 }, { _, _ -> .5 }, R.brick)
        for (k in 0 until 8) b.p(x + 2 + (hash(k, x) * 6).toInt(), y + 17 + (hash(x, k) * 5).toInt(), if (k % 3 == 0) rgb(0xc01e2a) else rgb(0x2a4a2a))
        b.vol(x + 13, y + 23, 5, 5, { _, _ -> true }, { _, _ -> .5 }, R.brick)
        for (k in 0 until 6) b.p(x + 13 + (hash(k, y) * 5).toInt(), y + 19 + (hash(y, k) * 4).toInt(), if (k % 2 == 0) rgb(0x3a5a32) else rgb(0xe8d8f0))
        if (e.has(Look.NEWYEAR)) for (k in 0 until 5) b.p(x + 2 + k * 4, y + 2 + (k % 2), intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[k % 3])
    }

    private fun townHouse(b: Buf) {
        val museum = house.id == "museum"
        for (y in hy - 30 until hy + hh) for (x in hx - 6 until hx + hw + 6) {
            b.p(x, y, if (museum) rp(intArrayOf(rgb(0xb8a888), rgb(0xd8c8a4), rgb(0xece0c4)), .6 - (x - hx) / 300.0 + fbm(x * .1, y * .1) * .2, x, y)
            else rp(R.brick, .55 + (if ((y - hy) % 4 == 0) -.25 else 0.0) + (if (((x - hx) + ((y - hy) / 4) * 4) % 8 == 0) -.2 else 0.0), x, y))
        }
        b.vgrad(hx - 8, hy - 36, hw + 16, 6, if (museum) R.roofG.copyOfRange(2, 6) else R.roofS.copyOfRange(1, 5))
        if (winter) b.r(hx - 8, hy - 37, hw + 16, 2, R.snow[5])
        if (museum) for (i in 0 until 5) b.vol(hx + 4 + i * 20, hy - 26, 6, 96, { _, _ -> true }, { u, _ -> .9 - u * .12 }, R.cream, rgb(0x6a5a42))
        for (r in 0 until 2) for (i in 0 until 4) {
            val x = hx + 2 + i * 24
            val y = hy - 20 + r * 40
            if (museum && (i == 1 || i == 2) && r == 1) continue
            b.r(x - 1, y - 1, 16, 22, rgb(0xe8e2d4))
            if (lit) b.vgrad(x, y, 14, 20, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040))) else b.vgrad(x, y, 14, 20, intArrayOf(rgb(0x5c7480), rgb(0x8aa0a8)))
            b.r(x + 6, y, 2, 20, rgb(0xe8e2d4)); b.r(x, y + 8, 14, 2, rgb(0xe8e2d4))
            if (lit) b.glow(x + 7, y + 10, 18, rgb(0xffc860), .2f, 4)
        }
        b.r(hx + 38, hy + 34, 18, 38, rgb(0x3a2214)); b.r(hx + 46, hy + 34, 2, 38, rgb(0x22130b)); b.ball(hx + 44, hy + 54, 1, R.brass)
        b.r(hx + 30, hy + 22, 34, 9, rgb(0xfbf3dc)); b.r(hx + 32, hy + 25, 30, 1, rgb(0x26375e)); b.r(hx + 32, hy + 27, 20, 1, rgb(0x26375e))
    }

    private fun ground(b: Buf) {
        val dirt = if (winter) intArrayOf(rgb(0xb4bccc), rgb(0xc8d0dc), rgb(0xdce2ea)) else intArrayOf(rgb(0x4a3a2a), rgb(0x5e4a34), rgb(0x6e5a40))
        for (y in 150 until 190) {
            val half = 10 + (y - 150) * .55
            for (x in (82 - half).roundToInt() until (82 + half).roundToInt()) b.p(x, y, rp(dirt, fbm(x * .2, y * .2) + .2, x, y))
        }
        if (e.sky.rain || (e.season == Season.AUTUMN && !winter) || e.season == Season.SPRING) {
            for ((x, y, rx, ry) in listOf(listOf(70, 178, 9, 2), listOf(96, 184, 7, 2))) for (j in -ry..ry) for (i in -rx..rx) {
                if ((i / rx.toDouble()).let { it * it } + (j / ry.toDouble()).let { it * it } > 1) continue
                b.p(x + i, y + j, if (j < 0) Air.skyRamp(e).last() else Air.skyRamp(e).first())
            }
            if (lit) { b.r(68, 177, 3, 1, rgb(0xf8d070)); b.r(95, 183, 2, 1, rgb(0xf8d070)) }
        }
    }

    private fun fence(b: Buf) {
        Props.fence(b, 0, 64, 136, 30, winter)
        Props.fence(b, 102, 170, 136, 30, winter)
        for (i in 0 until 4) for (y in 138 + i until 164 - i) for (k in 0 until 3) b.p(65 + i * 3 + k, y, rp(R.woodG, .5 - k * .12, 65 + i * 3, y))
        if (!winter) for ((x, y, r) in listOf(Triple(6, 128, R.glass), Triple(24, 128, R.glass), Triple(114, 128, R.glass), Triple(138, 129, R.brick))) {
            b.vol(x, y, 8, 9, { u, v -> !(v < 2 && (u < 2 || u > 5)) }, { u, _ -> .5 - u * .06 + if (u == 2) .35 else 0.0 }, r, R.INK)
        }
    }

    private fun street(b: Buf) {
        for (y in 150 until 160) for (x in 0 until 170) b.p(x, y, rp(R.stone, .5 + (if (x % 8 == 0) -.2 else 0.0), x, y))
        b.line(150, 108, 150, 160, rgb(0x2a2a30)); b.r(146, 104, 9, 5, rgb(0x2a2a30)); b.r(147, 105, 7, 3, if (lit) rgb(0xfff0b0) else rgb(0x8a8a90))
        if (lit) b.glow(150, 108, 34, rgb(0xfff0b0), .3f, 5)
    }

    private fun props(b: Buf) {
        val ps = house.props
        // the tree on the left: a rowan, or a birch
        if ("rowan" in ps || (!town && house.id.hashCode() % 2 == 0)) rowan(b) else if (!town) Props.birch(b, 18, 66, 70, e.leaves, alt = true)
        if ("well" in ps) {
            b.vol(4, 140, 18, 14, { _, _ -> true }, { u, v -> .6 - u * .02 - (if (v % 4 == 0) .2 else 0.0) }, R.woodG, R.INK)
            b.line(12, 100, 12, 140, rgb(0x3a2214)); b.line(-4, 96, 40, 120, rgb(0x55331e)); b.line(40, 120, 40, 132, rgb(0x8e857a)); b.r(38, 132, 5, 5, rgb(0x706860))
        }
        if ("hives" in ps) for (k in 0 until 3) {
            val x = 4 + k * 18
            b.vol(x, 144, 14, 14, { _, _ -> true }, { u, v -> .7 - u * .03 - if (v % 4 == 0) .15 else 0.0 }, R.honey, rgb(0x3a1a04))
            b.r(x - 2, 141, 18, 3, if (winter) R.snow[5] else rgb(0x8e3a24))
        }
        if ("antenna" in ps) { b.line(140, 0, 140, 60, rgb(0x55504c)); for (k in 0 until 4) b.line(130 + k, 6 + k * 8, 150 - k, 6 + k * 8, rgb(0x55504c)) }
        if ("telescope" in ps) { b.line(14, 160, 20, 140, rgb(0x2a2a30)); b.line(26, 160, 20, 140, rgb(0x2a2a30)); b.vol(8, 128, 24, 6, { u, v -> abs(v - 3 + (u - 12) * .3) < 2.5 }, { u, _ -> .7 - u * .02 }, R.brass, R.INK) }
        if ("goat" in ps && !winter) goat(b, 22, 166)
        if ("boat" in ps) b.vol(2, 156, 40, 10, { u, v -> u > v * 1.2 && u < 40 - v * 1.2 }, { u, v -> .6 - v * .06 - u * .004 }, R.red, R.INK)
        if ("nets" in ps) for (x in 104 until 160 step 3) for (y in 120 until 136 step 3) b.p(x, y, rgb(0x6a6a5a))
        if ("easel" in ps) { b.line(12, 170, 22, 128, rgb(0x7c4e30)); b.line(36, 170, 22, 128, rgb(0x7c4e30)); b.r(10, 130, 24, 18, rgb(0xfbf3dc)); b.vgrad(12, 132, 20, 8, R.dusk.copyOfRange(3, 8)); b.r(12, 140, 20, 6, rgb(0x4e7886)) }
        if ("owl" in ps) b.vol(150, 116, 9, 12, ell(4.5, 6.0, 4.5, 6.0), sph(3.0, 4.0, 5.0, 6.0, .3), intArrayOf(rgb(0x4a3020), rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52)), R.INK)
        if ("owl" in ps) { b.p(152, 120, rgb(0xf8d070)); b.p(156, 120, rgb(0xf8d070)) }
        if ("woodpile" in ps) for (j in 0 until 4) for (i in 0 until 6 - j % 2) { val x = 114 + i * 6 + (j % 2) * 3; val y = 158 - j * 6; b.disc(x, y, 3, rgb(0xc88e58)); b.disc(x, y, 1, rgb(0x8e5a34)) }
        if ("station" in ps) { b.line(30, 70, 30, 166, rgb(0x2a2a30)); b.r(26, 66, 9, 5, rgb(0xd83a2a)); b.r(26, 66, 9, 1, rgb(0xfbf3dc)) }
        if ("lantern" in ps || "meteo" in ps) { b.line(150, 110, 150, 166, rgb(0x2a2a30)); b.r(146, 104, 9, 7, rgb(0x2a2a30)); b.r(147, 105, 7, 5, if (lit) rgb(0xffd060) else rgb(0x8a8a90)) }
        if ("meteo" in ps) { b.r(8, 128, 22, 18, rgb(0xf2ece0)); for (y in 130 until 146 step 3) b.r(9, y, 20, 1, rgb(0xc8c0b0)); b.line(12, 146, 12, 166, rgb(0xf2ece0)); b.line(26, 146, 26, 166, rgb(0xf2ece0)) }
        if ("cheese" in ps) for (k in 0 until 3) b.vol(118 + k * 12, 156, 10, 6, ell(5.0, 3.0, 5.0, 3.0), sph(4.0, 2.0, 5.0, 3.0, .3), R.honey, rgb(0x5a3006))
        if ("carvings" in ps) for (k in 0 until 3) { val x = 116 + k * 14; b.r(x, 120, 10, 14, rgb(0xc88e58)); b.r(x + 2, 122, 6, 10, rgb(0x8e5a34)); b.p(x + 4, 124, rgb(0xf8d070)) }
        if ("swing" in ps) { b.line(130, 100, 130, 166, rgb(0x55331e)); b.line(160, 100, 160, 166, rgb(0x55331e)); b.line(128, 100, 162, 100, rgb(0x55331e)); b.line(140, 100, 140, 150, rgb(0x8e857a)); b.line(150, 100, 150, 150, rgb(0x8e857a)); b.r(138, 150, 14, 2, rgb(0x8e5a34)) }
        if ("books" in ps) for (k in 0 until 4) b.r(118 + k * 4, 156, 3, 8, intArrayOf(rgb(0x842a24), rgb(0x304474), rgb(0x426442), rgb(0xc8952e))[k])
        if ("garden" in ps && !winter) for (k in 0 until 6) { val x = 112 + k * 8; b.disc(x, 170, 3, rgb(0x5c7e50)); b.disc(x, 169, 2, rgb(0x8ab478)) }
        if ("tractor" in ps) { b.vol(120, 150, 34, 14, { _, _ -> true }, { u, _ -> .6 - u * .01 }, R.blue, R.INK); b.ball(126, 166, 5, R.iron, R.INK); b.ball(148, 164, 7, R.iron, R.INK); b.r(140, 138, 10, 12, rgb(0x2c3c64)); b.r(141, 139, 8, 6, rgb(0x8aa0b0)) }
        if ("columns" in ps || "town" in ps) Unit
        if (e.has(Look.NEWYEAR) && !town) for (x in hx until hx + hw step 6) b.p(x, hy + 2 + (x / 6) % 2, intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[(x / 6) % 3])
    }

    private fun goat(b: Buf, x: Int, feet: Int) {
        b.vol(x, feet - 12, 16, 9, ell(8.0, 4.5, 8.0, 4.5), sph(6.0, 3.0, 8.0, 5.0, .4), R.cream, R.INK)
        b.vol(x + 12, feet - 18, 7, 7, ell(3.5, 3.5, 3.5, 3.5), sph(2.5, 2.5, 3.5, 3.5, .4), R.cream, R.INK)
        b.p(x + 14, feet - 21, rgb(0x6e6862)); b.p(x + 16, feet - 21, rgb(0x6e6862)); b.p(x + 16, feet - 16, R.INK); b.p(x + 15, feet - 12, rgb(0xe8e2d4))
        for (i in listOf(2, 5, 10, 13)) b.r(x + i, feet - 4, 1, 4, rgb(0x6e6862))
    }

    private fun rowan(b: Buf) {
        b.r(18, 92, 4, 64, rgb(0x2a1a10))
        b.line(20, 110, 6, 96, rgb(0x2a1a10)); b.line(20, 104, 36, 88, rgb(0x2a1a10)); b.line(21, 100, 30, 80, rgb(0x2a1a10))
        val ramp = when (e.leaves) {
            Leaves.BARE -> null
            Leaves.BUDS -> R.grassSpring
            Leaves.BLOSSOM -> R.blossom
            Leaves.GREEN -> R.green
            Leaves.GOLD -> intArrayOf(rgb(0x1e2a1a), rgb(0x3a3a1e), rgb(0x6a4a1a), rgb(0x9a5a1e), rgb(0xc4782a))
            Leaves.FALLING -> intArrayOf(rgb(0x3a1a10), rgb(0x6a2a1a), rgb(0x9a3a1e), rgb(0xc45a2a))
        }
        if (ramp != null) for (k in 0 until if (e.leaves == Leaves.FALLING) 220 else 420) {
            val a = hash(k, 1) * 6.28
            val d = kotlin.math.sqrt(hash(k, 2)) * 24
            val x = (20 + kotlin.math.cos(a) * d * 1.2).roundToInt()
            val y = (84 + sin(a) * d * .85).roundToInt()
            b.p(x, y, rp(ramp, .2 + hash(k, 3) * .6 - (y - 60) / 80.0, x, y))
        }
        if (e.month in listOf(8, 9, 10, 11, 12, 1)) for (k in 0 until 16) {
            val x = 4 + (hash(k, 5) * 34).toInt()
            val y = 70 + (hash(k, 6) * 26).toInt()
            for ((i, j) in listOf(0 to 0, 1 to 0, 0 to 1, 1 to 1, 2 to 1, 1 to 2)) b.p(x + i, y + j, if ((i + j) % 2 == 0) rgb(0xc01e1e) else rgb(0xe83a2a))
            if (winter) b.p(x + 1, y - 1, R.snow[5])
        }
    }

    private fun lights(b: Buf) {
        b.glow(hx + 22, hy + hh + 14, 26, rgb(0xffc860), .22f, 4)
        b.glow(hx + 70, hy + hh + 14, 26, rgb(0xffc860), .22f, 4)
    }

    override fun anim(b: Buf, t: Int) {
        if (e.phase.dark && !e.sky.grey) Air.stars(b, 0, 0, 170, 60, t, 14) { x, y -> !(x in 22..38 && y in 16..32) }
        Air.clouds(b, 0, 0, 170, 70, t, e, if (e.sky.grey) 5 else 2)
        if (!town && house.id != "meteo") Props.smoke(b, hx + hw / 2 + 24, 32, t, 9, 34, if (e.phase.dark) rgb(0x6a6a80) else rgb(0xb8a8b8), .5f, if (e.temp < -10) .05 else .5)
        if ("cat" in house.props) {
            val y = Art.still || (t / 14) % 6 != 0
            b.spr(listOf(".k...k...", "kgk.kgk..", "kgggggk..", "kgygyggk.", "kgggpggk.", ".kgwwgk..", ".kggggk..", "kgggwggk.", "kgggwgggk", "kggggggk."),
                124, 131, mapOf('k' to R.INK, 'g' to rgb(0x55504c), 'y' to if (y) rgb(0xe8c040) else rgb(0x3e3a38), 'p' to rgb(0xd08080), 'w' to rgb(0x8a837a)))
        }
        val r = who
        if (r != null) People.draw(b, r.sprite, r.look, 82, 178, winter)
        People.postman(b, 128, 178, winter)
        if (dog) People.dogSit(b, 110, 178, if (Art.still) 0 else t / 2)
        if (e.leaves == Leaves.FALLING || e.leaves == Leaves.GOLD) for (i in 0 until 7) {
            val ph = (t * .4 + i * 30) % 110
            val x = (10 + rnd(i) * 40 + sin(t * .12 + i) * 6 + ph * .3).roundToInt()
            val y = (80 + ph).roundToInt()
            b.p(x, y, if (i % 2 == 0) rgb(0xd8782a) else rgb(0xa8381e)); b.p(x + 1, y, if (i % 2 == 0) rgb(0xe8a040) else rgb(0xc04a2a))
        }
        if (lit) b.glow(88, 112, 10, rgb(0xfff0a0), (.05 + .04 * sin(t * .6)).toFloat(), 3)
        Air.precip(b, e, t, 0, 0, 170, 190, 1.0, still = Art.still)
        Air.fog(b, e, t, 0, 60, 170, 130, .4f)
    }
}
