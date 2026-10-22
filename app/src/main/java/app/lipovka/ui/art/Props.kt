package app.lipovka.ui.art

import app.lipovka.domain.Leaves
import kotlin.math.PI
import kotlin.math.abs
import kotlin.math.ceil
import kotlin.math.hypot
import kotlin.math.max
import kotlin.math.min
import kotlin.math.roundToInt
import kotlin.math.sin
import kotlin.math.sqrt

/** Things that appear in many scenes: the kettle, the cat, cups and jars, trees, smoke. */
object Props {
    private val LV = doubleArrayOf(-.48, -.66, .58).let { v -> val l = sqrt(v.sumOf { it * it }); DoubleArray(3) { v[it] / l } }

    /** The green enamel kettle with white dots, [s] its scale (1 = 36×30). */
    fun kettle(b: Buf, x: Int, y: Int, s: Double = 1.0) {
        fun hw(v: Double): Double {
            var w = 6.5 + 6.5 * sin(min(1.0, (v - 8) / 18) * PI / 2)
            if (v > 26) w -= (v - 26) * 1.4
            return w
        }
        val w = ceil(36 * s).toInt()
        val h = ceil(30 * s).toInt()
        val ink = rgb(0x0b0807)
        val enOl = rgb(0x0a1610)
        // handle
        b.vol(x, y, w, h, { u, v ->
            val uu = u / s
            val vv = v / s
            val d = hypot((uu + .5 - 14) / 10, (vv + .5 - 10) / 9)
            vv < 10 && d > .82 && d <= 1
        }, { _, v -> .3 + .5 * (1 - v / (10 * s)) }, R.iron, ink)
        for (v in 0 until h) for (u in 0 until w) {
            val uu = u / s
            val vv = v / s
            val d = hypot((uu + .5 - 14) / 10, (vv + .5 - 10) / 9)
            if (vv < 10 && d > .82 && d <= 1 && abs(uu - 14) < 4.5) b.p(x + u, y + v, rp(R.wood, .65 - vv / 24, x + u, y + v))
        }
        // spout
        b.vol(x, y, w, h, { u, v ->
            val uu = u / s
            val vv = v / s
            if (uu < 22 || uu > 33.5) false else {
                val c = 23 - (uu - 22) * 1.05
                val t = 3.2 - (uu - 22) * .16
                abs(vv + .5 - c) <= t
            }
        }, { u, v -> .35 + .5 * ((u / s - 22) / 12) * (1 - (v / s) / 30) }, R.enamel, enOl)
        // body
        val bm = { u: Int, v: Int -> val uu = u / s; val vv = v / s; vv >= 8 && vv <= 28 && abs(uu + .5 - 14) <= hw(vv) }
        b.vol(x, y, w, h, bm, { u, v ->
            val uu = u / s
            val vv = v / s
            val ww = hw(vv)
            val nx = (uu + .5 - 14) / ww
            val ny = (vv - 17) / 16
            val nz = sqrt(max(0.0, 1 - nx * nx * .95))
            val d = nx * LV[0] + ny * LV[1] * .6 + nz * LV[2]
            .12 + .8 * max(0.0, d) + if (d > .9) .25 else 0.0
        }, R.enamel, enOl)
        for (v in 0 until h) for (u in 0 until w) {
            val vv = v / s
            if (bm(u, v) && vv > 26.2) b.p(x + u, y + v, R.enamel[0])
            if (bm(u, v) && vv > 8 && vv < 9.6) b.p(x + u, y + v, R.enamel[1])
        }
        val dots = listOf(9 to 13, 16 to 12, 21 to 17, 6 to 19, 13 to 18, 19 to 23, 24 to 22, 9 to 24, 15 to 26, 4 to 25, 12 to 10)
        val shade = sph(14.0, 17.0, 13.0, 11.0)
        for ((u, v) in dots) {
            val pu = (u * s).toInt()
            val pv = (v * s).toInt()
            if (!bm(pu, pv)) continue
            val l = shade(u, v)
            val c = when {
                l > .62 -> rgb(0xfffbf0)
                l > .38 -> rgb(0xe6dcc4)
                else -> rgb(0xa89c84)
            }
            b.p(x + pu, y + pv, c)
            if (s >= .9) { b.p(x + pu + 1, y + pv, c); b.p(x + pu, y + pv + 1, if (l > .5) c else rgb(0x8a8070)) }
        }
        // lid and knob
        b.vol(x, y, w, h, { u, v -> val a = (u / s + .5 - 14) / 7.5; val c = (v / s + .5 - 8) / 2.2; a * a + c * c <= 1 },
            { u, _ -> .55 - ((u / s) - 14) / 18 }, R.enamel, enOl)
        b.ball((x + 14 * s).roundToInt(), (y + 5 * s).roundToInt(), max(1, (2 * s).roundToInt()), R.iron, ink)
    }

