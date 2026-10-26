package app.lipovka.ui.art

/**
 * The people of Lipovka, painted from shaded parts like everything else: legs or a skirt, a body with
 * the opened letter in both hands, a head with a face and hair. Each resident's look is hair, top and
 * bottom colours, then their own things: glasses, a beard, a braid, a cap, an apron, a shawl. In winter
 * everyone wraps up: hats, coats with fur collars, felt boots.
 */
object People {
    private val HAIR = mapOf(
        "brown" to 0x5c3826L, "grey" to 0xa8a8b0L, "white" to 0xe8e8ecL,
        "fair" to 0xd8b070L, "black" to 0x2e2628L, "red" to 0xb85a28L,
    )
    private val SCARF = mapOf("scarf_blue" to 0x4a6aa8L, "scarf_red" to 0xc04a3aL, "scarf_green" to 0x4a8a5aL)
    private val TOP = mapOf(
        "red" to 0xac3e2cL, "brown" to 0x7c4e2cL, "blue" to 0x3a5a9cL, "green" to 0x3c6c44L, "white" to 0xe8e2d4L,
        "yellow" to 0xe0a830L, "violet" to 0x6a4a90L, "cream" to 0xecdcb6L, "black" to 0x2a2a30L, "grey" to 0x6c6c74L,
    )
    private val BOTTOM = mapOf("green" to 0x304c32L, "grey" to 0x55504cL, "blue" to 0x2c3c64L, "brown" to 0x5c3820L, "black" to 0x26262aL)

    private const val OL = 0xFF140C08.toInt()
    private val SKIN = R.skin

    /** A shading ramp around one colour. */
    private fun ramp(c: Int) = intArrayOf(c.dim(.62f), c.dim(.45f), c.dim(.28f), c.dim(.12f), c, c.lit(.16f), c.lit(.32f))

    /** Where a body's parts go, in rows up from the feet and columns out from the middle. */
    private class Body(
        val head: Int, val headH: Int, val headW: Int,
        val neck: Int, val waist: Int, val shoulder: Int, val hip: Int,
        val skirt: Boolean, val hem: Int = -4, val hemW: Int = 8,
    )

    private fun body(sprite: String) = when (sprite) {
        "woman_young" -> Body(-45, 12, 11, -32, -19, 6, 5, true)
        "woman" -> Body(-45, 12, 11, -32, -19, 6, 6, true, hemW = 9)
        "woman_old" -> Body(-43, 12, 11, -31, -18, 6, 6, true, hem = -3, hemW = 9)
        "man_old" -> Body(-45, 12, 12, -32, -18, 7, 6, false)
        "teen" -> Body(-43, 12, 11, -30, -17, 6, 5, false)
        "girl" -> Body(-33, 11, 11, -22, -13, 5, 5, true, hem = -6, hemW = 6)
        else -> Body(-47, 12, 12, -34, -19, 7, 6, false)
    }

    fun height(sprite: String) = -body(sprite).head

    /**
     * Draws a resident standing with the opened letter, feet at (cx, feetY). [look] is hair, top,
     * bottom and then traits; [winter] wraps them up.
     */
    fun draw(b: Buf, sprite: String, look: List<String>, cx: Int, feetY: Int, winter: Boolean) {
        val hairKey = look.getOrElse(0) { "brown" }
        val traits = look.drop(3).toSet()
        val woman = sprite.startsWith("woman") || sprite == "girl"
        val old = sprite.endsWith("_old")
        val hair = rgb(HAIR[hairKey] ?: if (old) 0xa8a8b0L else 0x5c3826L)
        val top = rgb(TOP[look.getOrElse(1) { "red" }] ?: 0xac3e2cL)
        val bottom = rgb(BOTTOM[look.getOrElse(2) { "grey" }] ?: 0x55504cL)
        val scarf = SCARF[hairKey]?.let { rgb(it) } ?: if ((sprite == "woman_old" && traits.none { it in setOf("bun", "bob", "curls", "long") }) || (winter && woman && sprite != "girl" && "beret" !in traits)) top.lit(.08f).let { if (winter) mix(it, rgb(0xc04a3a), .4f) else it } else null
        val bd = body(sprite)
        val p = Painter(b, cx, feetY)
        for (i in -9..9) b.mul(cx + i, feetY, rgb(0x303040), .35f)
        val coat = if (winter) top.dim(.2f) else top
        legs(p, bd, bottom, coat, winter, woman, traits)
        torso(p, bd, coat, top, woman, winter, traits)
        head(p, bd, sprite, hair, scarf, winter, traits)
        letter(p, bd, if (winter) R.felt[3] else SKIN[4])
    }

