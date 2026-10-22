package app.lipovka.ui.art

import kotlin.math.abs

/**
 * The gifts residents give, each family drawn in a 14×16 cell (its bottom centre at the anchor) so
 * they can stand on shelves, hang on walls or sit in a list.
 */
object ItemArt {
    const val W = 14
    const val H = 16

    /** Where a family belongs in the room. */
    enum class Slot { SHELF, WALL, LINE }

    fun slot(family: String): Slot = when (family) {
        "postcard", "photo", "qsl", "map", "badge", "feather", "bouquet", "record", "carving" -> Slot.WALL
        "socks", "mittens", "scarf" -> Slot.LINE
        else -> Slot.SHELF
    }

    private fun col(variant: String): Int = when (variant) {
        "red", "jam", "patterned" -> rgb(0xb5452f)
        "green", "cucumbers" -> rgb(0x3c6c44)
        "grey" -> rgb(0x8a8a92)
        "blue", "blueberry" -> rgb(0x3a5a9c)
        "white" -> rgb(0xece6d8)
        "gold" -> rgb(0xe0a830)
        "striped" -> rgb(0xd8c4a0)
        "check" -> rgb(0x8e2434)
        else -> rgb(0xa86a3a)
    }

    private fun jarRamp(v: String) = when (v) {
        "jam", "lingonberry" -> R.jam
        "cranberry" -> intArrayOf(rgb(0x2a0608), rgb(0x52101a), rgb(0x7a1a24), rgb(0xa8283a), rgb(0xd04a5a))
        "honey" -> R.honey
        "cucumbers" -> intArrayOf(rgb(0x1a2a14), rgb(0x2e4a22), rgb(0x4a6a30), rgb(0x6a8a40), rgb(0x9ab070))
        "mushrooms" -> intArrayOf(rgb(0x2a1a0c), rgb(0x4a2e16), rgb(0x6e4a24), rgb(0x946a3a), rgb(0xc09a6a))
        "applejam" -> R.gold
        "blueberry" -> intArrayOf(rgb(0x14102a), rgb(0x261e4a), rgb(0x3a2e6a), rgb(0x54468e), rgb(0x7a6ab0))
        "cloudberry" -> intArrayOf(rgb(0x6a2e06), rgb(0xa04a0c), rgb(0xd07018), rgb(0xf09a30), rgb(0xfcc870))
        else -> R.jam
    }

