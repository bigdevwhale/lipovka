package app.lipovka.ui.art

/**
 * The people of Lipovka, drawn from parts: a head, a torso holding the opened letter, and legs.
 * Each resident's look picks the hair, the top and the bottom colours; in winter everyone wears a hat
 * and felt boots.
 */
object People {
    private val HEAD_W_YOUNG = listOf(
        "....kkkkkk....",
        "...khHHHHhk...",
        "..khHHHHHHhk..",
        "..khHhhhhHhk..",
        ".khhffffffhhk.",
        ".khffffffffhk.",
        ".khfeffffefhk.",
        ".khrffFfffrhk.",
        ".khffmmmfffhk.",
        "..khFffffFhhk.",
        "..khkFFFFkkhk.",
    )
    private val HEAD_W = listOf(
        ".....kkkk.....",
        "....khHHhk....",
        "...kkhhhhkk...",
        "..khHHHHHHhk..",
        "..khffffffhk..",
        "..kffffffffk..",
        "..kfeffffefk..",
        "..kfrfFffrfk..",
        "..kffmmmfffk..",
        "...kFffffFk...",
        "....kFFFFk....",
    )
    private val HEAD_SCARF = listOf(
        "....kkkkkk....",
        "...kqqQQqqk...",
        "..kqqqqqqqQk..",
        ".kqqkkkkkkqQk.",
        ".kqkffffffkQk.",
        ".kqkfeffefkQk.",
        ".kqkfFffFfkqk.",
        ".kqkfrmmrfkqk.",
        ".kqqkfFFfkqqk.",
        "kqqqqkkkkqqqQk",
        "kQqqqqqqqqqQQk",
    )
    private val HEAD_M_YOUNG = listOf(
        "...kkkkkkk....",
        "..khhHHHhhk...",
        ".khHHHHhhhhk..",
        ".khhffffffhk..",
        ".kffffffffffk.",
        ".kffeffffeffk.",
        ".kfffFffffffk.",
        ".kffrffFfrffk.",
        "..kfffmmfffk..",
        "..kFffffffFk..",
        "...kFFFFFFk...",
    )
    private val HEAD_M = listOf(
        "...kkkkkkk....",
        "..khhhhhhhk...",
        ".khHHHhhhhhk..",
        ".khffffffffk..",
        ".kffffffffffk.",
        ".kffeffffeffk.",
        ".kfffFffffffk.",
        ".kffhhhhhhffk.",
        "..kfffmmfffk..",
        "..kFffffffFk..",
        "...kFFFFFFk...",
    )
    private val HEAD_M_OLD = listOf(
        "...kkkkkkkk...",
        "..kqqqQQqqqk..",
        ".kqqqqqqqqqQk.",
        "kkkkkkkkkkkkkk",
        ".kffffffffffk.",
        ".kffeffffeffk.",
        ".kfffFffffffk.",
        ".khhffFfffhhk.",
        ".khhhhmmhhhhk.",
        "..khhhhhhhhk..",
        "...khhhhhhk...",
    )
    private val HEAD_HAT = listOf(
        "..kkkkkkkkkk..",
        ".kuuuuUUuuuuk.",
        "kuuuuuuuuuuuUk",
        "kuUkkkkkkkkUuk",
        "kuUkffffffkUuk",
        "kuUfeffffefUuk",
        "kuUffFfffffUuk",
        ".kUfrffFffrUk.",
        ".kUffmmmfffUk.",
        "..kFffffffFk..",
        "...kFFFFFFk...",
    )
    private val HEAD_GIRL = listOf(
        "....kkkkkk....",
        "...khHHHHhk...",
        "..khHHHHHHhk..",
        "ykkhffffffhkky",
        "yhkffffffffkhy",
        ".hkfeffffefkh.",
        ".hkfrfFffrfkh.",
        ".hkffmmmfffkh.",
        "..kkFffffFkk..",
        "....kFFFFk....",
    )
    private val HEAD_KID_HAT = listOf(
        "......kk......",
        ".....kyyk.....",
        "....kqqqqk....",
        "...kqqQqqqk...",
        "..kqqqqqqqQk..",
        "..kyyyyyyyyk..",
        "..kfeffffefk..",
        "..kfrfFffrfk..",
        "..kffmmmfffk..",
        "...kFffffFk...",
    )
    private val HEAD_TEEN = listOf(
        "..k.kkkkk.k...",
        "..khkhHHhkhk..",
        ".khHHHHHHhhk..",
        ".khhffffffhk..",
        ".kffffffffffk.",
        ".kffeffffeffk.",
        ".kfffFffffffk.",
        ".kffffffFfffk.",
        "..kfffmmfffk..",
        "..kFffffffFk..",
        "...kFFFFFFk...",
    )
    private val TORSO_W = listOf(
        "...kkTtkkkkTtkk.",
        "..kttyttttttyTk.",
        ".kttttttttttttTk",
        ".ktTtttttytttTTk",
        "kttTttttttttttTk",
        "ktTttttffcccttTk",
        "kTTtttttffcCCcTk",
        ".kTTttkkcccccTk.",
        ".kkTTk.kcCCCck..",
        "..kTtkkkcccck...",
    )
    private val TORSO_M = listOf(
        "...kkkTTTTkkk...",
        "..kttTtwwtTttk..",
        ".kttttTwwTttttk.",
        ".ktTtttTyTtttTk.",
        "kttTttttyttttTTk",
        "ktTtttttttttttTk",
        "kTTttttffccctTTk",
        "kfkTtttffcCCcTkk",
        ".kkTTtkkcccccTk.",
        "..kTTTkkcCCCck..",
        "..kbkkkkkkkkk...",
    )
    private val TORSO_KID = listOf(
        "..kkTTTTkk..",
        ".kttTwwTttk.",
        "kttttTTttttk",
        "kTtttttttTTk",
        "kfTtttffccTk",
        ".kkTtkfcCCck",
        "..kTtkkccck.",
        "..kkkkkkkk..",
    )
    private val LEGS_SKIRT = listOf(
        "...kbkkkkkbk....",
        "...kbBbbbBbk....",
        "..kbBbbbbbBbk...",
        "..kbBbbbbbBbk...",
        ".kbBbbbbbbbBbk..",
        ".kbBbbbbbbbBbk..",
        ".kbbbbbbbbbbbk..",
        "kbBbbbbbbbbbBbk.",
        "kbBbbbbbbbbbbbk.",
        "kbbbbbbbbbbbbbk.",
        "kBBBBBBBBBBBBBk.",
        ".kkkkkkkkkkkkk..",
        "....kssk.kssk...",
        "....kkkk.kkkk...",
    )
    private val LEGS_TROUSERS = listOf(
        "..kbbbbbbbbbk...",
        "..kbBbbbbbBbk...",
        "..kbBbbkbbBbk...",
        "..kbBbbkbbBbk...",
        "..kbBbbkbbBbk...",
        "..kbbbbkbbbbk...",
        "..kbBbbkbbBbk...",
        "..kbBbbkbbBbk...",
        "..kbbbbkbbbbk...",
        "..kbbbkkkbbbk...",
        "..kssskkksssk...",
        ".kssssk.kssssk..",
        ".kkkkkk.kkkkkk..",
    )
    private val LEGS_KID_SKIRT = listOf(
        "..kbbbbbbbk.",
        ".kbBbbbbbBbk",
        ".kbbbbbbbbbk",
        "kbBbbbbbbbBk",
        "kkkkkkkkkkkk",
        "...kfk.kfk..",
        "...kfk.kfk..",
        "..kssk.kssk.",
        "..kkkk.kkkk.",
    )