    /** Draws relative to the feet: x out from the middle, y up (negative) from the ground. */
    private class Painter(val b: Buf, val cx: Int, val fy: Int) {
        fun p(x: Int, y: Int, c: Int) = b.p(cx + x, fy + y, c)
        fun r(x: Int, y: Int, w: Int, h: Int, c: Int) = b.r(cx + x, fy + y, w, h, c)
        inline fun vol(x: Int, y: Int, w: Int, h: Int, noinline mask: (Int, Int) -> Boolean, noinline light: (Int, Int) -> Double, ramp: IntArray, ol: Int? = OL) =
            b.vol(cx + x, fy + y, w, h, mask, light, ramp, ol)
    }

    private fun legs(p: Painter, bd: Body, bottom: Int, coat: Int, winter: Boolean, skirt: Boolean, traits: Set<String>) {
        val boot = if (winter) R.felt else ramp(rgb(0x2a1a12))
        val bootH = if (winter) 6 else 3
        if (bd.skirt) {
            // stockings, shoes, and the skirt over them
            for (s in listOf(-4, 1)) p.vol(s, bd.hem, 3, -bd.hem - bootH + 1, { _, _ -> true }, { u, _ -> .55 - u * .1 }, if (winter) R.felt else ramp(rgb(0xc8a890)), null)
            for (s in listOf(-5, 1)) p.vol(s, -bootH, 5, bootH, { u, v -> !(v == 0 && (u == 0 || u == 4)) }, { u, v -> .6 - u * .08 - v * .04 }, boot)
            val h = bd.hem - bd.waist
            val skirtC = if (winter) coat else (if ("apron" in traits && bd.hemW < 7) bottom else bottom)
            p.vol(-bd.hemW, bd.waist, bd.hemW * 2 + 1, h, { u, v ->
                val half = bd.hip + (bd.hemW - bd.hip) * v.toDouble() / h
                kotlin.math.abs(u - bd.hemW) <= half
            }, { u, v -> .72 - (u - bd.hemW + bd.hemW) / (bd.hemW * 2.0) * .5 + (if ((u + v / 3) % 5 == 0) -.12 else 0.0) }, ramp(skirtC))
            if (!winter) for (x in -bd.hemW + 1 until bd.hemW) p.p(x, bd.hem - 2, skirtC.lit(.2f).let { if ((x + 20) % 3 == 0) it else skirtC.dim(.1f) })
            if ("apron" in traits && !winter) {
                val ap = rgb(0xf2ece0)
                p.vol(-4, bd.waist, 9, h - 2, { u, v -> kotlin.math.abs(u - 4) <= 3 + v / 6 }, { u, _ -> .7 - u * .03 }, ramp(ap), ap.dim(.4f))
                for (x in -4..4) if ((x + 10) % 2 == 0) p.p(x, bd.hem - 4, rgb(0xc04a3a))
            }
            return
        }
        val legTop = bd.waist
        val legH = -legTop - bootH
        val coatLen = if (winter) 7 else 0
        for ((k, s) in listOf(-6, 1).withIndex()) {
            p.vol(s, legTop, 5, legH, { _, _ -> true }, { u, v -> .62 - u * .08 + (if (k == 1) -.12 else 0.0) + (if (v % 7 == 6) -.08 else 0.0) }, ramp(bottom))
            p.vol(s - (if (k == 0) 1 else 0), -bootH, 6, bootH, { u, v -> !(v == 0 && (u == 0 || u == 5)) }, { u, v -> .6 - u * .08 - v * .04 }, boot)
        }
        p.p(0, legTop + 6, OL)
        if ("overalls" in traits) for (y in legTop until legTop + 4) p.r(-5, y, 11, 1, bottom)
        if (coatLen > 0) p.vol(-7, legTop, 15, coatLen, { u, v -> kotlin.math.abs(u - 7) <= 6 + v / 3 }, { u, _ -> .68 - u * .035 }, ramp(coat))
    }

