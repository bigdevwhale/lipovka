package app.lipovka.ui.art

import kotlin.math.PI
import kotlin.math.abs
import kotlin.math.cos
import kotlin.math.roundToInt
import kotlin.math.sin

/** Postage stamps: a perforated paper edge, a little picture, the face value. 34×40. */
object StampArt {
    const val W = 34
    const val H = 40

    private fun bg(name: String): IntArray = when (name) {
        "sky" -> R.morning.copyOfRange(0, 5)
        "dusk" -> R.dusk.copyOfRange(3, 9)
        "night" -> R.night.copyOfRange(1, 6)
        "red" -> R.red.copyOfRange(2, 6)
        "green" -> R.green.copyOfRange(3, 8)
        "blue" -> R.blue.copyOfRange(2, 6)
        "gold" -> R.gold.copyOfRange(2, 6)
        "cream" -> R.paper.copyOfRange(2, 6)
        "violet" -> R.violet.copyOfRange(2, 6)
        "sea" -> R.water.copyOfRange(2, 7)
        else -> R.morning
    }

    fun draw(family: String, bgName: String, value: Int, empty: Boolean = false): Buf {
        val b = Buf(W, H)
        b.r(0, 0, W, H, if (empty) rgb(0xd9c290) else rgb(0xfbf3dc))
        if (empty) {
            b.r(3, 3, W - 6, H - 6, rgb(0xcdb27c))
            for ((x, y) in listOf(14 to 12, 15 to 11, 16 to 11, 17 to 11, 18 to 12, 18 to 13, 17 to 14, 16 to 15, 16 to 16, 16 to 19)) { b.p(x, y, rgb(0xa88a58)); b.p(x + 1, y, rgb(0xa88a58)) }
        } else {
            val pic = Buf(28, 30)
            pic.vgrad(0, 0, 28, 30, bg(bgName))
            picture(pic, family, bgName)
            for (y in 0 until 30) for (x in 0 until 28) b.d[(y + 3) * W + x + 3] = pic.d[y * 28 + x] or (0xFF shl 24)
            b.r(3, 34, 28, 4, rgb(0xfbf3dc))
            b.digits(value.coerceIn(1, 99).toString(), 4, 34, rgb(0x842a24))
            b.r(W - 13, 36, 10, 1, rgb(0x8e857a))
        }
        for (i in 1 until W step 3) { b.d[i] = 0; b.d[(H - 1) * W + i] = 0 }
        for (j in 1 until H step 3) { b.d[j * W] = 0; b.d[j * W + W - 1] = 0 }
        return b
    }

