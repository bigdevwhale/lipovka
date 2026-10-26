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
    private val face = Facades.of(house.id)
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
        val f = face
        if (f.left == Annex.VERANDA) veranda(b)
        when (f.right) {
            Annex.SHED -> shed(b)
            Annex.WHEEL -> wheel(b)
            else -> Unit
        }
        walls(b)
        if (f.side) sideRoof(b) else frontRoof(b)
        val (fr, acc) = frame()
        val gw = if (f.narrow || f.trim == Trim.TALL) 16 else 20
        val n = f.windows
        val span = if (f.right == Annex.SHOPFRONT) f.w - 52 else f.w
        val gap = (span - n * gw) / (n + 1)
        for (i in 0 until n) {
            val x = f.x + gap + i * (gw + gap)
            if (f.right == Annex.COLUMNS && n == 2) window(b, if (i == 0) f.x + 12 else f.x + f.w - 12 - gw, f.top + 22, gw, fr, acc)
            else window(b, x, f.top + 22, gw, fr, acc)
        }
        when (f.right) {
            Annex.PORCH -> porch(b, fr)
            Annex.SHOPFRONT -> shopfront(b)
            Annex.COLUMNS -> portico(b)
            else -> Unit
        }
        if (f.plinth) for (y in 142 until 152) for (x in f.x until f.x + f.w) b.p(x, y, rp(R.brick, .5 + (if ((y - 142) % 3 == 0) -.25 else 0.0) + (if ((x + (y - 142) / 3 * 3) % 6 == 0) -.2 else 0.0), x, y))
        else for (x in f.x - 3 until f.x + f.w + 1 step 6) b.vol(x, 150, 6, 5, { _, _ -> true }, { u, v -> .6 - u * .06 - v * .05 }, R.stone, rgb(0x1a1614))
        val cx = f.x + f.w / 2
        when (house.id) {
            "halt" -> { b.r(cx - 17, f.top + 4, 34, 9, rgb(0xfbf3dc)); b.r(cx - 15, f.top + 7, 30, 1, rgb(0x26375e)); b.r(cx - 15, f.top + 9, 22, 1, rgb(0x26375e)) }
            "shop" -> { b.r(f.x + 8, f.top + 6, 40, 10, rgb(0x2a4a2a)); b.r(f.x + 10, f.top + 9, 36, 1, rgb(0xf2ece0)); b.r(f.x + 10, f.top + 12, 26, 1, rgb(0xf2ece0)) }
            "club" -> { b.r(cx - 17, f.top + 4, 34, 9, rgb(0x842a24)); b.r(cx - 15, f.top + 7, 30, 1, rgb(0xf8d070)); b.r(cx - 15, f.top + 9, 18, 1, rgb(0xf8d070)) }
        }
    }

    /** Log rows with the corner ends sticking out, or boards. */
    private fun walls(b: Buf) {
        val f = face
        val mid = f.x + f.w / 2
        for (y in f.top until 150) for (x in f.x until f.x + f.w) {
            if (f.wall == Wall.PLANKS) {
                val paint = if (f.paint2 != null && x >= mid) f.paint2 else f.paint
                val seam = if (f.side) (y - f.top) % 5 == 0 else (x - f.x) % 6 == 0
                b.p(x, y, if (seam) paint.dim(.45f) else paint.dim(((x - f.x) / f.w.toFloat()) * .2f + (fbm(x * .2, y * .3) * .1).toFloat() + if (f.side && (y - f.top) % 5 == 1) -.06f else 0f))
            } else {
                val k = (y - f.top) % 5
                val l = when (k) { 0 -> .78; 1 -> .66; 2 -> .55; 3 -> .44; else -> .22 }
                b.p(x, y, rp(logs(), l + (fbm(x * .15, y * .6) - .5) * .18 - (x - f.x) / f.w.toDouble() * .12 + logTone(), x, y))
                if (f.wall == Wall.OLD && hash(x, y) > .985) b.p(x, y, rgb(0x2a2420))
            }
        }
        if (f.paint2 != null) b.r(mid, f.top, 1, 150 - f.top, rgb(0xf2ece0))
        if (f.wall != Wall.PLANKS) {
            var y = f.top
            while (y < 150) {
                for (x in listOf(f.x - 3, f.x + f.w - 1)) {
                    b.vol(x, y, 4, 5, ell(2.0, 2.5, 2.0, 2.5), sph(1.5, 2.0, 2.0, 2.5, .3), logs(), rgb(0x1e100a))
                    b.p(x + 2, y + 2, logs()[2])
                }
                y += 5
            }
        } else {
            b.r(f.x - 2, f.top, 3, 150 - f.top, f.paint.lit(.3f)); b.r(f.x + f.w - 1, f.top, 3, 150 - f.top, (f.paint2 ?: f.paint).lit(.3f))
        }
    }

    private fun logs() = if (face.wall == Wall.OLD) R.woodG else R.wood
    private fun logTone() = when (face.wall) { Wall.NEW -> .12; Wall.DARK -> -.16; Wall.OLD -> .05; else -> 0.0 }

    /** A pixel of the roof: painted tin with standing seams, shingles, slate, or thatch. */
    private fun roofPx(b: Buf, x: Int, y: Int, l0: Double, row: Int) {
        val roof = roof()
        var l = l0
        when (house.roof) {
            'T' -> l += (hash(x, y / 3) - .5) * .3 + if (y % 6 == 0) -.12 else 0.0
            'S' -> l += kotlin.math.sin(x * 1.1) * .1 + if (row % 6 == 0) -.2 else 0.0
            'W' -> l += (if (row % 4 == 0) -.18 else 0.0) + (if ((x + (row / 4) * 3) % 6 == 0) -.12 else 0.0) + (hash(x / 6, row / 4) - .5) * .1
            else -> l += (if (x % 6 == 0) .16 else if (x % 6 == 1) -.1 else 0.0)
        }
        b.p(x, y, if (winter && hash(x, y) > .1 && row % 4 != 0) rp(R.snow, l + .2, x, y) else rp(roof, l, x, y))
    }

    /** Where the gable's apex is (front) or the ridge (side). */
    private val apex: Int get() = face.let { f -> if (f.side) f.top + 2 - ((22 * f.pitch).toInt() + 6) else f.top + 2 - ((f.w / 2 + 7) / f.pitch).toInt() }
    private val chimneyX: Int get() = face.x + face.w / 2 + if (face.side) face.w / 4 else face.w / 5
    private val chimneyY: Int get() = if (face.side) apex - 6 else apex + ((chimneyX - face.x - face.w / 2) / face.pitch).toInt() - 2

    /** The gable end to the street: the roof's two edges, the boarded gable and what looks out of it. */
    private fun frontRoof(b: Buf) {
        val f = face
        val ax = f.x + f.w / 2
        val eave = f.top + 2
        val e = f.w / 2 + 9
        val ay = apex
        for (y in ay until eave) {
            val half = ((y - ay) * f.pitch).roundToInt() + 2
            for (x in ax - half until ax + half) roofPx(b, x, y, if (x < ax) .62 else .36, y - ay)
            b.p(ax - half - 1, y, R.INK); b.p(ax + half, y, R.INK)
        }
        if (winter) for (x in ax - e until ax + e) if (hash(x, 1) > .3) b.p(x, eave, R.snow[5])
        val (fr, acc) = frame()
        val band = if (f.hip) 18 else 10
        val gt = ay + band
        for (y in gt until f.top) {
            val half = ((y - gt) * f.pitch).roundToInt()
            for (x in ax - half until ax + half) b.p(x, y, gableBoard(x, y, ax))
        }
        if (f.hip) for (y in ay + 6 until gt) { val half = ((y - ay) * f.pitch).roundToInt() + 2; b.p(ax - half + 3, y, R.INK.lit(.1f)); b.p(ax + half - 4, y, R.INK.lit(.1f)) }
        if (f.carving > 0) for (y in ay + 4 until eave) {
            val half = ((y - ay) * f.pitch).roundToInt() + 2
            b.p(ax - half + 1, y, fr); b.p(ax + half - 2, y, fr.dim(.15f))
            if (y % 3 == 0) { b.p(ax - half + 2, y + 1, fr); b.p(ax + half - 3, y + 1, fr.dim(.15f)) }
        }
        if (f.carving > 0 && f.wall != Wall.PLANKS) b.spr(listOf("..kk....", ".kWWk...", "kWkWWk..", "...kWWk.", "....kWWk", "....kWWk"), ax - 4, ay - 6, mapOf('k' to R.INK, 'W' to fr))
        if (f.carving > 1) {
            valance(b, ax - e + 4, ax + e - 4, eave, fr)
            for (x in listOf(ax - 2, ax - e + 6, ax + e - 10)) towel(b, x, if (x == ax - 2) gt - 2 else eave - 2, fr, acc)
        }
        val gy = (gt + f.top) / 2 + 2
        gableThing(b, ax, gy, fr, acc)
        if (f.flag) { b.line(ax, ay - 22, ax, ay, rgb(0x2a2a30)); b.vol(ax + 1, ay - 22, 12, 7, { u, v -> u < 12 - (if (v == 3) 2 else 0) }, { u, v -> .6 - (if ((u + v) % 4 == 0) .15 else 0.0) }, R.red) }
        if (f.chimney) chimney(b, chimneyX, chimneyY)
    }

    /** The long side to the street: the whole roof slope, and maybe a little lookout gable on it. */
    private fun sideRoof(b: Buf) {
        val f = face
        val ax = f.x + f.w / 2
        val eave = f.top + 2
        val rh = (22 * f.pitch).toInt() + 6
        val ridge = apex
        val e = f.w / 2 + 8
        for (y in ridge until eave) {
            val t = (eave - y).toDouble() / rh
            val half = (e - t * (if (f.hip) 26 else 5)).roundToInt()
            for (x in ax - half until ax + half) roofPx(b, x, y, if (!f.hip) .62 - t * .1 else if (x < ax - e + 26) .5 else if (x >= ax + e - 26) .3 else .62 - t * .1, y - ridge)
            b.p(ax - half - 1, y, R.INK); b.p(ax + half, y, R.INK)
        }
        b.r(ax - e + (if (f.hip) 26 else 5), ridge - 1, 2 * e - 2 * (if (f.hip) 26 else 5), 1, R.INK)
        if (winter) for (x in ax - e until ax + e) if (hash(x, 1) > .3) b.p(x, eave, R.snow[5])
        val (fr, acc) = frame()
        if (f.carving > 0) valance(b, ax - e + 2, ax + e - 2, eave, fr)
        if (f.gable == Gable.LOOKOUT) {
            // a lookout gable in the middle of the roof
            val dw = 22
            val dt = eave - 18
            for (y in dt until eave) for (x in ax - dw / 2 until ax + dw / 2) b.p(x, y, gableBoard(x, y, ax))
            val ay = dt - 12
            for (y in ay until dt + 1) {
                val half = ((y - ay) * 1.1).roundToInt() + 1
                for (x in ax - half until ax + half) roofPx(b, x, y, if (x < ax) .62 else .36, y - ay)
                b.p(ax - half - 1, y, R.INK); b.p(ax + half, y, R.INK)
            }
            for (y in ay + 5 until dt) { val half = ((y - ay - 5) * 1.1).roundToInt(); for (x in ax - half until ax + half) b.p(x, y, gableBoard(x, y, ax)) }
            if (f.carving > 0) for (y in ay + 3 until dt + 1) { val half = ((y - ay) * 1.1).roundToInt() + 1; b.p(ax - half + 1, y, fr); b.p(ax + half - 2, y, fr.dim(.15f)) }
            lookout(b, ax, dt + 2, fr, acc)
        }
        if (f.chimney) chimney(b, chimneyX, chimneyY)
    }

    private fun gableBoard(x: Int, y: Int, ax: Int): Int {
        val f = face
        return if (f.wall == Wall.PLANKS) (if (f.paint2 != null && x >= ax) f.paint2 else f.paint).dim(.15f + if ((x - ax + 60) % 5 == 0) .3f else 0f)
        else rp(logs(), .5 + logTone() + (if (x < ax) .12 else 0.0) + (if ((x - ax + 60) % 4 == 0) -.15 else 0.0), x, y)
    }

    private fun gableThing(b: Buf, ax: Int, gy: Int, fr: Int, acc: Int) {
        when (face.gable) {
            Gable.ROUND -> {
                b.ball(ax, gy, 4, R.wood, rgb(0x1e100a))
                b.disc(ax, gy, 3, if (lit) rgb(0xf6d77a) else rgb(0x8aa0b0))
                b.r(ax, gy - 3, 1, 7, rgb(0x3a2214)); b.r(ax - 3, gy, 7, 1, rgb(0x3a2214))
            }
            Gable.LOOKOUT -> lookout(b, ax, gy - 6, fr, acc)
            Gable.STUDIO -> {
                // a painter's north light: a tall glazed panel up into the gable
                val y0 = gy - 12
                b.r(ax - 13, y0 - 1, 26, 28, fr)
                if (lit) b.vgrad(ax - 12, y0, 24, 26, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040)))
                else b.vgrad(ax - 12, y0, 24, 26, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
                for (i in 0..3) b.r(ax - 12 + i * 6, y0, 1, 26, fr)
                for (j in 0..3) b.r(ax - 12, y0 + j * 7, 24, 1, fr)
                for (j in 0 until 26) b.mul(ax - 4 - j / 3, y0 + j, rgb(0x404860), .25f)
            }
            Gable.ANTLERS -> {
                b.r(ax - 4, gy - 1, 9, 5, rgb(0x55331e)); b.r(ax - 3, gy, 7, 3, rgb(0x7c4e30))
                val bone = rgb(0xe8dcc0)
                for (s in listOf(-1, 1)) {
                    b.line(ax + s * 2, gy, ax + s * 9, gy - 8, bone); b.line(ax + s * 9, gy - 8, ax + s * 10, gy - 14, bone)
                    b.line(ax + s * 5, gy - 4, ax + s * 4, gy - 9, bone); b.line(ax + s * 8, gy - 7, ax + s * 13, gy - 9, bone)
                }
            }
            Gable.LOFT -> {
                b.r(ax - 8, gy - 8, 16, 16, rgb(0x1e100a))
                for (x in ax - 7 until ax + 7) for (y in gy - 7 until gy + 8) b.p(x, y, rp(R.woodG, .45 + (if ((x - ax + 7) % 4 == 0) -.15 else 0.0) + (if (x < ax) .08 else 0.0), x, y))
                b.r(ax, gy - 7, 1, 15, rgb(0x1e100a)); b.line(ax - 7, gy - 7, ax - 1, gy + 7, rgb(0x3a2a20)); b.line(ax + 6, gy - 7, ax + 1, gy + 7, rgb(0x3a2a20))
                b.r(ax - 2, gy - 14, 4, 4, rgb(0x3a2214)); b.line(ax + 1, gy - 11, ax + 1, gy - 2, rgb(0x8e857a))
            }
            Gable.VENT -> { b.r(ax - 4, gy - 3, 8, 7, rgb(0x1e100a)); for (j in 0 until 3) b.r(ax - 3, gy - 2 + j * 2, 6, 1, R.woodG[3]) }
            Gable.NONE -> Unit
        }
    }

    /** A little window in the attic with a rail under it. */
    private fun lookout(b: Buf, ax: Int, y: Int, fr: Int, acc: Int) {
        b.r(ax - 7, y - 1, 14, 15, fr)
        if (lit) b.vgrad(ax - 5, y + 1, 10, 11, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040)))
        else b.vgrad(ax - 5, y + 1, 10, 11, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
        b.r(ax, y + 1, 1, 11, fr); b.r(ax - 5, y + 5, 10, 1, fr)
        for (k in 0 until 3) b.p(ax - 2 + k * 2, y - 2, acc)
        b.r(ax - 9, y + 13, 18, 2, rgb(0x55331e))
        for (x in ax - 9 until ax + 9 step 3) b.r(x, y + 15, 1, 3, rgb(0x55331e))
        b.r(ax - 9, y + 18, 18, 1, rgb(0x3a2214))
        if (lit) b.glow(ax, y + 6, 14, rgb(0xffc860), .25f, 4)
    }

    /** Carved valance under the eaves: a row of little hanging scallops. */
    private fun valance(b: Buf, x0: Int, x1: Int, y: Int, fr: Int) {
        for (x in x0 until x1) {
            b.p(x, y, fr); b.p(x, y + 1, fr.dim(.25f))
            val k = (x - x0) % 6
            if (k in 1..4) b.p(x, y + 2, fr.dim(.1f))
            if (k in 2..3) b.p(x, y + 3, fr.dim(.15f))
            if (k == 0) b.p(x, y + 2, R.INK)
        }
    }

    /** A carved board hanging from the roof, the "towel" of northern houses. */
    private fun towel(b: Buf, x: Int, y: Int, fr: Int, acc: Int) {
        for (j in 0 until 16) for (i in 0 until 5) {
            val cut = (j % 4 == 3 && (i == 0 || i == 4)) || (j > 12 && (i == 0 || i == 4)) || (j == 15 && i != 2)
            if (!cut) b.p(x + i, y + j, if (i == 2 && j % 4 == 1) acc else if (i == 4) fr.dim(.25f) else fr)
        }
    }

    private fun chimney(b: Buf, x: Int, y: Int) {
        b.vol(x - 4, y, 8, 18, { _, _ -> true }, { u, v -> .6 - u * .05 + if (v % 3 == 0) -.15 else 0.0 }, R.brick, rgb(0x1a0806))
        b.r(x - 5, y - 1, 10, 2, rgb(0x2a0e0a))
        if (winter) b.r(x - 5, y - 2, 10, 1, R.snow[5])
    }

    /** A glazed veranda on the left: little panes, a sloping roof. */
    private fun veranda(b: Buf) {
        val f = face
        val x0 = f.x - 28
        val top = f.top + 16
        val (fr, _) = frame()
        for (y in top until 150) for (x in x0 until f.x) b.p(x, y, rp(R.wood, .55 + (if ((x - x0) % 5 == 0) -.15 else 0.0), x, y))
        for (r in 0 until 3) for (c in 0 until 4) {
            val x = x0 + 3 + c * 6
            val y = top + 6 + r * 7
            if (lit) b.vgrad(x, y, 5, 6, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040)))
            else b.vgrad(x, y, 5, 6, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
            b.mul(x + 1, y, rgb(0x404860), .2f)
        }
        for (c in 0..4) b.r(x0 + 2 + c * 6, top + 5, 1, 22, fr)
        for (r in 0..3) b.r(x0 + 2, top + 5 + r * 7, 25, 1, fr)
        for (y in top - 8 until top + 2) {
            val k = (y - (top - 8)) * 3
            for (x in maxOf(x0 - 3, f.x - k) until f.x + 1) roofPx(b, x, y, .55, y - top)
        }
        b.line(x0 - 3, top + 1, f.x, top - 8, R.INK)
        if (lit) b.glow(x0 + 14, top + 16, 26, rgb(0xffc860), .25f, 4)
    }

    /** A lean-to shed of grey boards on the right. */
    private fun shed(b: Buf) {
        val f = face
        val x0 = f.x + f.w - 2
        val top = f.top + 22
        for (y in top until 150) for (x in x0 until minOf(170, x0 + 26)) b.p(x, y, rp(R.woodG, .5 + (if ((x - x0) % 5 == 0) -.2 else 0.0) + (fbm(x * .3, y * .2) - .5) * .2, x, y))
        for (y in top - 6 until top + 1) for (x in x0 until minOf(170, x0 + 28)) if (y - (top - 6) >= (x - x0) / 5) roofPx(b, x, y, .45, y)
        b.r(x0 + 8, top + 10, 10, 18, rgb(0x2a2420)); b.r(x0 + 9, top + 11, 8, 17, rgb(0x3e3530)); b.p(x0 + 15, top + 19, R.brass[3])
    }

    /** The mill's water wheel, turning in its race on the right. */
    private fun wheel(b: Buf) {
        val cx = face.x + face.w + 14
        val cy = 116
        val r = 24
        for (a in 0 until 360 step 2) {
            val an = Math.toRadians(a.toDouble())
            for (k in 0..2) b.p(cx + (kotlin.math.cos(an) * (r - k)).roundToInt(), cy + (kotlin.math.sin(an) * (r - k)).roundToInt(), R.wood[if (k == 1) 4 else 2])
        }
        for (k in 0 until 8) {
            val an = k * Math.PI / 4
            b.line(cx, cy, cx + (kotlin.math.cos(an) * r).roundToInt(), cy + (kotlin.math.sin(an) * r).roundToInt(), R.wood[3])
        }
        for (k in 0 until 16) {
            val an = k * Math.PI / 8
            val x = cx + (kotlin.math.cos(an) * (r + 2)).roundToInt()
            val y = cy + (kotlin.math.sin(an) * (r + 2)).roundToInt()
            b.r(x - 1, y - 1, 3, 3, R.wood[1])
        }
        b.ball(cx, cy, 3, R.iron, R.INK)
        // the race bringing water over the top
        for (y in 82 until 88) for (x in cx - 4 until 170) b.p(x, y, if (y < 84) R.wood[2] else rp(R.water, .7, x, y))
        if (!winter) for (j in 0 until 14) b.p(cx - 3 + (j % 3), 88 + j, R.water[5 - j % 3])
    }

    private fun porch(b: Buf, fr: Int) {
        val f = face
        val x0 = f.x + f.w - 4
        val top = f.top + 12
        // the door under a little gabled canopy
        b.r(x0 - 14, top + 10, 14, 140 - top, rgb(0x3a2214))
        for (x in x0 - 13 until x0 - 1) for (y in top + 11 until 150) b.p(x, y, rp(R.wood, .45 + (if ((x - x0) % 4 == 0) -.15 else 0.0), x, y))
        b.p(x0 - 4, top + 34, R.brass[4])
        for (s in listOf(x0 - 17, x0 + 3)) b.vol(s, top + 6, 3, 150 - top - 6, { _, _ -> true }, { u, _ -> .6 - u * .12 }, R.wood, R.INK)
        for (y in top - 6 until top + 6) {
            val half = (y - (top - 6)) + 2
            for (x in x0 - 7 - half until x0 - 7 + half) roofPx(b, x, y, if (x < x0 - 7) .62 else .36, y - top)
            b.p(x0 - 8 - half, y, R.INK); b.p(x0 - 7 + half, y, R.INK)
        }
        for (x in x0 - 18 until x0 + 5) b.p(x, top + 6, fr)
        for (k in 0 until 3) b.r(x0 - 18 + k, 140 + k * 3, 24 - 2 * k, 3, rp(R.wood, .6 - k * .1, x0, 140))
    }

    /** The shop's display window with its goods, and an awning. */
    private fun shopfront(b: Buf) {
        val f = face
        val x0 = f.x + f.w - 50
        val y0 = f.top + 20
        b.r(x0 - 2, y0 - 2, 46, 34, rgb(0xe8e2d4))
        if (lit) b.vgrad(x0, y0, 42, 30, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040)))
        else b.vgrad(x0, y0, 42, 30, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
        b.r(x0, y0 + 18, 42, 2, rgb(0x8e5a34))
        for (k in 0 until 6) { Props.jar(b, x0 + 2 + k * 7, y0 + 18, listOf(R.jam, R.honey, R.apple)[k % 3], w = 6, h = 8) }
        for (k in 0 until 5) b.ball(x0 + 6 + k * 8, y0 + 27, 2, if (k % 2 == 0) R.apple else R.honey)
        b.r(x0 + 20, y0, 2, 30, rgb(0xe8e2d4))
        for (i in 0 until 46) for (j in 0 until 6) b.p(x0 - 2 + i, y0 - 9 + j, if ((i / 5) % 2 == 0) rgb(0xc04a3a) else rgb(0xf2ece0))
        for (i in 0 until 46 step 5) b.r(x0 - 2 + i, y0 - 3, 3, 1, rgb(0xc04a3a))
        if (lit) b.glow(x0 + 21, y0 + 14, 34, rgb(0xffc860), .3f, 5)
    }

    /** The club's columned porch with a pediment, in the middle of the front. */
    private fun portico(b: Buf) {
        val f = face
        val cx = f.x + f.w / 2
        val y0 = f.top + 16
        for (y in y0 - 10 until y0 + 1) { val half = (y - (y0 - 10)) * 2 + 2; for (x in cx - half until cx + half) b.p(x, y, rp(R.cream, .7 - (if (x > cx) .15 else 0.0), x, y)); b.p(cx - half - 1, y, R.INK); b.p(cx + half, y, R.INK) }
        b.r(cx - 23, y0, 46, 3, R.cream[2])
        for (k in 0 until 4) b.vol(cx - 21 + k * 12, y0 + 3, 6, 150 - y0 - 3, { _, _ -> true }, { u, _ -> .9 - u * .12 }, R.cream, rgb(0x6a5a42))
        b.r(cx - 6, y0 + 14, 12, 150 - y0 - 14, rgb(0x55331e)); b.r(cx, y0 + 14, 1, 150 - y0 - 14, rgb(0x3a2214))
        b.ball(cx - 2, y0 + 30, 1, R.brass); b.ball(cx + 2, y0 + 30, 1, R.brass)
    }

    private fun window(b: Buf, x: Int, y: Int, gw: Int, fr: Int, acc: Int) {
        val f = face
        val gh = if (f.trim == Trim.TALL) 32 else 28
        val y = if (f.trim == Trim.TALL) y - 4 else y
        if (lit) b.glow(x + gw / 2, y + 14, 34, rgb(0xffc860), .32f, 5)
        f.shutters?.let { sh ->
            for (s in listOf(x - 4 - gw / 2, x + gw + 4)) {
                for (yy in y - 1 until y + gh + 1) for (xx in s until s + gw / 2) b.p(xx, yy, sh.dim(if ((xx - s) % 3 == 0) .25f else ((xx - s) / gw.toFloat()) * .2f))
                b.r(s, y - 1, gw / 2, 1, sh.lit(.25f)); b.r(s, y + gh / 2, gw / 2, 1, sh.dim(.35f))
                b.disc(s + gw / 4, y + gh / 4, 1, fr); b.disc(s + gw / 4, y + gh * 3 / 4, 1, fr)
            }
        }
        when (f.trim) {
            Trim.CARVED -> {
                b.r(x - 3, y - 8, gw + 6, 8, fr)
                for (i in 0 until gw + 6 step 3) { b.p(x - 3 + i, y - 9, fr); b.p(x - 2 + i, y - 10, fr) }
                b.r(x + gw / 2 - 4, y - 12, 8, 4, fr); b.r(x, y - 6, gw, 2, acc); b.p(x + gw / 2, y - 11, acc)
                b.r(x - 3, y, 3, gh, fr); b.r(x + gw, y, 3, gh, fr)
                for (j in 2 until gh step 4) { b.p(x - 2, y + j, acc); b.p(x + gw + 1, y + j, acc) }
            }
            Trim.ARCHED -> {
                for (i in -3 until gw + 3) { val d = (i - gw / 2.0) / (gw / 2.0 + 3); val h = (kotlin.math.sqrt(maxOf(0.0, 1 - d * d)) * 7).roundToInt(); for (j in 0..h) b.p(x + i, y - j, fr) }
                for (i in 0 until gw) { val d = (i + .5 - gw / 2.0) / (gw / 2.0); val h = (kotlin.math.sqrt(maxOf(0.0, 1 - d * d)) * 4).roundToInt(); for (j in 1..h) b.p(x + i, y - j, if (lit) rgb(0xf8d070) else Air.skyRamp(e).first()) }
                b.r(x - 3, y, 3, gh, fr); b.r(x + gw, y, 3, gh, fr)
            }
            Trim.PLAIN, Trim.TALL -> {
                b.r(x - 2, y - 2, gw + 4, 2, fr); b.r(x - 2, y, 2, gh, fr); b.r(x + gw, y, 2, gh, fr)
                if (f.trim == Trim.TALL) { b.r(x - 4, y - 5, gw + 8, 3, fr.dim(.1f)); b.r(x - 4, y - 5, gw + 8, 1, fr.lit(.2f)) }
            }
        }
        b.r(x - 5, y + gh, gw + 10, 3, fr); b.r(x - 3, y + gh + 3, gw + 6, 2, fr.dim(.18f))
        if (winter) b.r(x - 5, y + gh - 1, gw + 10, 1, R.snow[5])
        if (lit) b.vgrad(x, y, gw, gh, intArrayOf(rgb(0xfff0b0), rgb(0xf8d070), rgb(0xeab040), rgb(0xd08c24)))
        else {
            b.vgrad(x, y, gw, gh, Air.skyRamp(e).let { it.copyOfRange(0, minOf(4, it.size)) })
            for (j in 0 until gh) b.mul(x + gw / 2 - 1 - (j % 3), y + j, rgb(0x404860), .3f)
        }
        // curtains, unless it's a town-style tall window
        if (f.trim != Trim.TALL) for (j in 0 until 20) {
            val w1 = (gw * 3 / 10 - j / 4).coerceAtLeast(0)
            for (i in 0 until w1) {
                val c = if ((i + j) % 2 == 0) rgb(0xfbf6ea) else rgb(0xe8dcc4)
                b.p(x + i, y + j, c); b.p(x + gw - 1 - i, y + j, c)
            }
        }
        b.r(x + gw / 2 - 1, y, 2, gh, rgb(0x55331e)); b.r(x, y + gh * 3 / 7, gw, 2, rgb(0x55331e))
        if (f.trim == Trim.TALL) b.r(x, y + gh * 3 / 4, gw, 1, rgb(0x55331e))
        // pot plants on the sill inside
        b.vol(x + 2, y + gh - 6, 6, 6, { u, v -> v > 2 || abs(u - 3) < 2 }, { _, _ -> .5 }, R.brick)
        for (k in 0 until 8) b.p(x + 2 + (hash(k, x) * 6).toInt(), y + gh - 11 + (hash(x, k) * 5).toInt(), if (k % 3 == 0) rgb(0xc01e2a) else rgb(0x2a4a2a))
        if (gw >= 18) {
            b.vol(x + gw - 7, y + gh - 5, 5, 5, { _, _ -> true }, { _, _ -> .5 }, R.brick)
            for (k in 0 until 6) b.p(x + gw - 7 + (hash(k, y) * 5).toInt(), y + gh - 9 + (hash(y, k) * 4).toInt(), if (k % 2 == 0) rgb(0x3a5a32) else rgb(0xe8d8f0))
        }
        if (e.has(Look.NEWYEAR)) for (k in 0 until gw / 4) b.p(x + 2 + k * 4, y + 2 + (k % 2), intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[k % 3])
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
        if ("well" in ps) well(b)
        if ("hives" in ps) for (k in 0 until 3) {
            // on little legs in the grass in front of the fence
            val x = 4 + k * 18
            for (l in listOf(x + 2, x + 10)) b.r(l, 162, 2, 8, rgb(0x3a2214))
            b.vol(x, 148, 14, 14, { _, _ -> true }, { u, v -> .7 - u * .03 - if (v % 4 == 0) .15 else 0.0 }, R.honey, rgb(0x3a1a04))
            b.r(x - 2, 145, 18, 3, if (winter) R.snow[5] else rgb(0x8e3a24))
            b.r(x + 5, 158, 4, 1, rgb(0x2a1206))
            for (i in -8..8) b.mul(x + 7 + i, 170, rgb(0x303040), .3f)
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
        if (e.has(Look.NEWYEAR) && !town) for (x in face.x until face.x + face.w step 6) b.p(x, face.top + 2 + (x / 6) % 2, intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[(x / 6) % 3])
    }

    /** A sweep well: a log frame standing in the grass, the post and the long beam with the bucket on a rope. */
    private fun well(b: Buf) {
        val ground = 174
        for (i in -12..14) b.mul(12 + i, ground, rgb(0x303040), .35f)
        // the post and the beam, behind the frame
        b.vol(28, 104, 4, ground - 104, { _, _ -> true }, { u, _ -> .6 - u * .1 }, R.woodG, R.INK)
        b.line(8, 96, 54, 116, rgb(0x55331e)); b.line(8, 97, 54, 117, rgb(0x3a2214))
        b.vol(50, 113, 7, 6, { _, _ -> true }, { u, v -> .55 - u * .05 - v * .04 }, R.stone, R.INK)
        b.line(9, 98, 9, 146, rgb(0x8e857a))
        b.vol(6, 146, 7, 6, { u, v -> u >= v / 3 && u < 7 - v / 3 }, { u, _ -> .6 - u * .06 }, R.iron, R.INK)
        // the log frame
        val top = ground - 18
        for (r in 0 until 6) for (x in 0 until 24) b.p(x, top + r * 3, R.INK)
        for (r in 0 until 6) b.vol(0, top + r * 3, 24, 3, { _, _ -> true }, { u, v -> .7 - v * .18 - u * .012 }, R.wood)
        for (r in 0 until 6) for (x in listOf(-2, 23)) b.vol(x, top + r * 3, 3, 3, ell(1.5, 1.5, 1.5, 1.5), sph(1.0, 1.0, 1.5, 1.5, .3), R.wood, rgb(0x1e100a))
        b.r(1, top - 1, 22, 1, if (winter) R.snow[5] else R.wood[1])
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
        if (!town && face.chimney) Props.smoke(b, chimneyX, chimneyY - 2, t, 9, 34, if (e.phase.dark) rgb(0x6a6a80) else rgb(0xb8a8b8), .5f, if (e.temp < -10) .05 else .5)
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