    private fun torso(p: Painter, bd: Body, coat: Int, top: Int, woman: Boolean, winter: Boolean, traits: Set<String>) {
        val h = bd.waist - bd.neck
        val w = bd.shoulder * 2 + 1
        val main = if ("sweater" in traits) top.dim(.1f) else coat
        p.vol(-bd.shoulder, bd.neck, w, h, { u, v ->
            val half = if (v < 2) bd.shoulder - (2 - v) else bd.shoulder - (v * (bd.shoulder - bd.hip) / h)
            kotlin.math.abs(u - bd.shoulder) <= half
        }, { u, v -> .74 - u * .45 / w - v * .012 }, ramp(main))
        // sleeves along the sides, darker where they turn away from the light
        for (v in 2 until h - 2) { p.p(-bd.shoulder + 1, bd.neck + v, main.dim(.22f)); p.p(bd.shoulder - 1, bd.neck + v, main.dim(.38f)) }
        val col = bd.neck
        when {
            winter -> {
                // a fur collar and the coat's buttons
                p.vol(-bd.shoulder + 1, col - 1, w - 2, 4, { _, _ -> true }, { u, v -> .7 - u * .04 - v * .06 + (if ((u + v) % 2 == 0) .08 else 0.0) }, R.felt.let { intArrayOf(rgb(0x3a2a20), rgb(0x5a4030), rgb(0x7a5a40), rgb(0x9a7a58), rgb(0xb89a78)) })
                for (y in col + 5 until bd.waist step 3) p.p(0, y, R.brass[4])
            }
            "tie" in traits -> {
                p.r(-2, col, 5, 3, rgb(0xf2ece0)); p.r(0, col + 1, 1, 7, rgb(0x842a24)); p.p(-1, col + 2, rgb(0x842a24)); p.p(1, col + 2, rgb(0x842a24))
                p.r(-3, col, 1, 6, main.dim(.4f)); p.r(3, col, 1, 6, main.dim(.4f))
            }
            "uniform" in traits -> {
                p.r(-1, col, 3, 2, rgb(0xf2ece0)); p.r(0, col + 2, 1, h - 2, main.dim(.45f))
                for (y in col + 3 until bd.waist step 3) p.p(1, y, R.brass[4])
                p.r(-5, col + 4, 3, 1, R.brass[3])
            }
            woman -> {
                p.r(-2, col, 5, 2, main.lit(.25f)); p.p(0, col + 2, main.lit(.25f))
            }
            else -> {
                p.p(-1, col, rgb(0xf2ece0)); p.p(1, col, rgb(0xf2ece0)); p.p(0, col + 1, SKIN[3])
                for (y in col + 3 until bd.waist step 3) p.p(0, y, main.dim(.5f))
            }
        }
        if ("vest" in traits && !winter) for (v in 1 until h) { val half = bd.shoulder - 1 - v / 5; for (x in listOf(-half, -half + 1, -half + 2, half - 2, half - 1, half)) p.p(x, bd.neck + v, rgb(0x3a3a30).let { if (x > 0) it.dim(.3f) else it }) }
        if ("overalls" in traits) { p.r(-4, col + 1, 2, h, rgb(0x2c3c64)); p.r(3, col + 1, 2, h, rgb(0x2c3c64)); p.r(-4, col + 8, 9, h - 8, rgb(0x2c3c64)) }
        if ("apron" in traits && !woman && !winter) { val ap = rgb(0x8a6a48); p.vol(-4, col + 4, 9, -col - 4 - 8, { _, _ -> true }, { u, _ -> .65 - u * .04 }, ramp(ap), ap.dim(.5f)) }
        if ("apron" in traits && woman && !winter) { val ap = rgb(0xf2ece0); p.vol(-3, col + 6, 7, h - 6, { _, _ -> true }, { u, _ -> .7 - u * .04 }, ramp(ap), ap.dim(.4f)) }
        if ("shawl" in traits || (winter && woman && bd.headH > 11)) {
            // a knitted shawl over the shoulders, ending in a point with a fringe
            val sc = if (winter) rgb(0x8a5a8a) else rgb(0x6a2a3a)
            p.vol(-bd.shoulder - 1, col - 1, w + 2, 10, { u, v -> kotlin.math.abs(u - bd.shoulder - 1) <= bd.shoulder + 1 - v * .9 }, { u, v -> .7 - u * .03 - v * .02 + (if ((u + v) % 4 == 0) .12 else 0.0) }, ramp(sc))
            for (x in -bd.shoulder until bd.shoulder + 1 step 2) if (kotlin.math.abs(x) > 2) p.p(x, col + 10 - (bd.shoulder + 1 - kotlin.math.abs(x)) + 0, sc.lit(.3f))
            p.r(-bd.shoulder - 1, col + 1, 1, 6, sc.lit(.3f)); p.r(bd.shoulder + 1, col + 1, 1, 6, sc.dim(.2f))
        }
        if ("beads" in traits && !winter) for (k in -3..3) p.p(k, col + 1 + (if (kotlin.math.abs(k) < 2) 1 else 0), if (k % 2 == 0) rgb(0xe83a3a) else rgb(0xf8e0a0))
        if ("satchel" in traits) { p.vol(bd.shoulder - 2, col + 5, 6, 6, { _, _ -> true }, { u, _ -> .6 - u * .06 }, R.red); p.r(bd.shoulder - 1, col + 7, 4, 1, R.brass[4]) }
    }

