package app.lipovka.ui.art

import app.lipovka.domain.Env
import app.lipovka.domain.House
import app.lipovka.domain.Leaves
import app.lipovka.domain.Look
import app.lipovka.domain.Pt
import app.lipovka.domain.Season
import app.lipovka.domain.Sky
import app.lipovka.domain.World
import kotlin.math.PI
import kotlin.math.abs
import kotlin.math.cos
import kotlin.math.hypot
import kotlin.math.roundToInt
import kotlin.math.sin

/** What the map shows of the round. */
data class MapRound(
    /** The path still to walk to the next stop, from the postman's spot. */
    val ahead: List<Pt> = emptyList(),
    /** The rest of the round after the next stop, house by house. */
    val later: List<Pt> = emptyList(),
    val postman: Pt = World.POST,
    /** Houses with letters waiting in the bag. */
    val pending: Set<String> = emptySet(),
    /** Houses already visited today. */
    val visited: Set<String> = emptySet(),
    val walking: Boolean = false,
)

/** The whole countryside, from the post office at the bottom to the district town at the top. */
class MapScene(private val e: Env, private val open: Int, private val round: MapRound, private val dog: Boolean) : Scene(World.W, World.H) {
    override val key = listOf(e.copy(minute = e.minute / 10), open, round, dog)

    private val winter = e.snow
    private val river = listOf(
        doubleArrayOf(180.0, 326.0, 140.0, 332.0, 122.0, 350.0, 104.0, 360.0),
        doubleArrayOf(104.0, 360.0, 80.0, 372.0, 40.0, 366.0, -10.0, 384.0),
    )
    private val riverPts: List<Pair<Double, Double>> = river.flatMap { s -> (0..250).map { bez(s, it / 250.0) } }
    private val lake = Pt(38.0, 138.0)
    private val dist: FloatArray = FloatArray(World.W * World.H)

    init {
        // distance to the river for every pixel near it
        dist.fill(99f)
        for ((px, py) in riverPts.filterIndexed { i, _ -> i % 2 == 0 }) {
            val x0 = px.roundToInt()
            val y0 = py.roundToInt()
            for (j in -12..12) for (i in -12..12) {
                val x = x0 + i
                val y = y0 + j
                if (x < 0 || y < 0 || x >= w || y >= h) continue
                val d = hypot(px - x, py - y).toFloat()
                val k = y * w + x
                if (d < dist[k]) dist[k] = d
            }
        }
    }

    private fun riverD(x: Int, y: Int) = if (x < 0 || y < 0 || x >= w || y >= h) 99f else dist[y * w + x]
    private fun inLake(x: Int, y: Int) = ((x - lake.x) / 34).let { it * it } + ((y - lake.y) / 40).let { it * it } <= 1 - fbm(x * .1, y * .1) * .25

    private fun ground(): IntArray = when {
        winter -> R.snow
        e.season == Season.SUMMER -> R.grassSummer
        e.season == Season.SPRING -> R.grassSpring
        else -> R.grass
    }

    override fun base(b: Buf) {
        land(b)
        water(b)
        rail(b)
        roads(b)
        woods(b)
        for (hs in World.houses) if (hs.district <= open) building(b, hs)
        post(b)
        village(b)
        events(b)
        Air.grade(b, e)
        lights(b)
        locked(b)
    }

    private fun land(b: Buf) {
        val g = ground()
        for (y in 0 until h) for (x in 0 until w) {
            val n = fbm(x * .06, y * .06)
            var c = rp(g, .25 + n * .6, x, y)
            if (!winter) {
                val n2 = vn(x * .04 + 50, y * .04)
                if (n2 > .66 && hash(x, y) > .3) c = rp(if (e.season == Season.AUTUMN) intArrayOf(rgb(0x8a7a3a), rgb(0xa08a44), rgb(0xb49a50)) else intArrayOf(rgb(0x6a8a3a), rgb(0x7a9a44)), n, x, y)
            }
            b.p(x, y, c)
        }
        for (i in 0 until 600) {
            val x = (rnd(i) * w).toInt()
            val y = (rnd(i + 3000) * h).toInt()
            if (winter) { b.p(x, y, rgb(0xd0d8e4)); continue }
            b.p(x, y, g[0]); b.p(x + 1, y - 1, g[4])
            if (e.season == Season.SUMMER && i % 7 == 0) b.p(x, y - 1, if (i % 2 == 0) rgb(0xf0e070) else rgb(0xe8e8f0))
        }
        // fields north of the village and by the halt
        field(b, 120, 400, 46, 30)
        field(b, 4, 560, 30, 40)
        field(b, 150, 236, 20, 40)
        field(b, 4, 196, 40, 18)
    }

    private fun field(b: Buf, x0: Int, y0: Int, fw: Int, fh: Int) {
        for (y in y0 until y0 + fh) for (x in x0 until x0 + fw) {
            if (x >= w) continue
            val s = ((x + y * .5) / 3).toInt() % 2 == 0
            b.p(x, y, when {
                winter -> if (s) rgb(0xe8eef4) else rgb(0xccd4e0)
                e.season == Season.SPRING -> if (s) rgb(0x6a4a26) else rgb(0x55391c)
                e.season == Season.SUMMER -> if (s) rgb(0xc8a848) else rgb(0xb49438)
                else -> if (s) rgb(0x8a7040) else rgb(0x6a5430)
            })
        }
        if (e.has(Look.HAYMAKING) || (e.season == Season.AUTUMN && !winter) || e.has(Look.HARVEST)) {
            for (k in 0 until 3) {
                val x = x0 + 6 + (hash(x0, k) * (fw - 12)).toInt()
                val y = y0 + 6 + (hash(k, y0) * (fh - 12)).toInt()
                b.vol(x - 5, y - 5, 10, 8, { u, v -> v < 8 && ((u - 5) / 5.0).let { it * it } + ((v - 7) / 7.0).let { it * it } <= 1 }, sph(4.0, 3.0, 6.0, 6.0, .25), R.thatch, rgb(0x2a1a08))
            }
        }
    }