    private val HAIR = mapOf(
        "brown" to (0x5c3826L to 0x3a2216L), "grey" to (0xa8a8b0L to 0x7a7a84L), "white" to (0xe8e8ecL to 0xb8b8c4L),
        "fair" to (0xd8b070L to 0xa87e40L), "black" to (0x2e2628L to 0x141014L), "red" to (0xb85a28L to 0x7a3416L),
    )
    private val SCARF = mapOf("scarf_blue" to (0x4a6aa8L to 0x2c4478L), "scarf_red" to (0xc04a3aL to 0x842a24L), "scarf_green" to (0x4a8a5aL to 0x2c5a38L))
    private val TOP = mapOf(
        "red" to Triple(0xac3e2cL, 0x6e1f1fL, 0xe8b443L), "brown" to Triple(0x7c4e2cL, 0x4a2c1aL, 0xc8952eL),
        "blue" to Triple(0x3a5a9cL, 0x1e2a4aL, 0xe8e0d0L), "green" to Triple(0x3c6c44L, 0x1e3a24L, 0xe8b443L),
        "white" to Triple(0xe8e2d4L, 0xa8a090L, 0xa33a2cL), "yellow" to Triple(0xe0a830L, 0xa06418L, 0xfbf3dcL),
        "violet" to Triple(0x6a4a90L, 0x3a2458L, 0xe8b443L), "cream" to Triple(0xecdcb6L, 0xb4a282L, 0x5a74aaL),
        "black" to Triple(0x2a2a30L, 0x141418L, 0xa8a8b0L), "grey" to Triple(0x6c6c74L, 0x3a3a40L, 0xcacaceL),
    )
    private val BOTTOM = mapOf(
        "green" to (0x304c32L to 0x16261aL), "grey" to (0x55504cL to 0x2a2828L), "blue" to (0x2c3c64L to 0x141c34L),
        "brown" to (0x5c3820L to 0x2a170eL), "black" to (0x26262aL to 0x101014L),
    )