    private fun letter(p: Painter, bd: Body, hand: Int) {
        // forearms come round to the front, both hands holding the opened letter at the chest
        val y = bd.neck + (bd.waist - bd.neck) * 2 / 3
        val s = bd.shoulder
        p.vol(-3, y - 3, 7, 5, { _, _ -> true }, { u, v -> .82 - u * .03 - v * .02 }, R.paper, R.paper[0])
        p.r(-2, y - 2, 5, 1, rgb(0x6a7aa0)); p.r(-2, y, 3, 1, rgb(0x6a7aa0))
        // forearms bending in from the elbows
        for (k in 0..2) { p.p(-s + 1 + k, y - 2 + k / 2, OL); p.p(s - 1 - k, y - 2 + k / 2, OL) }
        p.r(-5, y - 1, 2, 2, hand); p.r(4, y - 1, 2, 2, hand.dim(.15f))
        p.p(-4, y + 1, hand.dim(.3f)); p.p(4, y + 1, hand.dim(.4f))
    }

    private fun head(p: Painter, bd: Body, sprite: String, hair: Int, scarf: Int?, winter: Boolean, traits: Set<String>) {
        val w = bd.headW
        val h = bd.headH
        val x0 = -w / 2
        val y0 = bd.head
        val old = sprite.endsWith("_old")
        val man = !sprite.startsWith("woman") && sprite != "girl"
        val hr = ramp(hair)
        // hair falling behind the shoulders comes first
        if (scarf == null) when {
            "long" in traits -> p.vol(x0 - 1, y0 + 3, w + 2, h + 4, { u, v -> v < h + 1 || u < 3 || u > w - 2 }, { u, v -> .6 - u * .04 - v * .01 }, hr)
            "bob" in traits -> p.vol(x0 - 1, y0 + 2, w + 2, h - 1, { _, _ -> true }, { u, _ -> .62 - u * .04 }, hr)
        }
        // neck and face
        p.r(-1, bd.neck - 1, 3, 2, SKIN[3])
        val fx = x0 + 1
        val fy = y0 + 2
        val fw = w - 2
        val fh = h - 2
        p.vol(fx, fy, fw, fh, ell(fw / 2.0, fh / 2.0 - .5, fw / 2.0 + .3, fh / 2.0 + .4), sph(fw / 2.0 - 1.5, fh / 2.0 - 2.0, fw / 2.0 + 1, fh / 2.0 + 1, .3, .1), SKIN)
        p.p(fx - 1, fy + fh / 2, SKIN[3]); p.p(fx + fw, fy + fh / 2, SKIN[2])
        val ey = fy + fh / 2 - 1
        val exL = fx + 2
        val exR = fx + fw - 3
        // eyes, brows, nose, mouth, cheeks
        val eye = rgb(0x2a1a10)
        if (old && "glasses" !in traits) { p.p(exL, ey, eye); p.p(exR, ey, eye) }
        else { p.p(exL, ey, eye); p.p(exL, ey + 1, eye); p.p(exR, ey, eye); p.p(exR, ey + 1, eye); p.p(exL, ey, rgb(0x5a4030)) }
        val brow = if (old) hair.dim(.2f) else hair.dim(.25f)
        p.p(exL - 1, ey - 2, brow); p.p(exL, ey - 2, brow); p.p(exR, ey - 2, brow); p.p(exR + 1, ey - 2, brow)
        p.p(fx + fw / 2, ey + 2, SKIN[2]); p.p(fx + fw / 2 - 1, ey + 3, SKIN[2].lit(.1f))
        val mouth = if (man) SKIN[1] else rgb(0xb84a4a)
        p.p(fx + fw / 2 - 1, ey + 4, mouth); p.p(fx + fw / 2, ey + 4, mouth)
        if (!man || sprite == "girl" || old) { p.p(exL - 1, ey + 2, rgb(0xe88a7a)); p.p(exR + 1, ey + 2, rgb(0xe8908a)) }
        if (old) { p.p(exL - 1, ey + 1, SKIN[2]); p.p(exR + 1, ey + 1, SKIN[2]) }
        if ("stubble" in traits) for (j in 0 until 3) for (i in 1 until fw - 1) if ((i + j) % 2 == 0) p.p(fx + i, ey + 3 + j, hair.dim(.1f).let { mix(it, SKIN[3], .55f) })
        if ("mustache" in traits || "beard" in traits) for (i in -2..1) p.p(fx + fw / 2 + i, ey + 3, hair.dim(.12f))
        if ("beard" in traits) {
            p.vol(fx, ey + 3, fw, 7, { u, v -> kotlin.math.abs(u - fw / 2.0 + .5) <= fw / 2.0 - v * .5 }, { u, v -> .7 - u * .05 - v * .03 + (if ((u + v) % 3 == 0) .08 else 0.0) }, hr, hair.dim(.5f))
            p.p(fx + fw / 2 - 1, ey + 4, SKIN[1]); p.p(fx + fw / 2, ey + 4, SKIN[1])
        }
        if ("glasses" in traits) {
            // thin round rims: top and bottom, the outer sides, a bridge over the nose
            val gl = if (old) rgb(0x8a7a5a) else rgb(0x3a3a44)
            for (cxg in listOf(exL, exR)) { p.p(cxg - 1, ey - 1, gl); p.p(cxg, ey - 1, gl); p.p(cxg + 1, ey - 1, gl); p.p(cxg, ey + 2, gl) }
            p.p(exL - 2, ey, gl); p.p(exR + 2, ey, gl); p.p(fx + fw / 2, ey, gl)
            p.p(exL + 1, ey, rgb(0xe8f0f4))
        }
        if ("earrings" in traits) { p.p(fx - 1, ey + 3, R.gold[4]); p.p(fx + fw, ey + 3, R.gold[3]) }
        if ("pipe" in traits) { p.r(fx + fw / 2 + 1, ey + 4, 4, 1, rgb(0x3a2214)); p.r(fx + fw / 2 + 4, ey + 2, 2, 3, rgb(0x55331e)) }

        // hair, or whatever covers it
        val hat = when {
            "beret" in traits -> "beret"
            "cap_rail" in traits -> "cap_rail"
            "cap_sea" in traits -> "cap_sea"
            "straw" in traits && !winter -> "straw"
            winter && scarf == null && sprite == "girl" -> "knit"
            winter && scarf == null && (sprite == "woman_young") -> "knit"
            winter && man -> "ushanka"
            "kepka" in traits -> "kepka"
            else -> null
        }
        if (scarf != null && hat == null) {
            // a headscarf tied under the chin, with a pattern of little dots
            val sr = ramp(scarf)
            p.vol(x0, y0, w, h - 3, { u, v -> v < 4 || u < 1 || u > w - 2 || (v == 4 && (u < 3 || u > w - 4)) }, { u, v -> .72 - u * .04 - v * .02 }, sr)
            for (j in 0 until h - 3) for (i in 0 until w) if ((i + j * 2) % 4 == 0 && (j < 4 || i < 1 || i > w - 2)) p.p(x0 + i, y0 + j, scarf.lit(.45f))
            p.p(x0 + 1, y0 + h - 2, scarf.dim(.2f)); p.p(x0 + w - 2, y0 + h - 2, scarf.dim(.35f))
            p.p(x0 + w / 2 - 1, y0 + h + 1, scarf); p.p(x0 + w / 2, y0 + h + 1, scarf.dim(.2f)); p.p(x0 + w / 2 + 1, y0 + h + 2, scarf.dim(.3f)); p.p(x0 + w / 2 - 2, y0 + h + 2, scarf.dim(.1f))
            return
        }
        // the hair itself, shaped by who wears it
        when {
            "bald" in traits -> {
                p.vol(x0, y0 + 3, 3, 6, { _, _ -> true }, { _, v -> .7 - v * .05 }, hr); p.vol(x0 + w - 3, y0 + 3, 3, 6, { _, _ -> true }, { _, v -> .4 - v * .05 }, hr)
                p.p(fx + 3, fy + 1, SKIN[5])
            }
            hat != null && hat != "beret" -> Unit
            man -> {
                p.vol(x0, y0, w, 6, { u, v -> v < 3 || u < 2 || u > w - 3 || (sprite == "teen" && v < 4 && u % 3 != 0) }, { u, v -> .7 - u * .04 - v * .05 }, hr)
                if (sprite == "teen") for (k in 0 until 4) p.p(x0 + 2 + k * 2, y0 - 1, hair)
                p.p(x0 + 3, y0 + 3, hair); p.p(x0 + 4, y0 + 3, hair)
            }
            else -> {
                p.vol(x0, y0, w, 7, { u, v -> v < 3 || u < 2 || u > w - 3 || (v == 3 && u < w / 2 + 1) }, { u, v -> .72 - u * .04 - v * .04 }, hr)
                when {
                    "bun" in traits -> p.vol(x0 + w / 2 - 3, y0 - 4, 7, 6, ell(3.5, 3.0, 3.5, 3.0), sph(2.5, 2.0, 3.5, 3.0, .3), hr)
                    "braid" in traits -> for (j in 0 until 16) { val c = if (j % 3 == 0) hair.dim(.3f) else hair; p.p(x0 + w - 2 + (if (j < 4) 0 else 1), y0 + h - 2 + j, c); p.p(x0 + w - 1 + (if (j < 4) 0 else 1), y0 + h - 2 + j, c.dim(.15f)) }
                    "ponytail" in traits -> p.vol(x0 + w - 2, y0 + 2, 4, 10, { u, v -> u < 3 - v / 5 + 1 }, { u, v -> .6 - u * .1 - v * .02 }, hr)
                    "curls" in traits -> for (k in 0 until 9) p.vol(x0 - 1 + (k % 5) * 3, y0 - 1 + (k / 5) * 3 + (if (k >= 5) 1 else 0), 4, 4, ell(2.0, 2.0, 2.0, 2.0), sph(1.5, 1.5, 2.0, 2.0, .3), hr, null)
                }
                if (sprite == "girl") for (s in listOf(-1, w)) {
                    p.vol(x0 + s - 1, y0 + 4, 3, 8, { _, _ -> true }, { _, v -> .6 - v * .03 }, hr)
                    p.p(x0 + s - 1, y0 + 4, rgb(0xe83a4a)); p.p(x0 + s + 1, y0 + 4, rgb(0xe83a4a)); p.p(x0 + s, y0 + 4, rgb(0xa82a3a))
                }
            }
        }
        when (hat) {
            "ushanka" -> {
                val fur = ramp(rgb(0x6a5040))
                p.vol(x0 - 1, y0 - 2, w + 2, 7, { u, v -> !(v == 0 && (u < 2 || u > w - 1)) }, { u, v -> .7 - u * .04 - v * .04 + (if ((u + v) % 2 == 0) .06 else 0.0) }, fur)
                p.vol(x0 - 1, y0 + 4, 3, 7, { _, _ -> true }, { _, v -> .6 - v * .04 }, fur); p.vol(x0 + w - 2, y0 + 4, 3, 7, { _, _ -> true }, { _, v -> .35 - v * .04 }, fur)
                p.r(x0 + 1, y0 + 2, w - 2, 1, rgb(0x3a2a20))
            }
            "knit" -> {
                val kc = if (sprite == "girl") rgb(0xc04a3a) else rgb(0x4a6aa8)
                p.vol(x0, y0 - 1, w, 6, { u, v -> !(v == 0 && (u < 2 || u > w - 3)) }, { u, v -> .7 - u * .04 - v * .04 + (if (u % 2 == 0) .08 else 0.0) }, ramp(kc))
                p.r(x0, y0 + 4, w, 2, rgb(0xf2ece0)); p.vol(x0 + w / 2 - 2, y0 - 4, 4, 4, ell(2.0, 2.0, 2.0, 2.0), sph(1.5, 1.5, 2.0, 2.0, .4), ramp(rgb(0xf2ece0)), null)
            }
            "kepka" -> {
                val kc = rgb(0x4a4a50)
                p.vol(x0, y0, w, 5, { u, v -> !(v == 0 && (u < 2 || u > w - 3)) }, { u, v -> .65 - u * .04 - v * .03 }, ramp(kc))
                p.r(x0 - 2, y0 + 4, w / 2 + 2, 2, kc.dim(.35f)); p.r(x0 - 2, y0 + 4, w / 2 + 2, 1, kc.dim(.15f))
                p.vol(x0 + w - 3, y0 + 4, 3, 3, { _, _ -> true }, { _, _ -> .5 }, hr, null)
            }
            "beret" -> {
                val bc = rgb(0xa83a3a)
                p.vol(x0 - 2, y0 - 2, w + 3, 5, ell((w + 3) / 2.0, 2.5, (w + 3) / 2.0, 2.6), sph((w + 3) / 2.0 - 2, 1.5, (w + 3) / 2.0, 3.0, .35), ramp(bc))
                p.p(x0 + w / 2, y0 - 3, bc.dim(.3f))
            }
            "cap_rail" -> {
                val cc = rgb(0x1e2430)
                p.vol(x0, y0 - 1, w, 5, { _, _ -> true }, { u, v -> .6 - u * .04 - v * .04 }, ramp(cc))
                p.r(x0, y0 + 3, w, 1, rgb(0x842a24)); p.r(x0 + 1, y0 + 4, w - 2, 2, rgb(0x101014)); p.p(x0 + w / 2, y0 + 1, R.brass[4]); p.p(x0 + w / 2 - 1, y0 + 1, R.brass[3])
            }
            "cap_sea" -> {
                p.vol(x0, y0 - 1, w, 4, { _, _ -> true }, { u, v -> .8 - u * .03 - v * .03 }, R.cream)
                p.r(x0, y0 + 3, w, 1, rgb(0x1e2430)); p.r(x0 + 1, y0 + 4, w - 2, 2, rgb(0x101014)); p.p(x0 + w / 2, y0 + 3, R.brass[4])
            }
            "straw" -> {
                p.vol(x0 + 1, y0 - 3, w - 2, 5, { _, _ -> true }, { u, v -> .7 - u * .04 - v * .04 + (if ((u + v) % 3 == 0) -.1 else 0.0) }, R.honey)
                p.r(x0 - 3, y0 + 2, w + 6, 2, R.honey[3]); p.r(x0 - 3, y0 + 3, w + 6, 1, R.honey[1]); p.r(x0 + 1, y0 + 1, w - 2, 1, rgb(0x842a24))
            }
        }
        if ("headphones" in traits) {
            val hp = rgb(0x2a2a30)
            for (i in 1 until w - 1) p.p(x0 + i, y0 - 1 - (if (i in 3 until w - 3) 1 else 0), hp)
            p.vol(x0 - 2, y0 + 4, 3, 5, { _, _ -> true }, { _, _ -> .5 }, R.iron); p.vol(x0 + w - 1, y0 + 4, 3, 5, { _, _ -> true }, { _, _ -> .3 }, R.iron)
        }
    }