    private fun water(b: Buf) {
        val iced = e.ice && !e.has(Look.ICEBREAK)
        for (y in 300 until 400) for (x in 0 until w) {
            val d = riverD(x, y)
            if (d < 7.5) {
                b.p(x, y, if (iced) rp(R.ice, .45 + (1 - d / 7.5) * .3 + (fbm(x * .2, y * .2) - .5) * .3, x, y)
                else rp(R.water, .22 + (1 - d / 7.5) * .35 + (fbm(x * .15, y * .15) - .5) * .2, x, y))
            } else if (d < 9.5) {
                b.p(x, y, if (winter) rp(R.snow, .4, x, y) else rp(intArrayOf(rgb(0x4a3e28), rgb(0x6a5a3a), rgb(0x8a7650)), (d - 7.5) / 2.0, x, y))
            }
        }
        // reeds
        if (!winter) for ((k, pt) in riverPts.withIndex()) {
            if (k % 11 != 0 || hash(k, 4) < .5) continue
            val side = if ((k / 11) % 2 == 0) 1 else -1
            val x = (pt.first + side * 9).roundToInt()
            val y = (pt.second + side * 3).roundToInt()
            for (r in 0 until 3) { b.line(x + r, y, x + r + (r - 1), y - 4 - r, rgb(0x4a5a24)); b.p(x + r + (r - 1), y - 5 - r, rgb(0x6a3a1a)) }
        }
        if (e.has(Look.ICEBREAK)) for (k in 0 until 18) {
            val pt = riverPts[(k * 29) % riverPts.size]
            b.r(pt.first.roundToInt() - 2, pt.second.roundToInt() - 1, 4 + k % 3, 2, rgb(0xe2eef2))
        }
        // the lake at Ozyorki
        if (open >= 3 || true) for (y in 90 until 190) for (x in 0 until 80) {
            if (!inLake(x, y)) {
                if (inLake(x + 2, y) || inLake(x - 2, y) || inLake(x, y + 2) || inLake(x, y - 2)) b.p(x, y, if (winter) rgb(0xc8d2de) else rgb(0x8a7650))
                continue
            }
            val dd = hypot((x - lake.x) / 34, (y - lake.y) / 40)
            b.p(x, y, if (e.ice) rp(R.ice, .5 + dd * .3 + (fbm(x * .2, y * .2) - .5) * .3, x, y) else rp(R.water, .2 + (1 - dd) * .45 + (fbm(x * .12, y * .12) - .5) * .2, x, y))
        }
    }

    private fun rail(b: Buf) {
        val y0 = 212
        for (x in 0 until w) {
            for (j in -2..2) b.p(x, y0 + j, rgb(0x6a5e52))
            if (x % 3 == 0) b.r(x, y0 - 2, 1, 5, rgb(0x3a2a1e))
            b.p(x, y0 - 1, rgb(0x9a9aa2)); b.p(x, y0 + 1, rgb(0x9a9aa2))
        }
    }

    private fun road(b: Buf, a: Pt, c: Pt, e2: Pt, wd: Int = 2) {
        var t = 0.0
        while (t <= 1.0) {
            val (px, py) = quad(a.x, a.y, c.x, c.y, e2.x, e2.y, t)
            for (j in -wd..wd) for (i in -wd..wd) {
                if (i * i + j * j > wd * wd + 1) continue
                val x = (px + i).roundToInt()
                val y = (py + j).roundToInt()
                if (riverD(x, y) < 7.5) continue
                val edge = i * i + j * j >= wd * wd
                b.p(x, y, when {
                    winter -> if (edge) rgb(0xb4bccc) else rp(intArrayOf(rgb(0xc4ccd8), rgb(0xd8dee8), rgb(0xe4e8f0)), fbm(x * .3, y * .3), x, y)
                    edge -> rgb(0x7a5e3a)
                    else -> rp(intArrayOf(rgb(0x8e6e44), rgb(0xa8845a), rgb(0xb8966a)), .5 + fbm(x * .3, y * .3) * .5, x, y)
                })
            }
            t += .004
        }
    }

    /** The main street's x at a given y: it wanders a little on its way to the bridge. */
    private fun street(y: Double) = 100 + sin(y * .021) * 5

    /** A lane from the nearest point of a road line to a house. */
    private fun lane(b: Buf, from: Pt, to: Pt, wd: Int = 1) {
        val c = Pt((from.x + to.x) / 2, from.y + (to.y - from.y) * .2)
        road(b, from, c, to, wd)
    }