    private fun picture(b: Buf, f: String, bgName: String) {
        val ink = R.INK
        val light = rgb(0xfbf3dc)
        val darkBg = bgName in setOf("night", "blue", "violet", "red", "green", "sea", "dusk")
        val fg = if (darkBg) light else rgb(0x2a2a30)
        fun ground(c: Int = rgb(0x426442)) = b.r(0, 24, 28, 6, c)
        fun water() { for (y in 22 until 30) for (x in 0 until 28) b.p(x, y, rp(R.water, .3 + (y - 22) / 14.0 + if ((x + y) % 5 == 0) .2 else 0.0, x, y)) }
        when (f) {
            "house" -> { ground(); b.r(8, 15, 12, 9, rgb(0xc89a6a)); for (v in 0 until 6) b.r(14 - v - 1, 9 + v, 2 + v * 2, 1, rgb(0xa83e28)); b.r(10, 17, 3, 3, rgb(0xf6d77a)); b.r(15, 18, 3, 6, rgb(0x3a2214)) }
            "mill" -> { water(); b.r(10, 10, 12, 12, rgb(0xc89a6a)); for (v in 0 until 5) b.r(16 - v - 1, 5 + v, 2 + v * 2, 1, rgb(0x9a722e)); b.disc(8, 20, 5, rgb(0x3a2214)); b.disc(8, 20, 3, rgb(0x6694a0)); for (q in 0 until 6) { val a = q * PI / 3; b.line(8.0, 20.0, 8 + cos(a) * 5, 20 + sin(a) * 5, rgb(0x8e5a34)) } }
            "ship" -> { water(); b.disc(22, 6, 3, rgb(0xf8d070)); b.vol(4, 18, 20, 5, { u, v -> u > v && u < 20 - v }, { _, _ -> .6 }, R.red, ink); b.r(9, 12, 10, 6, light); b.r(12, 8, 3, 4, rgb(0x2a2a30)) }
            "boat" -> { water(); b.vol(5, 19, 18, 4, { u, v -> u > v && u < 18 - v }, { _, _ -> .6 }, R.wood, ink); b.line(14, 5, 14, 19, ink); for (j in 0 until 12) b.r(15, 6 + j, 1 + j / 2, 1, light) }
            "train" -> { ground(rgb(0x6a5e52)); b.r(0, 25, 28, 1, rgb(0x9a9aa2)); b.r(3, 15, 16, 8, rgb(0x2a4a2a)); b.r(19, 11, 6, 12, rgb(0x2a4a2a)); b.r(20, 13, 4, 3, rgb(0xf6d77a)); b.r(5, 17, 3, 2, rgb(0xf6d77a)); b.r(11, 17, 3, 2, rgb(0xf6d77a)); b.disc(7, 23, 2, ink); b.disc(14, 23, 2, ink); b.disc(21, 23, 2, ink); b.r(5, 10, 3, 5, ink) }
            "plane" -> { b.r(4, 13, 20, 3, light); b.r(11, 7, 4, 14, light); b.r(4, 11, 2, 4, light); b.p(23, 14, rgb(0xa33a2c)); for (i in 0 until 6) b.p(2 + i * 4, 24 + i % 2, fg) }
            "bird", "swallow" -> { val c = if (f == "swallow") rgb(0x1e2a4a) else rgb(0x8e5a34); b.vol(8, 12, 12, 7, ell(6.0, 3.5, 6.0, 3.5), sph(4.0, 2.0, 6.0, 3.5, .3), intArrayOf(c.dim(.3f), c, c.lit(.2f)), ink); b.line(10, 12, 4, 6, c); b.line(14, 12, 20, 5, c); b.p(19, 14, rgb(0xe8a030)); if (f == "swallow") { b.line(8, 16, 3, 20, c); b.line(8, 16, 5, 21, c); b.r(16, 15, 3, 2, rgb(0xd83a2a)) } }
            "crane" -> { ground(); for (i in 0 until 3) { val x = 6 + i * 7; val y = 6 + abs(i - 1) * 3; b.line(x - 3, y + 1, x, y, fg); b.line(x, y, x + 3, y + 1, fg) }; b.line(14, 14, 14, 24, rgb(0x2a2a30)); b.vol(10, 12, 9, 5, ell(4.5, 2.5, 4.5, 2.5), { _, _ -> .8 }, R.grey, ink); b.line(18, 13, 22, 8, rgb(0x2a2a30)); b.p(22, 7, rgb(0xd83a2a)) }
            "owl" -> { b.vol(8, 6, 13, 18, ell(6.5, 9.0, 6.5, 9.0), sph(4.0, 6.0, 6.5, 9.0, .3), intArrayOf(rgb(0x4a3020), rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52), rgb(0xd8b07a)), ink); b.disc(11, 11, 2, rgb(0xf8d070)); b.disc(17, 11, 2, rgb(0xf8d070)); b.p(11, 11, ink); b.p(17, 11, ink); b.p(14, 14, rgb(0xe8a030)); b.r(4, 24, 20, 2, rgb(0x55331e)) }
            "fish" -> { water(); b.vol(4, 10, 18, 9, ell(9.0, 4.5, 9.0, 4.5), sph(6.0, 3.0, 9.0, 4.5, .3), R.stone, ink); b.line(21, 14, 26, 9, ink); b.line(21, 14, 26, 19, ink); b.p(7, 13, ink); for (i in 8 until 20 step 3) b.p(i, 14, rgb(0x55504c)) }
            "flower" -> { ground(); b.line(14, 24, 14, 12, rgb(0x426442)); b.line(14, 18, 10, 15, rgb(0x426442)); for (a in 0 until 6) { val an = a * PI / 3; b.disc((14 + cos(an) * 3).roundToInt(), (10 + sin(an) * 3).roundToInt(), 2, rgb(0xd8303a)) }; b.disc(14, 10, 1, rgb(0xf8d070)) }
            "tree" -> { ground(); b.r(13, 16, 3, 8, rgb(0x55331e)); b.vol(5, 3, 18, 15, ell(9.0, 7.5, 9.0, 7.5), sph(6.0, 4.0, 9.0, 7.5, .25), R.green, ink); for (k in 0 until 5) b.p(8 + (hash(k, 1) * 12).toInt(), 6 + (hash(1, k) * 9).toInt(), rgb(0xd83a2a)) }
            "birch" -> { ground(rgb(0x9c4c20)); Props.birch(b, 9, 3, 22, app.lipovka.domain.Leaves.GOLD); Props.birch(b, 18, 6, 19, app.lipovka.domain.Leaves.GOLD, alt = true) }
            "fir" -> { ground(R.snow[4]); Props.spruce(b, 7, 3, 22, snow = true); for (k in 0 until 6) b.p(9 + (hash(k, 4) * 10).toInt(), 8 + (hash(4, k) * 12).toInt(), intArrayOf(rgb(0xff5050), rgb(0xffe060), rgb(0x60a0ff))[k % 3]) }
            "mushroom" -> { ground(); b.vol(7, 8, 14, 8, { u, v -> v < 8 && ((u - 7) / 7.0).let { it * it } + ((v - 8) / 8.0).let { it * it } <= 1 }, sph(5.0, 3.0, 7.0, 6.0, .3), R.red, ink); for ((x, y) in listOf(10 to 11, 15 to 10, 17 to 13)) b.p(x, y, light); b.vol(11, 16, 6, 8, { _, _ -> true }, { u, _ -> .8 - u * .06 }, R.cream, ink) }
            "berry" -> { for (k in 0 until 7) b.line(4 + k * 3, 24, 6 + k * 2, 14, rgb(0x426442)); for (k in 0 until 6) b.ball(6 + (k % 3) * 7, 12 + (k / 3) * 6, 2, R.jam, ink) }
            "apple" -> { b.ball(14, 16, 7, R.apple, ink); b.line(14, 9, 15, 5, rgb(0x55331e)); b.vol(15, 4, 6, 3, ell(3.0, 1.5, 3.0, 1.5), { _, _ -> .6 }, R.green, ink) }
            "bee" -> { b.vol(7, 11, 14, 9, ell(7.0, 4.5, 7.0, 4.5), sph(5.0, 3.0, 7.0, 4.5, .3), R.gold, ink); for (x in listOf(10, 14, 18)) b.r(x, 11, 2, 9, ink); b.vol(9, 5, 7, 6, ell(3.5, 3.0, 3.5, 3.0), { _, _ -> .9 }, R.glass, ink); b.vol(14, 4, 7, 6, ell(3.5, 3.0, 3.5, 3.0), { _, _ -> .9 }, R.glass, ink) }
            "horse" -> { ground(); b.r(6, 12, 14, 6, rgb(0x8e5a34)); b.r(18, 6, 4, 8, rgb(0x8e5a34)); b.r(21, 7, 3, 3, rgb(0x8e5a34)); for (x in listOf(7, 10, 16, 19)) b.r(x, 18, 1, 6, rgb(0x55331e)); b.r(17, 5, 2, 7, ink); b.line(6, 12, 3, 17, ink) }
            "cow" -> { ground(); b.r(5, 12, 15, 7, light); b.r(8, 13, 4, 3, ink); b.r(15, 15, 3, 3, ink); b.r(19, 10, 5, 5, light); b.p(21, 12, ink); for (x in listOf(6, 9, 15, 18)) b.r(x, 19, 1, 5, rgb(0x55504c)) }
            "goat" -> { ground(); b.vol(4, 12, 16, 8, ell(8.0, 4.0, 8.0, 4.0), sph(6.0, 3.0, 8.0, 4.0, .4), R.cream, ink); b.vol(17, 6, 7, 7, ell(3.5, 3.5, 3.5, 3.5), sph(2.5, 2.5, 3.5, 3.5, .4), R.cream, ink); b.p(19, 4, rgb(0x6e6862)); b.p(22, 4, rgb(0x6e6862)); b.r(21, 13, 1, 3, light); for (x in listOf(6, 9, 15, 18)) b.r(x, 20, 1, 4, rgb(0x55504c)) }
            "cat" -> { b.vol(5, 8, 18, 16, ell(9.0, 8.0, 9.0, 8.0), sph(6.0, 5.0, 9.0, 8.0, .25), R.ginger, ink); for ((ax, cx2) in listOf(6 to 9, 18 to 21)) for (v in 0 until 5) b.r(ax + v / 2, 4 + v, (cx2 - ax) - v, 1, R.ginger[4]); b.p(10, 15, ink); b.p(17, 15, ink); b.p(13, 18, rgb(0xd8707a)); b.p(14, 18, rgb(0xd8707a)) }
            "dog" -> { b.vol(5, 9, 18, 15, ell(9.0, 7.5, 9.0, 7.5), sph(6.0, 5.0, 9.0, 7.5, .3), intArrayOf(rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52), rgb(0xd8b07a), rgb(0xecd2a2)), ink); b.r(4, 8, 4, 8, rgb(0x6e4a28)); b.r(20, 8, 4, 8, rgb(0x6e4a28)); b.p(11, 15, ink); b.p(17, 15, ink); b.r(13, 18, 3, 2, ink) }
            "snowflake" -> { for (a in 0 until 6) { val an = a * PI / 3; b.line(14.0, 15.0, 14 + cos(an) * 10, 15 + sin(an) * 10, light); b.line(14 + cos(an) * 6, 15 + sin(an) * 6, 14 + cos(an + .5) * 8, 15 + sin(an + .5) * 8, light) } }
            "star" -> { for (a in 0 until 5) { val an = a * 2 * PI / 5 - PI / 2; b.line(14.0, 15.0, 14 + cos(an) * 10, 15 + sin(an) * 10, rgb(0xf8d070)); b.line(14.0, 15.0, 14 + cos(an) * 9, 15 + sin(an) * 9 + 1, rgb(0xf8d070)) }; b.disc(14, 15, 3, rgb(0xf8d070)) }
            "moon" -> { b.disc(14, 13, 8, rgb(0xf4eedc)); b.disc(18, 11, 7, bg(bgName)[1]); for (k in 0 until 6) b.p((hash(k, 3) * 28).toInt(), (hash(3, k) * 26).toInt(), light) }
            "sun" -> { b.glow(14, 13, 12, rgb(0xfff6d0), .5f, 4); b.disc(14, 13, 6, rgb(0xf8d070)); for (a in 0 until 8) { val an = a * PI / 4; b.line(14 + cos(an) * 8, 13 + sin(an) * 8, 14 + cos(an) * 11, 13 + sin(an) * 11, rgb(0xf8d070)) }; ground() }
            "rain" -> { water(); for (k in 0 until 16) { val x = (hash(k, 7) * 28).toInt(); val y = (hash(k, 8) * 20).toInt(); b.p(x, y, light); b.p(x - 1, y + 1, light) }; for (k in 0 until 3) for (a in 0 until 10) { val an = a / 10.0 * 2 * PI; b.p((6 + k * 8 + cos(an) * 3).roundToInt(), (26 + sin(an) * 1.2).roundToInt(), light) } }
            "rainbow" -> { val cols = intArrayOf(rgb(0xd83a3a), rgb(0xf0a030), rgb(0xf8e060), rgb(0x5aa050), rgb(0x4a7ac8), rgb(0x7a5ab0)); for ((k, c) in cols.withIndex()) for (a in 0..40) { val an = PI + a / 40.0 * PI; b.p((14 + cos(an) * (12 - k)).roundToInt(), (26 + sin(an) * (12 - k)).roundToInt(), c) }; ground() }
            "lighthouse" -> { water(); b.vol(11, 6, 7, 18, { u, v -> abs(u - 3.0) <= 2 + v * .08 }, { u, v -> .7 - u * .06 - if ((v / 4) % 2 == 0) .3 else 0.0 }, R.red, ink); b.r(10, 3, 9, 3, rgb(0xf8d070)); b.glow(14, 4, 10, rgb(0xfff0b0), .4f, 3) }
            "bridge" -> { water(); for (x in 0 until 28) b.r(x, 16, 1, 2, rgb(0x8e5a34)); for (x in listOf(3, 12, 21)) b.r(x, 18, 2, 8, rgb(0x55331e)); for (x in 0 until 28 step 3) b.r(x, 12, 1, 4, rgb(0x8e5a34)); b.r(0, 12, 28, 1, rgb(0x8e5a34)) }
            "kettle" -> { b.r(0, 25, 28, 5, rgb(0x714528)); Props.kettle(b, -2, 1, .78) }
            "letter" -> Props.envelope(b, 3, 8, 22, 15, light)
            "telegram" -> { for (y in 0 until 30 step 4) b.r(0, y, 28, 2, rgb(0x6e2420)); b.line(17, 2, 9, 14, rgb(0xf8d070)); b.line(18, 2, 10, 14, rgb(0xf8d070)); b.line(9, 14, 18, 14, rgb(0xf8d070)); b.line(18, 15, 10, 27, rgb(0xf8d070)); b.line(17, 15, 9, 27, rgb(0xfff0a0)) }
            "radio" -> { b.vol(4, 10, 20, 14, { _, _ -> true }, { u, _ -> .6 - u * .02 }, R.wood, ink); b.r(6, 12, 9, 9, rgb(0x2a2a30)); for (j in 13 until 21 step 2) b.r(7, j, 7, 1, rgb(0x55504c)); b.disc(19, 15, 2, rgb(0xe8bf58)); b.disc(19, 20, 1, rgb(0xe8bf58)); b.line(18, 10, 22, 2, fg); for (k in 0 until 3) b.p(23 + k, 2 + k, fg) }
            "book" -> { b.vol(5, 6, 18, 20, { _, _ -> true }, { u, _ -> .6 - u * .015 }, R.red, ink); b.r(7, 6, 1, 20, rgb(0xe8bf58)); b.r(10, 11, 10, 2, rgb(0xe8bf58)); b.r(10, 15, 8, 1, rgb(0xe8bf58)); b.r(6, 25, 16, 1, light) }
            "lake" -> { for (y in 14 until 30) for (x in 0 until 28) b.p(x, y, rp(R.water, .3 + (y - 14) / 30.0, x, y)); for (x in 0 until 28) { val h = (4 + sin(x * .4) * 3).roundToInt(); b.r(x, 14 - h, 1, h, rgb(0x2a4a32)) }; b.r(6, 20, 8, 1, light) }
            "mountain" -> { for (x in 0 until 28) { val h = 22 - (abs(x - 14) * 1.3).roundToInt(); for (y in (22 - h).coerceAtLeast(2) until 30) b.p(x, y, if (y < 10) light else rgb(0x6a6a7a)) } }
            "globe" -> { b.ball(14, 14, 10, R.blue, ink); for ((x, y) in listOf(9 to 9, 10 to 10, 11 to 10, 16 to 15, 17 to 16, 18 to 15, 12 to 18, 13 to 19)) { b.p(x, y, rgb(0x5aa050)); b.p(x + 1, y, rgb(0x5aa050)) }; b.line(14, 25, 14, 28, rgb(0xc8952e)); b.r(9, 28, 11, 1, rgb(0xc8952e)) }
            "rocket" -> { b.vol(11, 3, 7, 18, ell(3.5, 9.0, 3.5, 9.0), sph(2.0, 6.0, 3.5, 9.0, .4), R.grey, ink); b.disc(14, 9, 1, rgb(0x4a7ac8)); b.r(8, 16, 3, 5, rgb(0xa33a2c)); b.r(18, 16, 3, 5, rgb(0xa33a2c)); b.r(13, 21, 3, 4, rgb(0xf8b040)); b.p(14, 25, rgb(0xfff0a0)); for (k in 0 until 6) b.p((hash(k, 2) * 28).toInt(), (hash(2, k) * 30).toInt(), light) }
            "fireworks" -> for ((cx, cy, c) in listOf(Triple(9, 9, rgb(0xff6050)), Triple(19, 13, rgb(0xffe060)), Triple(12, 20, rgb(0x60c0ff)))) for (a in 0 until 10) { val an = a * PI / 5; b.line(cx + cos(an) * 2, cy + sin(an) * 2, cx + cos(an) * 5, cy + sin(an) * 5, c) }
            "sled" -> { ground(R.snow[4]); b.r(5, 18, 18, 3, rgb(0xa33a2c)); b.line(4, 22, 24, 22, rgb(0x55504c)); b.line(4, 22, 3, 19, rgb(0x55504c)); b.line(8, 21, 8, 22, rgb(0x55504c)); b.line(19, 21, 19, 22, rgb(0x55504c)) }
            "lantern" -> { b.r(10, 6, 9, 16, rgb(0x2a2a30)); b.r(11, 8, 7, 12, rgb(0xf6d77a)); b.r(13, 3, 3, 3, rgb(0x2a2a30)); b.r(11, 14, 7, 1, rgb(0xd83a2a)); b.glow(14, 14, 12, rgb(0xfff0b0), .35f, 3) }
            "bell" -> { b.vol(8, 6, 13, 15, { u, v -> abs(u - 6.0) <= 2.5 + v * .3 }, { u, _ -> .7 - u * .04 }, R.brass, ink); b.disc(14, 22, 2, rgb(0x6a4614)); b.r(12, 3, 5, 3, rgb(0xa33a2c)) }
            "clock" -> { b.ball(14, 14, 10, R.cream, ink); for (a in 0 until 12) { val an = a / 12.0 * 2 * PI; b.p((14 + cos(an) * 8).roundToInt(), (14 + sin(an) * 8).roundToInt(), ink) }; b.line(14, 14, 14, 8, ink); b.line(14, 14, 18, 16, ink) }
            "heart" -> { b.vol(5, 6, 18, 17, { u, v -> val x = (u - 9.0) / 9; val y = (8.0 - v) / 8; (x * x + y * y - 1).let { it * it * it } - x * x * y * y * y <= 0 }, sph(6.0, 5.0, 9.0, 8.0, .3), R.red, ink) }
            "anchor" -> { b.r(13, 5, 2, 18, fg); b.disc(14, 4, 2, fg); b.r(9, 9, 10, 2, fg); for (a in 0..10) { val an = a / 10.0 * PI; b.p((14 + cos(an) * 8).roundToInt(), (18 + sin(an) * 5).roundToInt(), fg) } }
            "violin" -> { b.vol(9, 10, 11, 16, { u, v -> val y = v - 8.0; abs(u - 5.0) <= 5 - (if (abs(y) < 2) 2.0 else 0.0) - abs(y) * .1 }, sph(4.0, 5.0, 6.0, 8.0, .3), R.honey, ink); b.r(14, 2, 2, 10, rgb(0x2a1a10)); b.p(12, 15, ink); b.p(17, 15, ink) }
            "camera" -> { b.vol(4, 10, 20, 13, { _, _ -> true }, { u, _ -> .5 - u * .01 }, R.iron, ink); b.ball(14, 16, 5, R.glass, ink); b.r(6, 8, 5, 2, rgb(0x2a2a30)); b.r(19, 12, 3, 2, rgb(0xe8bf58)) }
            else -> Props.envelope(b, 3, 8, 22, 15, light)
        }
    }
}