    // ------------------------------------------------------------ the postman and the dog

    /** The postman in his uniform with the bag, feet at (x+7, feetY). */
    fun postman(b: Buf, x: Int, feetY: Int, winter: Boolean, frame: Int = 0) {
        val cx = x + 7
        val p = Painter(b, cx, feetY)
        val bd = body("man")
        val uni = rgb(0x2c3c64)
        for (i in -9..9) b.mul(cx + i, feetY, rgb(0x303040), .35f)
        legs(p, bd, rgb(0x2a2a34), uni, winter, false, emptySet())
        torso(p, bd, if (winter) uni.dim(.15f) else uni, uni, false, winter, setOf("uniform"))
        // the strap across the chest and the leather bag on the hip
        for (k in 0 until 16) p.p(-6 + k * 12 / 16, bd.neck + 1 + k, R.leather[2])
        p.vol(3, bd.waist - 7, 9, 9, { u, v -> !(v == 8 && (u == 0 || u == 8)) }, { u, v -> .7 - u * .05 - v * .02 }, R.leather)
        p.r(3, bd.waist - 7, 9, 3, R.leather[4]); p.p(7, bd.waist - 5, R.brass[4])
        p.r(4, bd.waist - 9, 4, 3, rgb(0xf8eed4)); p.r(5, bd.waist - 10, 3, 1, rgb(0xe8dcc0))
        head(p, bd, "man", rgb(0x3a2216), null, winter, if (winter) emptySet() else setOf("postcap"))
        if (!winter) {
            val cc = rgb(0x1e2a4a)
            val x0 = -bd.headW / 2
            val y0 = bd.head
            p.vol(x0, y0 - 1, bd.headW, 5, { _, _ -> true }, { u, v -> .65 - u * .04 - v * .04 }, ramp(cc))
            p.r(x0, y0 + 3, bd.headW, 1, rgb(0xe8b443)); p.r(x0 + 1, y0 + 4, bd.headW - 2, 2, rgb(0x08080c)); p.p(x0 + bd.headW / 2, y0 + 1, R.brass[4])
        }
        if (frame % 2 == 1) p.p(-6, -1, rgb(0x303040))
    }