    private fun roads(b: Buf) {
        // the main street, from the post office up to the bridge
        var y = World.POST.y
        while (y > World.BRIDGE.y) {
            val y2 = (y - 12).coerceAtLeast(World.BRIDGE.y)
            road(b, Pt(street(y), y), Pt(street((y + y2) / 2), (y + y2) / 2), Pt(if (y2 == World.BRIDGE.y) World.BRIDGE.x else street(y2), y2), 3)
            y = y2
        }
        for (hs in World.houses.filter { it.district == 0 }) lane(b, Pt(street(hs.at.y + 6), hs.at.y + 6), Pt(hs.at.x, hs.at.y + 5))
        lane(b, Pt(street(430.0), 430.0), Pt(122.0, 433.0))
        // Zarechye: the forest road from the bridge to the railway crossing, lanes to the houses
        val cross = Pt(118.0, 220.0)
        road(b, World.BRIDGE, Pt(98.0, 300.0), cross, 2)
        fun forest(y: Double): Pt { val t = (World.BRIDGE.y - y) / (World.BRIDGE.y - cross.y); return quad(World.BRIDGE.x, World.BRIDGE.y, 98.0, 300.0, cross.x, cross.y, t).let { Pt(it.first, it.second) } }
        for (hs in World.houses.filter { it.district == 1 }) lane(b, forest(hs.at.y + 6), Pt(hs.at.x, hs.at.y + 5))
        // beyond the railway
        road(b, cross, Pt(116.0, 210.0), World.house("halt")!!.at, 2)
        road(b, cross, Pt(140.0, 214.0), World.house("stationhouse")!!.at, 1)
        road(b, Pt(112.0, 200.0), Pt(96.0, 192.0), Pt(90.0, 182.0), 1)
        road(b, Pt(90.0, 182.0), Pt(88.0, 168.0), World.house("boatshed")!!.at, 1)
        road(b, World.house("boatshed")!!.at, Pt(84.0, 130.0), World.house("painter")!!.at, 1)
        road(b, Pt(120.0, 196.0), Pt(130.0, 186.0), Pt(134.0, 176.0), 1)
        road(b, Pt(134.0, 176.0), Pt(130.0, 156.0), World.house("belkiny")!!.at, 1)
        road(b, World.house("belkiny")!!.at, Pt(140.0, 116.0), World.house("meteo")!!.at, 1)
        road(b, Pt(114.0, 196.0), Pt(104.0, 140.0), Pt(100.0, 78.0), 2)
        road(b, Pt(100.0, 78.0), Pt(84.0, 60.0), World.house("newspaper")!!.at, 2)
        road(b, Pt(100.0, 78.0), Pt(114.0, 56.0), World.house("museum")!!.at, 2)
    }

    private fun woods(b: Buf) {
        val trees = mutableListOf<Triple<Int, Int, Double>>()
        fun area(x0: Int, y0: Int, x1: Int, y1: Int, step: Int, keep: (Int, Int) -> Boolean) {
            var gy = y0
            while (gy < y1) {
                var gx = x0
                while (gx < x1) {
                    val x = gx + (hash(gx, gy) * step * .7).toInt() - step / 3
                    val y = gy + (hash(gy, gx) * step * .6).toInt() - step / 3
                    if (keep(x, y)) trees += Triple(x, y, hash(gx + 9, gy))
                    gx += step
                }
                gy += step
            }
        }
        fun clear(x: Int, y: Int): Boolean {
            if (riverD(x + 5, y + 14) < 13) return false
            if (inLake(x + 5, y + 14) || inLake(x, y)) return false
            if (abs(y + 16 - 212) < 6) return false
            if (World.houses.any { hypot(it.at.x - (x + 5), it.at.y - (y + 14)) < 18 }) return false
            if (hypot(x + 5 - World.POST.x, y + 14 - World.POST.y) < 30) return false
            return true
        }
        area(0, 236, 170, 330, 11) { x, y -> clear(x, y) && (x < 70 || x > 128 || hash(x, y) > .6) && abs(x + 5 - 108) > 7 }
        area(100, 60, 170, 196, 10) { x, y -> clear(x, y) }
        area(0, 0, 40, 100, 12) { x, y -> clear(x, y) }
        area(140, 0, 170, 60, 11) { x, y -> clear(x, y) }
        area(0, 380, 30, 450, 13) { x, y -> clear(x, y) && riverD(x, y) > 14 }
        area(150, 470, 170, 600, 14) { x, y -> clear(x, y) }
        trees.sortBy { it.second }
        for ((x, y, k) in trees) {
            if (k > .72) Props.birch(b, x + 4, y, 16, e.leaves, alt = k > .86)
            else Props.spruce(b, x, y, 18 + (k * 6).roundToInt(), snow = winter)
        }
    }