    /** The sleeping ginger cat, curled up; [br] 0..1 is its breath. 48×28. */
    fun cat(b: Buf, x: Int, y: Int, br: Double = 0.0, pal: IntArray = R.ginger, ol: Int = rgb(0x2e1206)) {
        val tail = listOf(44.0 to 17.0, 45.0 to 21.0, 42.0 to 24.5, 36.0 to 26.0, 28.0 to 26.5, 20.0 to 26.0, 14.0 to 24.5)
        val body = ell(26.0, 15.5 - br * .5, 18.0, 9.5 + br * .6)
        val sh = sph(24.0, 12.0, 19.0, 11.0, .2, .12)
        b.vol(x, y, 48, 28, { u, v -> v <= 25 && body(u, v) }, { u, v ->
            var l = sh(u, v)
            if (sin(u * .55 + v * .25) > .55 && u > 12) l -= .16
            l
        }, pal, ol)
        for (t in 0 until tail.size - 1) for (k in 0..6) {
            val (ax, ay) = tail[t]
            val (cx, cy) = tail[t + 1]
            val px = ax + (cx - ax) * k / 6
            val py = ay + (cy - ay) * k / 6
            val ix = (x + px).roundToInt()
            val iy = (y + py).roundToInt()
            b.disc(ix, iy, 2, rp(pal, .42 - t * .03 + (if ((t + k) % 5 == 0) -.15 else 0.0), ix, iy))
        }
        for (t in 0 until tail.size - 1) b.p((x + tail[t].first).toInt(), (y + tail[t].second + 3).toInt(), ol)
        b.vol(x + 13, y + 20, 8, 5, ell(4.0, 2.5, 4.0, 2.5), sph(4.0, 2.0, 4.0, 2.5, .4), R.cream, ol)
        val hs = sph(9.0, 13.0, 9.0, 8.0, .22, .18)
        b.vol(x, y, 22, 26, ell(10.5, 15.5, 8.5, 7.5), { u, v ->
            var l = hs(u, v)
            if (v < 12 && (u == 8 || u == 11 || u == 10)) l -= .18
            l
        }, pal, ol)
        ear(b, x, y, 3, 10, 6, 4, 9, 9, pal)
        ear(b, x, y, 11, 8, 14, 4, 17, 10, pal)
        b.vol(x + 6, y + 16, 10, 5, ell(5.0, 2.5, 4.5, 2.5), sph(4.0, 1.5, 5.0, 3.0, .45), R.cream)
        for ((u, v) in listOf(5 to 15, 6 to 16, 7 to 16, 13 to 15, 12 to 16, 11 to 16)) b.p(x + u, y + v, rgb(0x3a1608))
        b.p(x + 9, y + 17, rgb(0xd8707a)); b.p(x + 10, y + 17, rgb(0xd8707a)); b.p(x + 9, y + 18, rgb(0x8a3a3a))
        for ((u, v) in listOf(2 to 18, 1 to 19, 3 to 20, 17 to 18, 18 to 19)) b.p(x + u, y + v, rgb(0xfff6e0), .8f)
    }