    private fun postmanPal(winter: Boolean) = mapOf(
        'k' to rgb(0x140c08), 'N' to rgb(0x0e1426), 'n' to rgb(0x1e2a4a), 'b' to rgb(0x2c3c64), 'B' to rgb(0x405284),
        'V' to rgb(0x08080c), 'y' to rgb(0xe8b443), 'f' to rgb(0xf2c09a), 'F' to rgb(0xc4805e), 'r' to rgb(0xe48a7a),
        'h' to rgb(0x3a2216), 'L' to rgb(0x2a170e), 'l' to rgb(0x5c3820), 'u' to rgb(0x8a5a32), 'c' to rgb(0xf8eed4),
        'P' to rgb(0x2a2a34), 'p' to rgb(0x3c3c48), 'S' to rgb(if (winter) 0x6e6862 else 0x140c08), 'e' to rgb(0x2a1a10),
    )

    private val MINI = listOf("..nnn..", ".nnbnn.", ".VVVVV.", "..fff..", "..fff..", ".nnbnn.", "nnbnnnl", "fnbnnul", ".nbnnuu", ".nnnn..")
    private val MINI_HAT = listOf("..uuu..", ".uuuuu.", ".VuuuV.")
    private val MINI_LEGS = listOf(listOf(".P..P..", ".k..k.."), listOf("..PP...", "..kk..."))