    /** A house on the map: log walls, a pitched roof, carved window frames; [cx, cy] is its centre. */
    private fun hut(b: Buf, cx: Int, cy: Int, wd: Int, roof: IntArray, frame: Int, lit: Boolean, wins: Int = 2, door: Boolean = true, chim: Boolean = true) {
        val rh = 11
        val wh = 11
        val x0 = cx - wd / 2
        val y0 = cy - rh - wh + 6
        for (j in 0 until 4) for (i in 0 until wd + 2) b.mul(x0 + 3 + i, y0 + rh + wh - 1 + j, rgb(0x4a4a3a), .4f - j * .08f)
        for (y in 0 until wh) for (x in 0 until wd) {
            val k = y % 3
            b.p(x0 + x, y0 + rh + y, when (k) {
                0 -> rp(R.wood, .72, x0 + x, y)
                1 -> rp(R.wood, .56 + fbm(x * .3, y.toDouble()) * .1, x0 + x, y)
                else -> rgb(0x3a2214)
            })
        }
        var yy = 0
        while (yy < wh) { b.p(x0 - 1, y0 + rh + yy, rgb(0xc88e58)); b.p(x0 + wd, y0 + rh + yy, rgb(0xc88e58)); yy += 3 }
        val half = wd / 2 + 2
        for (v in 0..rh) {
            val hw = (half * v.toDouble() / rh).roundToInt()
            for (u in -hw until hw) {
                var l = if (u < 0) .62 else .38
                if ((v + (u + 40) % 2) % 3 == 0) l -= .14
                val px = cx + u
                val py = y0 + v
                b.p(px, py, if (winter && v < rh - 2 && hash(px, py) > .15) rp(R.snow, l + .2, px, py) else rp(roof, l + hash(px, py) * .08, px, py))
            }
            b.p(cx - hw - 1, y0 + v, R.INK); b.p(cx + hw, y0 + v, R.INK)
        }
        b.r(cx - half - 1, y0 + rh, 2 * half + 2, 1, R.INK)
        var u = -half
        while (u < half) { b.p(cx + u, y0 + rh + 1, rgb(0xe8dcc4)); u += 2 }
        b.r(cx - 2, y0 + rh - 6, 4, 3, rgb(0x2a1a10)); b.r(cx - 1, y0 + rh - 5, 2, 1, if (lit) rgb(0xf6d77a) else rgb(0x8aa0a8))
        val spots = if (wins == 1) listOf(3) else listOf(3, wd - 9)
        for (s in spots) {
            val x = x0 + s
            val y = y0 + rh + 3
            b.r(x - 1, y - 2, 7, 1, frame); b.p(x + 2, y - 3, frame); b.r(x - 1, y - 1, 1, 6, frame); b.r(x + 5, y - 1, 1, 6, frame); b.r(x - 1, y + 5, 7, 1, frame)
            b.r(x, y - 1, 5, 6, if (lit) rgb(0xf6d77a) else rgb(0x5c7480))
            b.r(x + 2, y - 1, 1, 6, rgb(0x2a1a10)); b.r(x, y + 1, 5, 1, rgb(0x2a1a10))
            if (!lit) { b.p(x, y, rgb(0x9ab4bc)); b.p(x + 3, y, rgb(0x9ab4bc)) }
        }
        if (door) { b.r(x0 + wd - 6, y0 + rh + wh - 7, 4, 7, rgb(0x3a2214)); b.p(x0 + wd - 3, y0 + rh + wh - 4, rgb(0xe8bf58)) }
        if (chim) { b.r(cx + 4, y0 + rh - 9, 3, 6, rgb(0x8e3a24)); b.r(cx + 3, y0 + rh - 10, 5, 1, rgb(0x4a1a12)) }
    }

    private fun roofOf(c: Char) = when (c) {
        'R' -> R.roofR
        'B' -> R.roofB
        'G' -> R.roofG
        'T' -> R.thatch
        'S' -> R.roofS
        else -> R.roofW
    }

    private fun frameOf(c: Char) = when (c) {
        'B' -> rgb(0x7aa0d8)
        'G' -> rgb(0x8ac08a)
        'Y' -> rgb(0xf0d070)
        else -> rgb(0xf2ece0)
    }

    private fun building(b: Buf, hs: House) {
        val cx = hs.at.x.roundToInt()
        val cy = hs.at.y.roundToInt()
        val lit = e.phase.lamps
        when (hs.id) {
            "mill" -> {
                hut(b, cx + 4, cy, 22, R.thatch, frameOf(hs.frame), lit, wins = 1)
            }
            "halt" -> {
                hut(b, cx, cy, 30, R.roofS, frameOf(hs.frame), lit)
                b.r(cx - 18, cy + 6, 40, 3, rgb(0x8e857a)); b.r(cx - 18, cy + 6, 40, 1, rgb(0xb4aca0))
                b.r(cx - 6, cy - 22, 12, 4, rgb(0xfbf3dc)); b.r(cx - 5, cy - 21, 10, 1, rgb(0x26375e)); b.r(cx - 5, cy - 19, 8, 1, rgb(0x26375e))
                b.line(cx + 22, cy - 14, cx + 22, cy + 6, rgb(0x2a2a30)); b.r(cx + 20, cy - 16, 5, 3, rgb(0xd83a2a))
            }
            "meteo" -> {
                hut(b, cx, cy, 22, R.roofS, frameOf(hs.frame), lit, wins = 1)
                b.line(cx + 16, cy - 30, cx + 16, cy + 4, rgb(0x55504c))
                b.r(cx + 13, cy - 30, 7, 1, rgb(0x8e857a)); b.disc(cx + 19, cy - 31, 1, rgb(0xd83a2a))
                b.r(cx - 18, cy - 4, 6, 6, rgb(0xf2ece0)); b.r(cx - 18, cy - 4, 6, 1, rgb(0xb4aca0)); b.line(cx - 15, cy + 2, cx - 15, cy + 6, rgb(0xf2ece0))
            }
            "museum" -> {
                b.vol(cx - 18, cy - 20, 36, 22, { _, _ -> true }, { u, v -> .7 - u * .008 - v * .01 }, intArrayOf(rgb(0xb8a888), rgb(0xd8c8a4), rgb(0xece0c4), rgb(0xf8f0dc)), R.INK)
                for (i in 0 until 5) b.r(cx - 15 + i * 7, cy - 14, 2, 15, rgb(0xfffaf0))
                for (v in 0 until 8) b.r(cx - 20 + v * 2, cy - 28 + v, 40 - v * 4, 1, rp(R.roofG, .5, cx, v))
                b.r(cx - 3, cy - 6, 6, 8, rgb(0x3a2214))
                if (lit) for (i in 0 until 4) b.r(cx - 12 + i * 7, cy - 10, 3, 3, rgb(0xf6d77a))
            }
            "newspaper" -> {
                b.vol(cx - 15, cy - 26, 30, 28, { _, _ -> true }, { u, v -> .6 - u * .01 - (if (v % 9 == 0) .2 else 0.0) }, R.brick, R.INK)
                for (r in 0 until 2) for (i in 0 until 4) b.r(cx - 12 + i * 7, cy - 22 + r * 11, 4, 5, if (lit) rgb(0xf6d77a) else rgb(0x5c7480))
                b.r(cx - 16, cy - 28, 32, 3, rgb(0x50505a))
                b.r(cx - 9, cy - 2, 18, 3, rgb(0xfbf3dc)); b.r(cx - 7, cy - 1, 14, 1, rgb(0x842a24))
            }
            else -> {
                val wd = when (hs.id) { "club" -> 30; "shop" -> 26; "lastochkiny", "farmstead" -> 22; "stationhouse", "painter" -> 20; else -> 24 }
                hut(b, cx, cy, wd, roofOf(hs.roof), frameOf(hs.frame), lit)
            }
        }
        extras(b, hs, cx, cy)
    }