    private fun ear(b: Buf, x: Int, y: Int, ax: Int, ay: Int, cx: Int, cy: Int, ex: Int, ey: Int, pal: IntArray) {
        for (v in 3 until 12) for (u in 2 until 19) {
            val s1 = (cx - ax) * (v - ay) - (cy - ay) * (u - ax)
            val s2 = (ex - cx) * (v - cy) - (ey - cy) * (u - cx)
            val s3 = (ax - ex) * (v - ey) - (ay - ey) * (u - ex)
            if ((s1 <= 0 && s2 <= 0 && s3 <= 0) || (s1 >= 0 && s2 >= 0 && s3 >= 0)) {
                b.p(x + u, y + v, if (v > 7 && abs(u - cx) < 1.6) rgb(0xe08a80) else rp(pal, .55, x + u, y + v))
            }
        }
    }

    /** A cup on a saucer, 13×15. */
    fun cup(b: Buf, x: Int, y: Int, blue: Int = rgb(0x2c4c8a)) {
        val ol = rgb(0x4a3a2a)
        b.vol(x - 3, y + 11, 20, 4, ell(10.0, 2.0, 10.0, 2.0), { _, v -> .75 - v * .12 }, R.cream, ol)
        b.vol(x + 11, y + 2, 6, 8, { u, v -> val d = hypot((u + .5 - 1) / 4.5, (v + .5 - 4) / 3.6); d <= 1 && d > .5 }, { _, _ -> .4 }, R.cream, ol)
        b.vol(x, y, 13, 12, { u, v -> v >= 1 && (v < 11 || abs(u - 6) < 5) }, { u, _ ->
            val nx = (u + .5 - 6.5) / 6.5
            .2 + .75 * max(0.0, -nx * LV[0] * 1.4 + .55)
        }, R.cream, ol)
        for (u in 1 until 12) b.p(x + u, y + 2, blue)
        b.p(x + 5, y + 6, blue); b.p(x + 4, y + 7, blue); b.p(x + 6, y + 7, blue); b.p(x + 5, y + 8, blue); b.p(x + 5, y + 7, rgb(0xe8b443))
        for (u in 1 until 12) b.p(x + u, y + 1, if (u < 3) rgb(0xa0581e) else rgb(0x7a3a12))
        b.p(x + 4, y + 1, rgb(0xc07a3a))
    }

    /** A jar with a cloth lid tied with string. */
    fun jar(b: Buf, x: Int, y: Int, ramp: IntArray, cloth: Int = rgb(0xa33a2c), w: Int = 9, h: Int = 12) {
        b.vol(x, y + 2, w, h - 2, { u, v -> !(v == h - 3 && (u == 0 || u == w - 1)) }, { u, v ->
            val nx = (u + .5 - w / 2.0) / (w / 2.0)
            .25 + .6 * max(0.0, -nx * .7 + .4) + if (u == 2 && v > 1 && v < h - 5) .35 else 0.0
        }, ramp, rgb(0x1a0a08))
        b.r(x + 1, y + 5, w - 2, 4, rgb(0xf2e2bb))
        b.r(x + 2, y + 6, w - 4, 1, rgb(0xa08060))
        b.r(x + 2, y + 7, w - 5, 1, rgb(0xa08060))
        for (u in -1..w) {
            b.p(x + u, y + 1, if (u % 2 != 0) cloth else rgb(0xf2e2bb))
            b.p(x + u, y + 2, if (u % 2 != 0) rgb(0xf2e2bb) else cloth)
        }
        b.p(x - 1, y + 3, cloth); b.p(x + w, y + 3, cloth); b.r(x, y + 3, w, 1, rgb(0xc4a272)); b.p(x + w / 2, y, cloth)
    }