    /** The postman as a tiny figure on the map, feet at (x+3, feetY). */
    fun mini(b: Buf, x: Int, feetY: Int, winter: Boolean, frame: Int) {
        val pal = postmanPal(winter)
        b.spr(MINI, x, feetY - 12, pal)
        if (winter) b.spr(MINI_HAT, x, feetY - 12, mapOf('u' to rgb(0x5a4030), 'V' to rgb(0x3a2a20)))
        b.spr(MINI_LEGS[frame % 2], x, feetY - 2, pal)
    }

    private val DOG = listOf(
        ".kk.......kk..",
        "kTtk.....kTTk.",
        "kTtk....ktttTk",
        ".kTk...ktetttnk",
        "..kk..ktttttwk.",
        "...kkktttttTk..",
        "..kTtttttttTk..",
        "..kTtwwwwttTk..",
    )
    private val DOG_LEGS = listOf(listOf("..kTk.kTk.kTk..", "..kk..kk..kk..."), listOf("...kTkkTk.kTk..", "...kk.kk..kk..."))
    private val DOG_SIT = listOf(
        ".........kk...",
        "........kTTk..",
        "..kk...ktttTk.",
        ".kTtk.ktetttnk",
        ".kTtk.kttttwk.",
        "..kTk.kttTtk..",
        "...kkktttwtk..",
        "....kTttwwtk..",
        "....kTttwwtk..",
        "...kTTttwwTk..",
        "...kTtk.kTTk..",
        "...kkk..kkk...",
    )
    private val DOG_MINI = listOf("t.....tt", ".ttttttk", ".tttttt.")
    private val dogPal = mapOf('k' to rgb(0x2a1608), 't' to rgb(0xc99a5e), 'T' to rgb(0x8e643a), 'w' to rgb(0xecd2a2), 'e' to rgb(0x140c08), 'n' to rgb(0x3a2010))