    private fun extras(b: Buf, hs: House, cx: Int, cy: Int) {
        val ps = hs.props
        if ("hives" in ps) for (k in 0 until 6) {
            val x = cx + 12 + (k % 3) * 6
            val y = cy - 6 + (k / 3) * 7
            b.r(x, y + 2, 5, 5, rgb(0xe0a630)); b.r(x, y + 2, 5, 1, rgb(0xf4cf6e)); b.r(x - 1, y + 1, 7, 1, if (winter) rgb(0xf2f6fa) else rgb(0x8e3a24)); b.r(x, y + 7, 5, 1, rgb(0x22130b))
        }
        if ("rowan" in ps) {
            Props.leafy(b, cx - 18, cy + 2, 6, e.leaves, rgb(0xd82a1a))
            if (e.leaves == Leaves.BARE && e.month in listOf(11, 12, 1)) for (k in 0 until 5) b.p(cx - 18 + (hash(k, 1) * 8 - 4).toInt(), cy - 6 + (hash(k, 2) * 6).toInt(), rgb(0xd82a1a))
        }
        if ("well" in ps) {
            val x = cx + 16
            b.r(x, cy - 2, 8, 5, rgb(0x706860)); b.r(x, cy - 2, 8, 1, rgb(0xada296))
            b.line(x + 2, cy - 16, x + 2, cy - 2, rgb(0x3a2214)); b.line(x - 4, cy - 20, x + 16, cy - 4, rgb(0x55331e)); b.line(x - 4, cy - 20, x - 4, cy - 10, rgb(0x8e857a))
        }
        if ("antenna" in ps) { b.line(cx + 6, cy - 34, cx + 6, cy - 14, rgb(0x55504c)); b.line(cx, cy - 32, cx + 12, cy - 32, rgb(0x55504c)); b.line(cx + 2, cy - 28, cx + 10, cy - 28, rgb(0x55504c)) }
        if ("telescope" in ps) { b.line(cx + 16, cy + 2, cx + 18, cy - 4, rgb(0x2a2a30)); b.line(cx + 20, cy + 2, cx + 18, cy - 4, rgb(0x2a2a30)); b.line(cx + 15, cy - 8, cx + 22, cy - 3, rgb(0xc8952e)) }
        if ("goat" in ps && !winter) { val x = cx - 20; b.r(x, cy, 5, 3, rgb(0xe8e2d4)); b.r(x + 4, cy - 2, 2, 2, rgb(0xe8e2d4)); b.p(x, cy + 3, rgb(0x2a2420)); b.p(x + 4, cy + 3, rgb(0x2a2420)) }
        if ("garden" in ps || "swing" in ps) {
            val x0 = cx - 14
            val y0 = cy + 8
            for (x in x0 until x0 + 16 step 2) { b.p(x, y0, rgb(0x8a7a62)); b.p(x, y0 + 10, rgb(0x8a7a62)) }
            if (!winter && e.season != Season.SPRING) for (y in y0 + 2 until y0 + 9 step 3) for (x in x0 + 2 until x0 + 15 step 3) { b.disc(x, y, 1, rgb(0x7e9c62)); b.p(x, y, rgb(0xb8d08a)) }
        }
        if ("woodpile" in ps) for (j in 0 until 3) for (i in 0 until 4 - j % 2) { b.disc(cx + 14 + i * 3 + j % 2, cy + 2 - j * 3, 1, rgb(0xc88e58)); b.p(cx + 14 + i * 3 + j % 2, cy + 2 - j * 3, rgb(0x8e5a34)) }
        if ("boat" in ps) b.vol(cx - 26, cy - 2, 14, 4, { u, v -> u > v && u < 14 - v }, { _, _ -> .6 }, R.red, R.INK)
        if ("easel" in ps) { b.line(cx + 14, cy + 2, cx + 17, cy - 8, rgb(0x7c4e30)); b.line(cx + 20, cy + 2, cx + 17, cy - 8, rgb(0x7c4e30)); b.r(cx + 14, cy - 8, 7, 5, rgb(0xfbf3dc)); b.p(cx + 16, cy - 6, rgb(0x4a7aca)); b.p(cx + 18, cy - 7, rgb(0xe8a040)) }
        if ("lantern" in ps) { b.line(cx + 14, cy - 12, cx + 14, cy + 4, rgb(0x2a2a30)); b.r(cx + 13, cy - 15, 3, 3, if (e.phase.lamps) rgb(0xffd060) else rgb(0x6a6a70)) }
        if ("shop" in ps) { b.r(cx - 8, cy - 18, 16, 3, rgb(0xfbf3dc)); b.r(cx - 6, cy - 17, 12, 1, rgb(0x2a4a2a)) }
        if ("club" in ps) { b.r(cx - 10, cy - 18, 20, 3, rgb(0xfbf3dc)); b.r(cx - 8, cy - 17, 16, 1, rgb(0x842a24)) }
        if ("cheese" in ps && !winter) for (k in 0 until 2) b.r(cx + 14 + k * 4, cy - 1, 3, 2, rgb(0xf4cf6e))
        if ("owl" in ps) { b.r(cx - 18, cy - 10, 3, 4, rgb(0x8e643a)); b.p(cx - 18, cy - 9, rgb(0xf8d070)); b.p(cx - 16, cy - 9, rgb(0xf8d070)) }
    }