    fun envelope(b: Buf, x: Int, y: Int, w: Int = 12, h: Int = 8, c: Int = rgb(0xf8eed4), seal: Int = rgb(0xa33a2c)) {
        b.r(x, y, w, h, rgb(0x3a2a1a))
        b.r(x + 1, y + 1, w - 2, h - 2, c)
        for (i in 1 until w / 2) {
            val yy = y + min(h - 2, ((i * (h - 2)).toDouble() / (w / 2)).roundToInt())
            b.p(x + i, yy, rgb(0xb4a282))
            b.p(x + w - 1 - i, yy, rgb(0xb4a282))
        }
        b.p(x + w / 2, y + h / 2 + 1, seal); b.p(x + w / 2 - 1, y + h / 2 + 1, seal)
    }

    /** A spruce; [snow] dusts the tops of the boughs. */
    fun spruce(b: Buf, x: Int, y: Int, hgt: Int, pal: IntArray = R.green, shade: Double = 0.0, snow: Boolean = false) {
        val w = (hgt * .62).roundToInt()
        b.r(x + w / 2, y + hgt - 2, 1, 3, rgb(0x3a2214))
        val tier = max(3, (hgt / 5.0).roundToInt())
        for (v in 0 until hgt - 1) {
            val layer = v % tier
            val half = (v.toDouble() / (hgt - 1)) * w / 2 * (.65 + .35 * layer / tier)
            val hr = half.roundToInt()
            for (u in -hr..hr) {
                val l = .55 - u / (half + 1) * .35 - v.toDouble() / hgt * .15 - shade + (if (layer == 0) -.12 else 0.0) + hash(x + u, y + v) * .12
                val c = if (snow && layer <= 1 && hash(x + u * 3, y + v) > .3) rp(R.snow, .5 + l * .4, x + u, y + v) else rp(pal, l, x + u, y + v)
                b.p(x + w / 2 + u, y + v, c)
            }
        }
    }

    /** A birch whose crown follows the season. */
    fun birch(b: Buf, x: Int, y: Int, hgt: Int, leaves: Leaves, alt: Boolean = false) {
        b.r(x, (y + hgt * .35).toInt(), 2, (hgt * .65).toInt() + 1, rgb(0xf2ece0))
        var j = (hgt * .4).toInt()
        while (j < hgt) { b.p(x + (j % 2), y + j, rgb(0x2a2420)); j += 3 }
        b.p(x + 1, y + hgt - 1, rgb(0xc4b8a8))
        val (ramp, density) = when (leaves) {
            Leaves.BARE -> null to 0.0
            Leaves.BUDS -> R.grassSpring to .35
            Leaves.BLOSSOM, Leaves.GREEN -> R.grassSummer to 1.0
            Leaves.GOLD -> (if (alt) R.honey else R.gold) to 1.0
            Leaves.FALLING -> (if (alt) R.autumn else R.gold) to .55
        }
        if (ramp == null) {
            // bare twigs
            for (k in 0 until 6) {
                val a = -PI / 2 + (hash(x, k) - .5) * 2.2
                val l = hgt * (.25 + hash(k, y) * .2)
                b.line((x + 1).toDouble(), y + hgt * .45, x + 1 + kotlin.math.cos(a) * l, y + hgt * .45 + sin(a) * l, rgb(0x5a4a40))
            }
            return
        }
        for (k in 0 until 5) {
            val cx = x + 1 + ((hash(x + k, y) - .5) * hgt * .5).roundToInt()
            val cy = y + (hgt * (.12 + .32 * hash(y, x + k))).roundToInt()
            val r = (hgt * .17 + hash(k, x) * 2).roundToInt()
            for (jj in -r..r) for (i in -r..r) {
                if (i * i + jj * jj > r * r) continue
                if (hash(cx + i, cy + jj) > .86 * density + (1 - density) * .3) continue
                val l = .6 - (i + jj) / (2.6 * r) * .5 + hash(cx + i * 3, cy + jj) * .15
                b.p(cx + i, cy + jj, rp(ramp, l, cx + i, cy + jj))
            }
        }
    }