    fun dog(b: Buf, x: Int, feetY: Int, frame: Int) {
        b.spr(DOG, x, feetY - 10, dogPal)
        b.spr(DOG_LEGS[frame % 2], x, feetY - 2, dogPal)
    }

    fun dogSit(b: Buf, x: Int, feetY: Int, wag: Int) {
        b.spr(DOG_SIT, x, feetY - DOG_SIT.size, dogPal)
        b.p(x + (wag % 2) + 1, feetY - 4, dogPal.getValue('t'))
        b.p(x + (wag % 2), feetY - 5, dogPal.getValue('t'))
    }

    fun dogMini(b: Buf, x: Int, feetY: Int, frame: Int) {
        b.spr(DOG_MINI, x, feetY - 4, dogPal)
        b.spr(listOf(if (frame % 2 == 0) ".t.t.t.t" else "..t.t.t."), x, feetY - 1, dogPal)
    }

    /** Bublik asleep on his mat: head on his paws, an ear flopped over, the tail curled into a bagel. */
    fun dogLying(b: Buf, x: Int, y: Int, br: Double) {
        val fur = intArrayOf(rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52), rgb(0xd8b07a), rgb(0xecd2a2))
        val ol = rgb(0x2a1608)
        // the mat
        for (j in 0 until 4) for (i in -3..32) b.p(x + i, y + 10 + j, if ((i + j) % 4 < 2) rgb(0xa33a2c) else rgb(0x842a24))
        for (i in -3..32 step 2) b.p(x + i, y + 14, rgb(0xd8c4a0))
        // body
        b.vol(x + 6, y, 22, 12, ell(11.0, 6.5 - br * .4, 11.0, 5.0 + br * .5), sph(8.0, 3.0, 11.0, 6.0, .3), fur, ol)
        // the tail: a ring on the rump
        for (a in 0 until 14) {
            val an = a / 14.0 * 2 * Math.PI
            b.p(x + 25 + (kotlin.math.cos(an) * 3).toInt(), y + 1 + (kotlin.math.sin(an) * 2.5).toInt(), if (a < 7) fur[3] else fur[2])
        }
        // front paws stretched forward
        b.vol(x - 2, y + 7, 10, 4, ell(5.0, 2.0, 5.0, 2.0), sph(4.0, 1.0, 5.0, 2.0, .45), fur, ol)
        // head resting on the paws
        b.vol(x - 1, y - 1, 11, 9, ell(5.5, 4.5, 5.5, 4.5), sph(4.0, 3.0, 5.5, 4.5, .3), fur, ol)
        b.vol(x - 5, y + 3, 6, 5, ell(3.0, 2.5, 3.0, 2.5), sph(2.0, 1.5, 3.0, 2.5, .5), fur, ol)
        b.p(x - 5, y + 4, rgb(0x140c08)); b.p(x - 4, y + 4, rgb(0x140c08))
        b.p(x + 1, y + 3, rgb(0x3a2010)); b.p(x + 2, y + 3, rgb(0x3a2010))
        // the floppy ear
        for (j in 0 until 5) b.r(x + 4, y + j, 3 - j / 3, 1, fur[0])
        b.p(x + 4, y - 1, ol); b.p(x + 5, y - 1, ol)
    }
}