    private fun post(b: Buf) {
        val px = World.POST.x.roundToInt() - 19
        val py = World.POST.y.roundToInt() - 18
        for (j in 0 until 4) for (i in 0 until 42) b.mul(px + 3 + i, py + 24 + j, rgb(0x4a4a3a), .4f - j * .08f)
        for (y in 0 until 13) for (x in 0 until 38) b.p(px + x, py + 12 + y, when (y % 3) { 0 -> rgb(0xe0c494); 1 -> rgb(0xd0ae7e); else -> rgb(0x8a6a44) })
        for (v in 0 until 12) {
            val hw = (21 * v / 12.0).roundToInt()
            for (u in -hw until hw) {
                var l = if (u < 0) .6 else .36
                if ((v + (u + 40) % 2) % 3 == 0) l -= .12
                b.p(px + 19 + u, py + v, if (winter && v < 10 && hash(u, v) > .2) rp(R.snow, l + .2, px + u, v) else rp(R.roofB, l, px + u, v))
            }
            b.p(px + 19 - hw - 1, py + v, rgb(0x06080e)); b.p(px + 19 + hw, py + v, rgb(0x06080e))
        }
        b.r(px - 3, py + 12, 44, 1, rgb(0x06080e))
        var u = -21
        while (u < 21) { b.p(px + 19 + u, py + 13, rgb(0xe8dcc4)); u += 2 }
        b.r(px + 12, py + 5, 14, 6, rgb(0x2a1a10)); b.r(px + 13, py + 6, 12, 4, rgb(0xf8eed4)); Props.envelope(b, px + 15, py + 6, 8, 4)
        b.r(px + 16, py + 17, 6, 8, rgb(0x3a2214)); b.p(px + 21, py + 21, rgb(0xe8bf58))
        for ((x, y) in listOf(px + 3 to py + 16, px + 28 to py + 16)) {
            b.r(x - 1, y - 1, 8, 7, rgb(0xf2ece0)); b.r(x, y, 6, 5, rgb(0xf6d77a)); b.r(x + 3, y, 1, 5, rgb(0x2a1a10)); b.r(x, y + 2, 6, 1, rgb(0x2a1a10))
        }
        b.r(px + 24, py + 18, 4, 6, rgb(0x304474)); b.r(px + 24, py + 18, 4, 1, rgb(0x5a74aa)); b.r(px + 25, py + 20, 2, 1, rgb(0x0c1228))
        b.r(px + 8, py - 6, 3, 6, rgb(0x8e3a24)); b.r(px + 7, py - 7, 5, 1, rgb(0x4a1a12))
        b.line(px + 42, py - 6, px + 42, py + 24, rgb(0x22130b))
    }

    /** The school, the square, the trees of the village. */
    private fun village(b: Buf) {
        hut(b, 122, 428, 30, R.thatch, rgb(0xf2ece0), e.phase.lamps && e.month !in listOf(6, 7, 8))
        b.r(130, 404, 3, 8, rgb(0x7c4e30)); b.r(129, 403, 5, 2, rgb(0x4a2c1a)); b.disc(131, 408, 1, rgb(0xe8bf58))
        for ((x, y, k) in listOf(Triple(60, 540, 1), Triple(160, 530, 2), Triple(14, 500, 3), Triple(90, 444, 4), Triple(160, 480, 5), Triple(56, 452, 6)))
            Props.leafy(b, x, y, 5 + k % 2, e.leaves, if (k % 2 == 0) rgb(0xd83a2a) else null)
        for ((x, y) in listOf(166 to 420, 8 to 590, 150 to 600)) Props.birch(b, x, y, 18, e.leaves, alt = x > 100)
    }

    private fun events(b: Buf) {
        if (e.has(Look.NEWYEAR)) {
            Props.spruce(b, 112, 524, 22, snow = winter)
        }
        if (e.has(Look.FAIR)) for (k in 0 until 3) {
            val x = 70 + k * 12
            val y = 532
            for (v in 0 until 6) b.r(x - v, y + v, 1 + v * 2, 1, if ((k + v) % 2 == 0) rgb(0xd83a2a) else rgb(0xfbf3dc))
            b.r(x - 5, y + 6, 11, 4, rgb(0x8e5a34))
        }
        if (e.has(Look.MASLENITSA)) {
            b.line(84, 540, 84, 520, rgb(0x7c4e30)); b.line(78, 526, 90, 526, rgb(0x7c4e30))
            b.vol(80, 520, 9, 14, ell(4.5, 7.0, 4.5, 7.0), sph(3.0, 4.0, 5.0, 7.0, .3), R.thatch, R.INK)
            b.r(80, 520, 9, 3, rgb(0xd83a3a))
        }
        if (e.has(Look.KUPALA)) b.disc(70, 392, 3, rgb(0x3a2214))
        if (e.has(Look.FISHING)) for (k in 0 until 3) {
            val x = 20 + k * 14
            val y = 120 + k * 12
            b.vol(x, y, 9, 3, { u, v -> u > v && u < 9 - v }, { _, _ -> .5 }, R.wood, R.INK)
            b.line(x + 5, y, x + 9, y - 6, rgb(0x2a1a10))
        }
        if (e.has(Look.RAILWAY)) for (x in 96 until 132 step 3) b.p(x, 176 + ((x / 3) % 2), intArrayOf(rgb(0xd83a3a), rgb(0xe8bf58), rgb(0x4a7aca))[(x / 3) % 3])
        if (e.has(Look.LILAC)) for ((x, y) in listOf(50 to 512, 128 to 498, 30 to 480)) for (k in 0 until 18) b.p(x + (hash(k, x) * 8).toInt(), y + (hash(x, k) * 6).toInt(), if (k % 3 == 0) rgb(0x6a4a7a) else rgb(0xb494bc))
        if (e.has(Look.MUSHROOMS) || e.has(Look.BERRIES)) for (k in 0 until 14) {
            val x = 10 + (hash(k, 3) * 150).toInt()
            val y = 250 + (hash(k, 5) * 70).toInt()
            if (e.has(Look.MUSHROOMS)) { b.p(x, y, rgb(0xb83a2a)); b.p(x + 1, y, rgb(0xb83a2a)); b.p(x, y + 1, rgb(0xf2ece0)) } else b.p(x, y, rgb(0xd83a4a))
        }
        if (e.has(Look.SCHOOL)) for (k in 0 until 6) b.p(112 + k * 3, 444, intArrayOf(rgb(0xd83a3a), rgb(0xf8d070), rgb(0xf2ece0))[k % 3])
    }