    /** A leafy tree (apple, rowan) with fruit when it's the season. */
    fun leafy(b: Buf, x: Int, y: Int, r: Int, leaves: Leaves, fruit: Int? = null) {
        b.r(x, y, 2, 5, rgb(0x3a2214))
        val ramp = when (leaves) {
            Leaves.BARE -> null
            Leaves.BUDS -> R.grassSpring
            Leaves.BLOSSOM -> R.blossom
            Leaves.GREEN -> R.green
            Leaves.GOLD -> R.gold
            Leaves.FALLING -> R.autumn
        }
        if (ramp == null) {
            for (k in 0 until 5) {
                val a = -PI / 2 + (k - 2) * .45
                b.line((x + 1).toDouble(), y.toDouble(), x + 1 + kotlin.math.cos(a) * r, y + sin(a) * r, rgb(0x4a3a30))
            }
            return
        }
        val sparse = if (leaves == Leaves.FALLING || leaves == Leaves.BUDS) .55 else .92
        for (j in -r..r) for (i in -r..r) {
            if (i * i + j * j > r * r || hash(x + i, y + j) > sparse) continue
            b.p(x + i, y - r + j, rp(ramp, .6 - (i + j) / (2.0 * r) * .4 + hash(i, j) * .15, x + i, y + j))
        }
        if (fruit != null && (leaves == Leaves.GREEN || leaves == Leaves.GOLD || leaves == Leaves.FALLING)) {
            for (k in 0 until 6) {
                val a = hash(x, k) * 6.28
                val d = hash(k, y) * r * .8
                b.p((x + kotlin.math.cos(a) * d).roundToInt(), (y - r + sin(a) * d).roundToInt(), fruit)
            }
        }
    }

    /** Rising smoke or steam: a few soft puffs drifting with the wind. */
    fun smoke(b: Buf, x: Int, y: Int, t: Int, n: Int = 6, len: Int = 24, c: Int = rgb(0xc8c0b8), a: Float = .55f, drift: Double = .35) {
        for (i in 0 until n) {
            val ph = (t * .6 + i * len.toDouble() / n) % len
            val yy = (y - ph).roundToInt()
            val xx = (x + sin(t * .25 + i * 1.7) * 1.2 + ph * drift).roundToInt()
            val al = (a * (1 - ph / len)).toFloat()
            b.p(xx, yy, c, al)
            b.p(xx + 1, yy, c, al * .8f)
            if (ph > len * .35) { b.p(xx, yy - 1, c, al * .7f); b.p(xx + 1, yy - 1, c, al * .6f); b.p(xx + 2, yy, c, al * .5f) }
        }
    }

    fun steam(b: Buf, x: Int, y: Int, t: Int, n: Int = 5, len: Int = 16, a: Float = .7f) = smoke(b, x, y, t, n, len, rgb(0xfffaf0), a, .2)

    /** A fence of pickets between x0 and x1, tops at y, h tall. */
    fun fence(b: Buf, x0: Int, x1: Int, y: Int, h: Int, snow: Boolean) {
        var x = x0
        while (x < x1) {
            for (yy in y until y + h) for (i in 0 until 4) b.p(x + i, yy, rp(R.woodG, .65 - i * .12 + (fbm(x.toDouble(), yy * .3) - .5) * .2, x + i, yy))
            b.p(x + 1, y - 1, R.woodG[4]); b.p(x + 2, y - 1, R.woodG[3])
            if (snow) { b.p(x + 1, y - 2, R.snow[5]); b.p(x + 2, y - 2, R.snow[4]); b.r(x, y - 1, 4, 1, R.snow[5]) }
            b.r(x, y + h, 4, 1, rgb(0x1a1410))
            x += 6
        }
        for (ry in listOf(y + 6, y + h - 8)) for (yy in ry until ry + 3) for (xx in x0 until x1) b.p(xx, yy, rp(R.woodG, .6 - (yy - ry) * .25, xx, yy))
    }
}
