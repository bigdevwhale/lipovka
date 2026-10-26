package app.lipovka.ui.art

/**
 * How each house looks from its gate. Every family built, painted and patched its own: log or planks,
 * gable to the street or eaves, a lookout in the attic, a glazed veranda, a porch, a shed, carvings.
 */
data class Facade(
    /** Left wall and width of the main walls; they run from [top] down to the ground behind the fence. */
    val x: Int = 66,
    val w: Int = 94,
    val top: Int = 78,
    val wall: Wall = Wall.LOGS,
    /** Board colour for [Wall.PLANKS]; [paint2] paints the right half another colour. */
    val paint: Int = 0,
    val paint2: Int? = null,
    /** True: the long side and the whole roof face the street; false: the gable does. */
    val side: Boolean = false,
    /** How flat the gable is: its edge runs this many pixels out per row down (the side roof's height grows with it). */
    val pitch: Double = 1.05,
    /** A hipped end clipping the top of the gable. */
    val hip: Boolean = false,
    val gable: Gable = Gable.ROUND,
    val windows: Int = 2,
    val narrow: Boolean = false,
    val trim: Trim = Trim.CARVED,
    val shutters: Int? = null,
    /** 0: plain eaves; 1: a carved valance; 2: that and carved boards hanging from the gable. */
    val carving: Int = 1,
    val left: Annex? = null,
    val right: Annex? = null,
    val plinth: Boolean = false,
    val chimney: Boolean = true,
    val flag: Boolean = false,
)

enum class Wall { LOGS, NEW, OLD, DARK, PLANKS }
enum class Gable { ROUND, LOOKOUT, STUDIO, ANTLERS, LOFT, VENT, NONE }
enum class Trim { PLAIN, CARVED, ARCHED, TALL }
enum class Annex { VERANDA, PORCH, SHED, WHEEL, COLUMNS, SHOPFRONT }

object Facades {
    private val BLUE = rgb(0x5a7cae)
    private val GREEN = rgb(0x3e7050)

    private val all = mapOf(
        "vetrovy" to Facade(shutters = GREEN),
        "sorokina" to Facade(x = 74, w = 78, top = 86, wall = Wall.OLD, pitch = 1.2, narrow = true, trim = Trim.PLAIN, shutters = BLUE, carving = 0, right = Annex.SHED),
        "kuznetsovy" to Facade(x = 70, w = 92, wall = Wall.NEW, side = true, gable = Gable.LOOKOUT, windows = 3, narrow = true, left = Annex.VERANDA),
        "ryabininy" to Facade(x = 70, w = 88, top = 82, gable = Gable.LOOKOUT, pitch = .9, trim = Trim.ARCHED, carving = 0),
        "lebedev" to Facade(x = 74, w = 86, wall = Wall.PLANKS, paint = rgb(0xd0a850), hip = true, trim = Trim.ARCHED, left = Annex.VERANDA, plinth = true),
        "sokolovy" to Facade(x = 66, w = 88, wall = Wall.PLANKS, paint = rgb(0x9ab8c8), side = true, gable = Gable.NONE, trim = Trim.TALL, carving = 0, right = Annex.PORCH),
        "apiary" to Facade(x = 76, w = 70, top = 90, wall = Wall.OLD, pitch = 1.3, narrow = true, trim = Trim.PLAIN, carving = 0, gable = Gable.VENT, chimney = false),
        "mill" to Facade(x = 60, w = 72, top = 70, wall = Wall.DARK, pitch = .9, windows = 1, trim = Trim.PLAIN, carving = 0, gable = Gable.LOFT, right = Annex.WHEEL, chimney = false),
        "farmstead" to Facade(x = 62, w = 82, top = 88, side = true, gable = Gable.NONE, trim = Trim.PLAIN, carving = 0, right = Annex.SHED),
        "forester" to Facade(x = 66, w = 84, wall = Wall.DARK, gable = Gable.ANTLERS, shutters = rgb(0x2c5a3a), trim = Trim.PLAIN, right = Annex.PORCH),
        "workshop" to Facade(x = 68, w = 90, wall = Wall.NEW, pitch = .95, carving = 2, gable = Gable.LOOKOUT),
        "lastochkiny" to Facade(wall = Wall.PLANKS, paint = rgb(0x7a9ccc), paint2 = rgb(0xd89a9a), trim = Trim.CARVED, carving = 1, shutters = rgb(0xf2ece0)),
        "halt" to Facade(x = 60, w = 104, top = 84, wall = Wall.PLANKS, paint = rgb(0xc8b070), side = true, hip = true, gable = Gable.NONE, windows = 3, trim = Trim.TALL, carving = 1),
        "stationhouse" to Facade(x = 70, w = 84, wall = Wall.PLANKS, paint = rgb(0x8aa0c0), hip = true, trim = Trim.PLAIN, plinth = true, right = Annex.PORCH, carving = 0),
        "boatshed" to Facade(x = 64, w = 92, top = 84, wall = Wall.OLD, pitch = 1.4, gable = Gable.LOFT, trim = Trim.PLAIN, carving = 0, shutters = BLUE),
        "painter" to Facade(x = 70, w = 86, wall = Wall.PLANKS, paint = rgb(0x6e8cb8), pitch = .85, gable = Gable.STUDIO, trim = Trim.PLAIN, carving = 0),
        "meteo" to Facade(x = 72, w = 84, top = 82, wall = Wall.PLANKS, paint = rgb(0xdcdcd0), side = true, hip = true, gable = Gable.NONE, trim = Trim.PLAIN, carving = 0, plinth = true, chimney = false),
        "belkiny" to Facade(x = 62, w = 104, top = 80, wall = Wall.LOGS, side = true, gable = Gable.LOOKOUT, windows = 3, shutters = rgb(0xc8a040), carving = 1),
        "shop" to Facade(x = 62, w = 100, top = 84, wall = Wall.PLANKS, paint = rgb(0x5a8a6a), side = true, gable = Gable.NONE, windows = 1, trim = Trim.PLAIN, carving = 0, right = Annex.SHOPFRONT, plinth = true),
        "club" to Facade(x = 60, w = 108, top = 80, wall = Wall.PLANKS, paint = rgb(0xe8d8b0), pitch = 1.7, gable = Gable.ROUND, windows = 2, trim = Trim.TALL, carving = 0, right = Annex.COLUMNS, flag = true, plinth = true),
    )

    fun of(id: String): Facade = all[id] ?: Facade()
}