    /** Lamps and lit windows glowing after dark. */
    private fun lights(b: Buf) {
        if (!e.phase.lamps) return
        for (hs in World.houses) if (hs.district <= open) b.glow(hs.at.x.roundToInt(), hs.at.y.roundToInt() - 4, 14, rgb(0xffc060), .22f, 4)
        b.glow(World.POST.x.roundToInt(), World.POST.y.roundToInt() - 2, 22, rgb(0xffc060), .3f, 5)
        for ((x, y) in listOf(110 to 560, 104 to 500, 106 to 440, 104 to 372)) {
            b.line(x, y, x, y - 12, rgb(0x2a2a30)); b.r(x - 1, y - 14, 3, 2, rgb(0xfff0b0))
            b.glow(x, y - 12, 16, rgb(0xfff0b0), .3f, 4)
        }
        if (e.has(Look.NEWYEAR)) b.glow(123, 514, 18, rgb(0xffe090), .3f, 4)
        if (e.has(Look.KUPALA)) b.glow(70, 390, 20, rgb(0xff9a40), .4f, 5)
    }

    /** Which district a map pixel belongs to. */
    private fun regionOf(x: Int, y: Int): Int = when {
        y < 80 -> 5
        y < 196 -> if (x < 84) 3 else 4
        y < 232 -> 2
        y < 346 -> 1
        else -> 0
    }

    /** Districts not open yet lie under a thick mist that thins at their edges. */
    private fun locked(b: Buf) {
        if (open >= 5) return
        val c = if (e.phase.dark) rgb(0x2a3048) else rgb(0xe6e4dc)
        val probes = listOf(0 to 0, 9 to 0, -9 to 0, 0 to 9, 0 to -9, 6 to 6, -6 to -6, 6 to -6, -6 to 6)
        for (y in 0 until 360) for (x in 0 until w) {
            val d = probes.count { (i, j) -> regionOf(x + i, y + j) > open }.toDouble() / probes.size
            if (d <= 0) continue
            val f = (d * 1.2 + (fbm(x * .05, y * .05) - .5) * .5).coerceIn(0.0, 1.0)
            val lv = kotlin.math.floor(f * 4 + (bay(x, y) / 16.0 - .5)) / 4
            if (lv > 0) b.p(x, y, c, (lv * .9).toFloat().coerceAtMost(.9f))
        }
    }