    fun height(sprite: String) = if (sprite == "girl") 27 else 35

    /**
     * Draws a resident standing with the opened letter, feet at (cx, feetY). [look] is hair, top,
     * bottom; [winter] puts on hats and felt boots.
     */
    fun draw(b: Buf, sprite: String, look: List<String>, cx: Int, feetY: Int, winter: Boolean) {
        val hairKey = look.getOrElse(0) { "brown" }
        val (h1, h2) = HAIR[hairKey] ?: (0x5c3826L to 0x3a2216L)
        val (t1, t2, ty) = TOP[look.getOrElse(1) { "red" }] ?: TOP.getValue("red")
        val (b1, b2) = BOTTOM[look.getOrElse(2) { "grey" }] ?: BOTTOM.getValue("grey")
        val scarf = SCARF[hairKey] ?: (t1 to t2)
        val fur = if (sprite == "man_old") 0x5a4a40L to 0x3a2e28L else 0x6a5040L to 0x48362aL
        val pal = mutableMapOf(
            'k' to rgb(0x140c08), 'h' to rgb(h1), 'H' to rgb(h1).lit(.18f), 'f' to rgb(0xf2c09a), 'F' to rgb(0xc4805e),
            'e' to rgb(0x2a1a10), 'r' to rgb(0xe88a7a), 'm' to rgb(0xa84a3a), 't' to rgb(t1), 'T' to rgb(t2), 'y' to rgb(ty),
            'b' to rgb(b1), 'B' to rgb(b2), 's' to rgb(if (winter) 0x6e6862 else 0x2a1a12), 'w' to rgb(0xf2ece0),
            'c' to rgb(0xfbf3dc), 'C' to rgb(0xd8c8a0), 'q' to rgb(scarf.first), 'Q' to rgb(scarf.second),
            'u' to rgb(fur.first), 'U' to rgb(fur.second),
        )
        if (sprite == "man_old") { pal['q'] = rgb(if (winter) fur.first else 0x3a3a44); pal['Q'] = rgb(if (winter) fur.second else 0x24242c); pal['h'] = rgb(h1); pal['H'] = rgb(h1) }
        val head: List<String>
        val torso: List<String>
        val legs: List<String>
        val kid = sprite == "girl"
        when (sprite) {
            "woman_young" -> { head = if (winter) HEAD_SCARF else HEAD_W_YOUNG; torso = TORSO_W; legs = LEGS_SKIRT }
            "woman" -> { head = if (winter) HEAD_SCARF else HEAD_W; torso = TORSO_W; legs = LEGS_SKIRT }
            "woman_old" -> { head = HEAD_SCARF; torso = TORSO_W; legs = LEGS_SKIRT }
            "man_young" -> { head = if (winter) HEAD_HAT else HEAD_M_YOUNG; torso = TORSO_M; legs = LEGS_TROUSERS }
            "man" -> { head = if (winter) HEAD_HAT else HEAD_M; torso = TORSO_M; legs = LEGS_TROUSERS }
            "man_old" -> { head = HEAD_M_OLD; torso = TORSO_M; legs = LEGS_TROUSERS }
            "teen" -> { head = if (winter) HEAD_HAT else HEAD_TEEN; torso = TORSO_M; legs = LEGS_TROUSERS }
            else -> { head = if (winter) HEAD_KID_HAT else HEAD_GIRL; torso = TORSO_KID; legs = LEGS_KID_SKIRT }
        }
        if (winter && (sprite.startsWith("woman"))) { pal['q'] = rgb(ty).dim(.1f); pal['Q'] = rgb(ty).dim(.4f) }
        if (winter && kid) { pal['q'] = rgb(0xc04a3a); pal['Q'] = rgb(0x842a24); pal['y'] = rgb(0xfbf3dc) }
        // shadow
        for (i in -8..8) b.mul(cx + i, feetY, rgb(0x303040), .35f)
        val legsTop = feetY - legs.size
        val torsoTop = legsTop - torso.size + if (kid) 0 else 1
        val headTop = torsoTop - head.size + 1
        b.spr(legs, cx - legs[0].length / 2, legsTop, pal)
        b.spr(torso, cx - torso[0].length / 2, torsoTop, pal)
        b.spr(head, cx - head[0].length / 2 + if (kid) 0 else 1, headTop, pal)
    }

