package app.lipovka.ui.art

/**
 * Who carries the post: one of the drawn postmen and postwomen, picked when the game starts and changeable in
 * the settings. The same figure stands at the gates and walks the round on the map.
 */
object Postman {
    const val DEFAULT = "postman"

    /** The men first, then the women; each is the name of their drawing. */
    val MEN = listOf("postman", "postman_m2", "postman_m3")
    val WOMEN = listOf("postman_f1", "postman_f2", "postman_f3")

    fun female(look: String) = look in WOMEN

    /** The figure for [look], in winter clothes when [winter], small for the map when [map]; any drawn postman will do if that one is missing. */
    fun sprite(look: String, winter: Boolean, map: Boolean = false): Sprite? {
        fun name(l: String) = "people/" + if (map) l.replaceFirst("postman", "postman_map") else l
        val ok = if (look in MEN || look in WOMEN) look else DEFAULT
        return (if (winter) Sprites.get(name(ok) + "_w") else null) ?: Sprites.get(name(ok))
            ?: (if (winter) Sprites.get(name(DEFAULT) + "_w") else null) ?: Sprites.get(name(DEFAULT))
    }

    /** A portrait of [look] for the picker: the summer figure on its own. */
    fun portrait(look: String): Buf? {
        val s = sprite(look, false) ?: return null
        return Buf(s.lw + 2, s.lh + 2, s.scale).also { it.blit(s, (s.lw + 2) / 2, s.lh + 1) }
    }
}