    override fun anim(b: Buf, t: Int) {
        val iced = e.ice && !e.has(Look.ICEBREAK)
        if (!iced) for ((k, pt) in riverPts.withIndex()) {
            if (k % 3 != 0) continue
            if ((k + t * 2) % 40 < 5) b.p(pt.first - 2, pt.second - 1, rgb(0xb8d4d8), .8f)
            if ((k + t * 2 + 20) % 40 < 4) b.p(pt.first + 2, pt.second + 1, rgb(0xb8d4d8), .6f)
        }
        if (e.sky.rain && !iced) for (i in 0 until 14) {
            val pt = riverPts[(rnd(i * 3 + (t + i * 5) / 10) * riverPts.size).toInt().coerceIn(0, riverPts.size - 1)]
            val r = ((t + i * 5) % 10) / 3.0
            if (r < .5) continue
            for (a in 0 until 12) {
                val an = a / 12.0 * 2 * PI
                b.p((pt.first + cos(an) * r * 1.4).roundToInt(), (pt.second + sin(an) * r * .7).roundToInt(), rgb(0xd0e4e8), (.6 * (1 - r / 3.4)).toFloat())
            }
        }
        // the mill wheel turning (still in hard frost)
        val mill = World.house("mill")!!
        val wx = mill.at.x.roundToInt() - 12
        val wy = mill.at.y.roundToInt() - 2
        b.disc(wx, wy, 7, rgb(0x3a2214)); b.disc(wx, wy, 5, if (iced) rgb(0xc8d4e0) else rgb(0x5a8090))
        val wa = if (iced) .3 else t * .15
        for (q in 0 until 8) {
            val an = wa + q * PI / 4
            b.line(wx.toDouble(), wy.toDouble(), wx + cos(an) * 7, wy + sin(an) * 7, rgb(0x8e5a34))
        }
        if (!iced) for (i in 0 until 5) { val ph = (t + i * 3) % 8; b.p((wx - 4 - ph * .5 + i).roundToInt(), (wy + 7 - ph * .3).roundToInt(), rgb(0xe4f2f4), (.8 * (1 - ph / 8.0)).toFloat()) }
        // chimneys
        for ((i, hs) in World.houses.filter { it.district <= open }.withIndex()) {
            val still = e.temp < -10
            Props.smoke(b, hs.at.x.roundToInt() + 6, hs.at.y.roundToInt() - 26, t + i * 7, 7, if (still) 34 else 26, rgb(0xd0ccc6), .5f, if (still) .02 else .4)
        }
        Props.smoke(b, World.POST.x.roundToInt() - 9, World.POST.y.roundToInt() - 25, t, 7, 26, rgb(0xd0ccc6), .55f)
        // the post office flag
        for (j in 0 until 5) for (i in 0 until 8) {
            val off = sin(t * .5 - i * .6).roundToInt()
            b.p(World.POST.x.roundToInt() + 24 + i, World.POST.y.roundToInt() - 24 + j + off, if (j < 2) rgb(0xe8e0d8) else if (j < 4) rgb(0x2c4070) else rgb(0xa83e28))
        }
        // bees, cranes, the train now and then
        if (e.season == Season.SUMMER || (e.season == Season.SPRING && e.month == 5)) {
            val ap = World.house("apiary")!!.at
            for (i in 0 until 5) b.p(ap.x + 16 + sin(t * .4 + i * 2) * 8 + i * 2, ap.y - 12 + cos(t * .5 + i) * 4, rgb(0x2a1a10))
        }
        if (e.has(Look.CRANES)) {
            val cx = ((t * .8) % (w + 60)) - 30
            for (i in 0 until 9) {
                val x = (cx - abs(i - 4) * 4).roundToInt()
                val y = 300 + i * 3 - (if (i > 4) (i - 4) * 6 else 0)
                b.p(x, y, rgb(0x2a2a30)); b.p(x - 1, y - 1, rgb(0x2a2a30)); b.p(x + 1, y - 1, rgb(0x2a2a30))
            }
        }
        if (open >= 2) {
            val tx = ((t * 1.6) % 600) - 200
            if (tx > -60 && tx < w + 10) for (car in 0 until 3) {
                val x = tx.roundToInt() - car * 16
                b.r(x, 205, 14, 6, if (car == 0) rgb(0x2a4a2a) else rgb(0x3a6a3a)); b.r(x + 2, 206, 3, 2, rgb(0xf6d77a)); b.r(x + 8, 206, 3, 2, rgb(0xf6d77a)); b.r(x, 211, 14, 1, R.INK)
                if (car == 0) Props.smoke(b, x + 11, 203, t, 5, 12, rgb(0xd8d8d8), .6f)
            }
        }
        if (e.has(Look.NEWYEAR)) for (k in 0 until 10) {
            val x = 112 + (hash(k, 1) * 14).toInt()
            val y = 506 + (hash(k, 2) * 18).toInt()
            if ((t + k) % 4 != 0) b.p(x, y, intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[k % 3])
        }
        if (e.has(Look.KUPALA)) for (i in 0 until 6) Props.smoke(b, 70, 390, t + i * 3, 3, 10, if (i % 2 == 0) rgb(0xffb040) else rgb(0xff6020), .8f, 0.0)
        // the round: dots ahead, the postman and the dog
        drawRound(b, t)
        // weather over everything
        Air.precip(b, e, t, 0, 0, w, h, 1.0, still = Art.still)
        Air.fog(b, e, t, 0, 0, w, h, .5f)
        if (e.leaves == Leaves.FALLING && !Art.still) for (i in 0 until 12) {
            val x = ((rnd(i) * w + sin(t * .1 + i) * 6) % w).roundToInt()
            val y = ((rnd(i + 50) * h + t * .6) % h).roundToInt()
            b.p(x, y, if (i % 2 == 0) rgb(0xe0a630) else rgb(0xc05638))
        }
    }

    private fun dots(b: Buf, pts: List<Pt>, solid: Boolean, c: Int) {
        for ((p, q) in pts.zipWithNext()) {
            val n = (p.to(q) * 1.3).toInt().coerceAtLeast(1)
            for (k in 0..n) {
                if (!solid && k % 3 != 0) continue
                val x = p.x + (q.x - p.x) * k / n
                val y = p.y + (q.y - p.y) * k / n
                b.p(x, y, c); b.p(x + 1, y, c)
            }
        }
    }

    private fun drawRound(b: Buf, t: Int) {
        dots(b, round.later, false, rgb(0xfff0c0))
        dots(b, round.ahead, false, rgb(0xf6c440))
        for (id in round.visited) {
            val hs = World.house(id) ?: continue
            val x = hs.at.x.roundToInt() + 6
            val y = hs.at.y.roundToInt() - 30
            b.r(x, y, 9, 8, R.INK); b.r(x + 1, y + 1, 7, 6, rgb(0x426442))
            for ((dx, dy) in listOf(2 to 4, 3 to 5, 4 to 4, 5 to 3, 6 to 2)) b.p(x + dx, y + dy, rgb(0xfbf3dc))
        }
        for ((i, id) in round.pending.withIndex()) {
            val hs = World.house(id) ?: continue
            val o = if (Art.still) 0 else ((t / 5 + i) % 2)
            val x = hs.at.x.roundToInt() - 6
            val y = hs.at.y.roundToInt() - 34 + o
            b.r(x - 1, y - 1, 14, 10, R.INK); b.r(x, y, 12, 8, rgb(0xfbf3dc)); Props.envelope(b, x + 1, y + 1, 10, 6); b.r(x + 5, y + 9, 2, 2, R.INK)
        }
        val f = if (round.walking && !Art.still) (t / 3) % 2 else 0
        val px = round.postman.x.roundToInt()
        val py = round.postman.y.roundToInt()
        People.mini(b, px - 3, py, winter, f)
        if (dog) People.dogMini(b, px + 4, py, f)
    }
}