    /** Draws one item with its bottom centre at (cx, by). */
    fun draw(b: Buf, family: String, variant: String, cx: Int, by: Int) {
        val x = cx - W / 2
        val y = by - H
        val ink = R.INK
        when (family) {
            "jar" -> Props.jar(b, x + 2, y + 3, jarRamp(variant), if (variant == "honey") rgb(0x3c6c44) else rgb(0xa33a2c), 10, 13)
            "pie" -> {
                b.vol(x, y + 10, 14, 6, ell(7.0, 3.0, 7.0, 3.0), sph(5.0, 1.5, 7.0, 3.0, .3), R.honey, ink)
                for (i in 2 until 12 step 3) b.p(x + i, y + 11, rgb(0x8a520c))
                if (variant == "berry") for (i in 3 until 12 step 3) b.p(x + i, y + 12, rgb(0x8e2434))
            }
            "bread" -> when (variant) {
                "kalach" -> { b.vol(x + 1, y + 6, 12, 10, { u, v -> val d = (u - 5.5) * (u - 5.5) / 36 + (v - 5.0) * (v - 5.0) / 25; d <= 1 && d > .25 }, sph(4.0, 3.0, 6.0, 5.0, .3), R.honey, ink) }
                "gingerbread" -> { b.vol(x + 2, y + 6, 10, 10, { _, _ -> true }, sph(4.0, 3.0, 6.0, 6.0, .3), R.wood.copyOfRange(3, 8), ink); b.r(x + 4, y + 9, 6, 1, rgb(0xfbf3dc)); b.r(x + 4, y + 12, 6, 1, rgb(0xfbf3dc)) }
                "pretzel" -> { b.vol(x + 2, y + 7, 10, 9, { u, v -> val a = (u - 2.5) * (u - 2.5) + (v - 5.0) * (v - 5.0); val c = (u - 7.5) * (u - 7.5) + (v - 5.0) * (v - 5.0); (a in 3.0..10.0) || (c in 3.0..10.0) }, sph(4.0, 3.0, 6.0, 5.0, .3), R.honey, ink) }
                else -> { b.vol(x, y + 8, 14, 8, ell(7.0, 5.0, 7.0, 5.0), sph(5.0, 3.0, 7.0, 5.0, .3), R.honey, ink); for (i in 3 until 12 step 3) b.line(x + i, y + 10, x + i + 1, y + 12, rgb(0x8a520c)) }
            }
            "basket" -> {
                b.vol(x + 1, y + 8, 12, 8, { u, v -> abs(u - 5.5) <= 6 - v * .3 }, { u, v -> .6 - u * .02 - if ((u + v) % 2 == 0) .12 else 0.0 }, R.thatch, ink)
                b.line(x + 2, y + 8, x + 7, y + 2, rgb(0x7a5622)); b.line(x + 7, y + 2, x + 12, y + 8, rgb(0x7a5622))
                val c = when (variant) { "apples" -> R.apple; "berries" -> R.jam; "eggs" -> R.cream; "cones" -> R.wood.copyOfRange(2, 7); else -> R.wood.copyOfRange(3, 8) }
                for (i in 0 until 3) b.ball(x + 4 + i * 3, y + 8, 1, c)
                if (variant == "mushrooms") for (i in 0 until 3) { b.r(x + 3 + i * 3, y + 6, 3, 2, rgb(0x8a4a20)); b.p(x + 4 + i * 3, y + 8, rgb(0xf2ece0)) }
            }
            "socks", "mittens" -> {
                val c = col(variant)
                if (family == "socks") { b.r(x + 4, y + 2, 5, 10, c); b.r(x + 1, y + 10, 8, 5, c); b.r(x + 4, y + 2, 5, 1, rgb(0xfbf3dc)); if (variant == "striped") for (j in 4 until 14 step 3) b.r(x + 1, y + j, 8, 1, rgb(0xa33a2c)) }
                else { b.vol(x + 2, y + 3, 9, 12, ell(4.5, 7.0, 4.5, 6.0), sph(3.0, 4.0, 5.0, 6.0, .4), intArrayOf(c.dim(.4f), c.dim(.2f), c, c.lit(.2f)), ink); b.vol(x + 9, y + 7, 4, 5, ell(2.0, 2.5, 2.0, 2.5), { _, _ -> .5 }, intArrayOf(c), ink); b.r(x + 2, y + 13, 9, 2, rgb(0xfbf3dc)) }
                b.p(x + 6, y, rgb(0x8e5a34))
            }
            "scarf" -> { val c = col(variant); b.r(x + 2, y, 10, 3, c); b.r(x + 2, y, 3, 16, c); b.r(x + 9, y, 3, 12, c); for (j in 0 until 16 step 3) b.p(x + 3, y + j, rgb(0xfbf3dc)); for (i in 0 until 3) b.p(x + 2 + i, y + 15, c.dim(.3f)) }
            "postcard" -> {
                b.r(x, y + 3, 14, 11, ink); b.r(x + 1, y + 4, 12, 9, rgb(0xfbf3dc))
                val sky = when (variant) { "winter" -> R.snow; "space" -> R.night; "sea", "ship" -> R.day; "flowers" -> R.blossom; else -> R.morning }
                b.vgrad(x + 2, y + 5, 10, 5, sky)
                val low = when (variant) { "sea", "ship", "lake" -> rgb(0x3a6070); "winter" -> rgb(0xe2eef2); "space" -> rgb(0x151d34); "city" -> rgb(0x706860); else -> rgb(0x426442) }
                b.r(x + 2, y + 9, 10, 3, low)
                when (variant) {
                    "ship" -> { b.r(x + 4, y + 8, 6, 2, rgb(0xa33a2c)); b.p(x + 7, y + 6, rgb(0xfbf3dc)) }
                    "mountains" -> { b.line(x + 2, y + 9, x + 6, y + 5, rgb(0x6a6a7a)); b.line(x + 6, y + 5, x + 11, y + 9, rgb(0x6a6a7a)) }
                    "space" -> { b.p(x + 4, y + 6, rgb(0xfbf3dc)); b.p(x + 9, y + 7, rgb(0xfbf3dc)); b.disc(x + 7, y + 7, 1, rgb(0xe8bf58)) }
                    "flowers" -> for (i in 0 until 3) b.p(x + 4 + i * 3, y + 8, rgb(0xd83a4a))
                    "birch" -> { b.r(x + 6, y + 5, 1, 6, rgb(0xfbf3dc)); b.r(x + 5, y + 5, 3, 2, rgb(0xe0a830)) }
                    "train" -> b.r(x + 3, y + 8, 8, 2, rgb(0x3a6a3a))
                    "city" -> for (i in 0 until 4) b.r(x + 3 + i * 2, y + 6 + i % 2, 1, 4, rgb(0x504840))
                }
                b.p(x + 7, y + 3, rgb(0xa33a2c))
            }
            "photo" -> {
                b.r(x + 1, y + 2, 12, 13, rgb(0x6e4426)); b.r(x + 2, y + 3, 10, 11, rgb(0xf2ece0))
                val tone = if (variant == "old") rgb(0xb4a07c) else rgb(0x8aa0b0)
                b.r(x + 3, y + 4, 8, 7, tone)
                val n = when (variant) { "group" -> 3; "wedding" -> 2; else -> 1 }
                for (i in 0 until n) { val px = x + 7 - n + i * 2; b.p(px, y + 6, rgb(0xf2c09a)); b.r(px, y + 7, 1, 3, if (variant == "wedding" && i == 1) rgb(0xfbf3dc) else rgb(0x2a2a30)) }
                if (variant == "landscape") { b.r(x + 3, y + 8, 8, 3, rgb(0x426442)); b.disc(x + 9, y + 5, 1, rgb(0xfff0b0)) }
                if (variant == "baby") b.disc(x + 7, y + 7, 2, rgb(0xf2c09a))
            }
            "book" -> {
                val c = if (variant == "notebook") rgb(0x8a8a92) else col(variant)
                b.vol(x + 2, y + 2, 10, 14, { _, _ -> true }, { u, _ -> .6 - u * .03 + if (u == 0) .3 else 0.0 }, intArrayOf(c.dim(.4f), c.dim(.2f), c, c.lit(.25f)), ink)
                b.r(x + 4, y + 5, 6, 1, rgb(0xe8bf58)); b.r(x + 3, y + 15, 9, 1, rgb(0xfbf3dc))
            }
            "candle" -> { b.vol(x + 4, y + 5, 6, 11, { _, _ -> true }, { u, _ -> .8 - u * .08 }, if (variant == "honey") R.honey else R.cream, ink); b.p(x + 7, y + 3, rgb(0x2a1a10)); b.p(x + 7, y + 2, rgb(0xffd060)); b.p(x + 7, y + 1, rgb(0xfff0b0)) }
            "toy" -> when (variant) {
                "matryoshka" -> { b.vol(x + 3, y + 3, 8, 13, ell(4.0, 7.0, 4.0, 6.5), sph(3.0, 4.0, 4.0, 7.0, .3), R.red, ink); b.disc(x + 7, y + 6, 2, rgb(0xf2c09a)); b.r(x + 5, y + 10, 4, 2, rgb(0xe8bf58)) }
                "horse" -> { b.r(x + 2, y + 7, 9, 4, rgb(0xc88e58)); b.r(x + 9, y + 3, 3, 5, rgb(0xc88e58)); b.r(x + 2, y + 11, 1, 4, rgb(0x8e5a34)); b.r(x + 9, y + 11, 1, 4, rgb(0x8e5a34)); b.p(x + 10, y + 4, ink); b.r(x + 8, y + 3, 1, 4, rgb(0xa33a2c)) }
                "whistle" -> { b.vol(x + 2, y + 6, 10, 9, ell(5.0, 4.5, 5.0, 4.5), sph(4.0, 3.0, 5.0, 4.5, .3), R.cream, ink); b.p(x + 4, y + 8, rgb(0x3a5a9c)); b.p(x + 8, y + 9, rgb(0xa33a2c)); b.r(x + 11, y + 9, 3, 2, R.cream[3]) }
                "boat" -> { b.vol(x, y + 10, 14, 4, { u, v -> u > v && u < 14 - v }, { _, _ -> .6 }, R.red, ink); b.line(x + 7, y + 1, x + 7, y + 10, rgb(0x2a1a10)); for (j in 0 until 7) b.r(x + 8, y + 2 + j, 1 + j / 2, 1, rgb(0xfbf3dc)) }
                "bear" -> { b.ball(x + 7, y + 11, 4, R.wood.copyOfRange(3, 8), ink); b.ball(x + 7, y + 5, 3, R.wood.copyOfRange(3, 8), ink); b.p(x + 4, y + 2, rgb(0x8e5a34)); b.p(x + 10, y + 2, rgb(0x8e5a34)) }
                else -> { b.vol(x + 2, y + 6, 10, 8, { u, v -> abs(u - 4.5) <= 5 - abs(v - 3.5) * .9 }, { u, _ -> .7 - u * .04 }, R.red, ink); b.line(x + 7, y + 2, x + 7, y + 6, rgb(0x5a3a1e)) }
            }
            "carving" -> when (variant) {
                "spoon" -> { b.vol(x + 4, y + 1, 6, 6, ell(3.0, 3.0, 3.0, 3.0), sph(2.0, 2.0, 3.0, 3.0, .3), R.wood.copyOfRange(3, 8), ink); b.r(x + 6, y + 7, 2, 9, rgb(0xc88e58)) }
                "sign" -> { b.vol(x, y + 4, 14, 8, { _, _ -> true }, { u, _ -> .6 - u * .02 }, R.wood, ink); b.r(x + 2, y + 6, 10, 1, rgb(0xe8bf58)); b.r(x + 2, y + 8, 7, 1, rgb(0xe8bf58)) }
                "frame" -> { b.r(x + 1, y + 2, 12, 13, rgb(0xc88e58)); b.r(x + 3, y + 4, 8, 9, rgb(0x8aa0b0)); for (i in 1 until 13 step 2) { b.p(x + i, y + 2, rgb(0x8e5a34)); b.p(x + i, y + 14, rgb(0x8e5a34)) } }
                "bird" -> { b.vol(x + 2, y + 5, 10, 6, ell(5.0, 3.0, 5.0, 3.0), sph(3.0, 2.0, 5.0, 3.0, .3), R.wood.copyOfRange(3, 8), ink); b.line(x + 2, y + 3, x + 6, y + 6, rgb(0xc88e58)); b.line(x + 12, y + 3, x + 8, y + 6, rgb(0xc88e58)) }
                else -> { b.ball(x + 7, y + 11, 4, R.wood.copyOfRange(2, 7), ink); b.ball(x + 7, y + 5, 3, R.wood.copyOfRange(2, 7), ink) }
            }
            "bouquet" -> {
                val c = when (variant) { "rowan" -> rgb(0xd82a1a); "wheat" -> rgb(0xe0b850); "cornflowers" -> rgb(0x4a6ad8); "willow" -> rgb(0xe8e4d8); else -> rgb(0xb494bc) }
                for (i in 0 until 5) b.line(x + 7, y + 15, x + 3 + i * 2, y + 4, rgb(0x6a7a3a))
                for (i in 0 until 9) b.p(x + 2 + (hash(i, 1) * 10).toInt(), y + 2 + (hash(i, 2) * 5).toInt(), c)
                b.r(x + 6, y + 11, 3, 2, rgb(0xa33a2c))
            }
            "feather" -> { val c = when (variant) { "owl" -> rgb(0xa88050); "jay" -> rgb(0x4a7ac8); else -> rgb(0xd8d8e0) }; for (j in 0 until 14) { val wd = (3 - abs(j - 6) / 3).coerceAtLeast(1); b.r(x + 7 - wd + j / 5, y + 1 + j, wd * 2, 1, if (variant == "jay" && j % 3 == 0) rgb(0x1a2a5a) else c) }; b.line(x + 7, y + 2, x + 9, y + 15, rgb(0x5a4a3a)) }
            "found" -> when (variant) {
                "shell" -> { b.vol(x + 2, y + 8, 10, 7, ell(5.0, 3.5, 5.0, 3.5), sph(3.0, 2.0, 5.0, 3.5, .4), R.blossom, ink); for (i in 3 until 11 step 2) b.line(x + 7, y + 14, x + i, y + 9, rgb(0xb47a8a)) }
                "cone" -> { b.vol(x + 4, y + 4, 6, 11, ell(3.0, 5.5, 3.0, 5.5), sph(2.0, 3.0, 3.0, 5.5, .3), R.wood.copyOfRange(2, 7), ink); for (j in 5 until 15 step 2) b.p(x + 6 + j % 4 / 2, y + j, rgb(0x3a2214)) }
                "amber" -> b.vol(x + 4, y + 8, 7, 6, ell(3.5, 3.0, 3.5, 3.0), sph(2.5, 2.0, 3.5, 3.0, .4), R.gold, ink)
                "horseshoe" -> b.vol(x + 2, y + 3, 10, 12, { u, v -> val d = (u - 4.5) * (u - 4.5) / 25 + (v - 5.0) * (v - 5.0) / 30; d <= 1 && d > .4 && v < 11 }, { u, _ -> .6 - u * .03 }, R.iron, ink)
                "key" -> { b.ball(x + 4, y + 8, 2, R.brass, ink); b.r(x + 6, y + 8, 7, 1, rgb(0xc8952e)); b.r(x + 11, y + 9, 1, 2, rgb(0xc8952e)) }
                else -> b.vol(x + 3, y + 9, 8, 6, ell(4.0, 3.0, 4.0, 3.0), sph(3.0, 2.0, 4.0, 3.0, .3), R.stone, ink)
            }
            "fish" -> { b.vol(x, y + 6, 12, 6, ell(6.0, 3.0, 6.0, 3.0), sph(4.0, 2.0, 6.0, 3.0, .3), if (variant == "smoked") R.honey else R.stone, ink); b.line(x + 11, y + 9, x + 14, y + 6, ink); b.line(x + 11, y + 9, x + 14, y + 12, ink); b.p(x + 2, y + 8, ink) }
            "honeycomb" -> { b.r(x + 1, y + 2, 12, 13, rgb(0x8e5a34)); for (j in 0 until 5) for (i in 0 until 5) { val px = x + 2 + i * 2 + (j % 2); val py = y + 3 + j * 2; b.p(px, py, rgb(0xe0a630)); b.p(px + 1, py, rgb(0xf4cf6e)) } }
            "tea" -> when (variant) {
                "tin" -> { b.vol(x + 3, y + 4, 8, 12, { _, _ -> true }, { u, _ -> .7 - u * .06 }, R.red, ink); b.r(x + 3, y + 4, 8, 2, rgb(0xe8bf58)); b.r(x + 5, y + 8, 4, 4, rgb(0xfbf3dc)) }
                else -> { b.vol(x + 2, y + 6, 10, 10, { _, _ -> true }, { u, _ -> .7 - u * .04 }, R.paper, ink); b.line(x + 2, y + 9, x + 12, y + 9, rgb(0x8a5a2a)); for (i in 0 until 4) b.p(x + 4 + i * 2, y + 4, if (variant == "rosehip") rgb(0xd04a2a) else rgb(0x5c7e50)) }
            }
            "plant" -> {
                b.vol(x + 3, y + 10, 8, 6, { u, v -> abs(u - 3.5) <= 4 - v * .2 }, { u, _ -> .6 - u * .04 }, R.brick, ink)
                when (variant) {
                    "cactus" -> { b.vol(x + 5, y + 2, 4, 9, ell(2.0, 4.5, 2.0, 4.5), sph(1.5, 3.0, 2.0, 4.5, .3), R.green, ink); b.p(x + 7, y + 1, rgb(0xe85a8a)) }
                    "aloe" -> for (i in 0 until 5) b.line(x + 7, y + 10, x + 3 + i * 2, y + 3 + abs(i - 2), rgb(0x5c7e50))
                    "lemon" -> { for (k in 0 until 14) b.p(x + 3 + (hash(k, 9) * 8).toInt(), y + 2 + (hash(9, k) * 8).toInt(), rgb(0x3c6c44)); b.ball(x + 9, y + 6, 1, R.gold) }
                    else -> { for (k in 0 until 14) b.p(x + 3 + (hash(k, 7) * 8).toInt(), y + 3 + (hash(7, k) * 7).toInt(), rgb(0x3c6c44)); val fl = if (variant == "violet") rgb(0x8a5ac8) else rgb(0xd8303a); b.p(x + 5, y + 3, fl); b.p(x + 8, y + 2, fl); b.p(x + 9, y + 5, fl) }
                }
            }
            "qsl" -> { val c = col(variant); b.r(x, y + 3, 14, 10, ink); b.r(x + 1, y + 4, 12, 8, rgb(0xfbf3dc)); b.r(x + 1, y + 4, 12, 3, c); b.r(x + 3, y + 8, 8, 1, rgb(0x2a2a30)); b.r(x + 3, y + 10, 5, 1, rgb(0x2a2a30)); b.p(x + 11, y + 10, c) }
            "lamp" -> {
                if (variant == "lantern") { b.r(x + 3, y + 3, 8, 11, rgb(0x2a2a30)); b.r(x + 4, y + 5, 6, 7, rgb(0xf6d77a)); b.r(x + 6, y + 1, 2, 2, rgb(0x2a2a30)); b.r(x + 4, y + 9, 6, 1, rgb(0xd83a2a)) }
                else { b.vol(x + 3, y + 11, 8, 5, { _, _ -> true }, { u, _ -> .7 - u * .05 }, R.brass, ink); b.vol(x + 4, y + 3, 6, 8, ell(3.0, 4.0, 3.0, 4.0), { u, _ -> if (u == 1) .9 else .5 }, R.glass, ink); b.p(x + 7, y + 6, rgb(0xffd060)) }
            }
            "map" -> { b.r(x, y + 3, 14, 11, if (variant == "star") rgb(0x1e2a48) else rgb(0xe0c890)); if (variant == "star") for (k in 0 until 8) b.p(x + 1 + (hash(k, 4) * 12).toInt(), y + 4 + (hash(4, k) * 9).toInt(), rgb(0xfbf3dc)) else { b.line(x + 2, y + 10, x + 6, y + 6, rgb(0x3a6070)); b.line(x + 6, y + 6, x + 12, y + 8, rgb(0x3a6070)); b.p(x + 9, y + 5, rgb(0xa33a2c)) }; b.r(x, y + 3, 1, 11, rgb(0x8e5a34)); b.r(x + 13, y + 3, 1, 11, rgb(0x8e5a34)) }
            "badge" -> {
                b.r(x + 5, y + 1, 4, 5, if (variant == "medal") rgb(0xa33a2c) else rgb(0x3a5a9c))
                b.ball(x + 7, y + 10, 4, R.brass, ink)
                when (variant) { "post" -> { b.r(x + 5, y + 9, 5, 3, rgb(0xfbf3dc)); b.p(x + 7, y + 10, rgb(0xa33a2c)) }; "honey" -> b.p(x + 7, y + 10, rgb(0x6a4614)); "star" -> { b.p(x + 7, y + 8, rgb(0xd83a2a)); b.r(x + 6, y + 10, 3, 1, rgb(0xd83a2a)) }; else -> b.p(x + 7, y + 10, rgb(0xfff0b0)) }
            }
            "record" -> { b.disc(x + 7, y + 8, 6, rgb(0x141418)); b.disc(x + 7, y + 8, 2, if (variant == "blue") rgb(0x3a5a9c) else rgb(0xa33a2c)); b.p(x + 5, y + 5, rgb(0x5a5a64)); b.p(x + 4, y + 7, rgb(0x5a5a64)) }
            "cheese" -> if (variant == "wedge") b.vol(x + 1, y + 8, 12, 8, { u, v -> v >= (12 - u) * .55 }, { u, _ -> .7 - u * .02 }, R.honey, ink) else { b.vol(x + 1, y + 8, 12, 8, ell(6.0, 4.0, 6.0, 4.0), sph(4.0, 2.0, 6.0, 4.0, .3), R.honey, ink); b.r(x + 2, y + 11, 10, 1, rgb(0xa33a2c)) }
            "bell" -> { b.vol(x + 3, y + 4, 8, 9, { u, v -> abs(u - 3.5) <= 1.5 + v * .3 }, { u, _ -> .7 - u * .05 }, R.brass, ink); b.p(x + 7, y + 13, ink); b.r(x + 6, y + 2, 2, 2, rgb(0x8e5a34)); if (variant == "sleigh") b.r(x + 2, y + 2, 10, 1, rgb(0xa33a2c)) }
            "thermometer" -> { b.r(x + 4, y + 1, 6, 15, rgb(0xf2ece0)); b.r(x + 6, y + 3, 2, 10, rgb(0xc8c0b0)); b.r(x + 6, y + 8, 2, 5, rgb(0xd83a2a)); b.disc(x + 7, y + 13, 1, rgb(0xd83a2a)); for (j in 3 until 13 step 2) b.p(x + 5, y + j, rgb(0x55504c)) }
            else -> Props.envelope(b, x + 1, y + 6, 12, 8)
        }
    }

    /** An item alone, for lists. */
    fun single(family: String, variant: String): Buf = Buf(W + 2, H + 2).also { draw(it, family, variant, W / 2 + 1, H + 1) }

}