    // ------------------------------------------------------------ the postman and the dog

    private val POSTMAN = listOf(
        "....kkkkk.....",
        "...knbbBnk....",
        "..knnbbBBnk...",
        "..kNNyyNNNk...",
        ".kVVVVVVVVVk..",
        "..khffffFk....",
        "..kfefefFk....",
        "..kfrfffrk....",
        "...kffFFk.....",
        "...kkFFkk.....",
        "..knnbbnnk....",
        ".knnbBnnnlk...",
        ".knbBnnnlnk...",
        "knnbnyynlnnk..",
        "knbbnnnlnnnk..",
        "kfnbnnlnnnfk..",
        "kFknnlnnnnkFk.",
        ".kknlluuuulk..",
        "..knlluccullk.",
        "..knllucclllk.",
        "..knlllllllk..",
        "..kNklllllk...",
        "..kNNNkkkkk...",
        "..kPPpkPPk....",
        "..kPPpkPPk....",
    )
    private val POSTMAN_HAT = listOf(
        "...kkkkkkk....",
        "..kuuuUuuuk...",
        ".kuuuuuuuuUk..",
        ".kuUkyykkUuk..",
        ".kuUkkkkkkUk..",
    )
    private val PLEGS = listOf(
        listOf("..kPPk.kPk....", "..kPPk.kPk....", ".kSSSk.kSSk...", ".kkkkk.kkkk..."),
        listOf("...kPPkPk.....", "...kPPkPk.....", "..kSSSkSSk....", "..kkkkkkkk...."),
    )
    private fun postmanPal(winter: Boolean) = mapOf(
        'k' to rgb(0x140c08), 'N' to rgb(0x0e1426), 'n' to rgb(0x1e2a4a), 'b' to rgb(0x2c3c64), 'B' to rgb(0x405284),
        'V' to rgb(0x08080c), 'y' to rgb(0xe8b443), 'f' to rgb(0xf2c09a), 'F' to rgb(0xc4805e), 'r' to rgb(0xe48a7a),
        'h' to rgb(0x3a2216), 'L' to rgb(0x2a170e), 'l' to rgb(0x5c3820), 'u' to rgb(0x8a5a32), 'c' to rgb(0xf8eed4),
        'P' to rgb(0x2a2a34), 'p' to rgb(0x3c3c48), 'S' to rgb(if (winter) 0x6e6862 else 0x140c08), 'e' to rgb(0x2a1a10),
    )
    private val hatPal = mapOf('k' to rgb(0x140c08), 'u' to rgb(0x5a4030), 'U' to rgb(0x3a2a20), 'y' to rgb(0xe8b443))

    /** The postman, feet at (x+7, feetY). */
    fun postman(b: Buf, x: Int, feetY: Int, winter: Boolean, frame: Int = 0) {
        val top = feetY - POSTMAN.size - 4
        val pal = postmanPal(winter)
        b.spr(POSTMAN, x, top, pal)
        if (winter) b.spr(POSTMAN_HAT, x, top, hatPal)
        b.spr(PLEGS[frame % 2], x, top + POSTMAN.size, pal)
    }

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

    /** A dog lying asleep by the stove. */
    fun dogLying(b: Buf, x: Int, y: Int, br: Double) {
        b.vol(x, y, 26, 12, ell(13.0, 7.0 - br * .4, 12.0, 5.0 + br * .4), sph(10.0, 4.0, 12.0, 6.0, .3), intArrayOf(rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52), rgb(0xd8b07a), rgb(0xecd2a2)), rgb(0x2a1608))
        b.vol(x - 4, y + 3, 11, 9, ell(5.5, 4.5, 5.0, 4.0), sph(4.0, 3.0, 5.0, 4.0, .3), intArrayOf(rgb(0x6e4a28), rgb(0x8e643a), rgb(0xb88a52), rgb(0xd8b07a), rgb(0xecd2a2)), rgb(0x2a1608))
        b.r(x - 3, y + 2, 3, 3, rgb(0x8e643a)); b.p(x - 4, y + 7, rgb(0x140c08)); b.p(x, y + 6, rgb(0x2a1608)); b.p(x + 1, y + 6, rgb(0x2a1608))
        for (i in 0..4) b.p(x + 24 + i / 2, y + 4 - i, rgb(0xc99a5e))
    }
}
