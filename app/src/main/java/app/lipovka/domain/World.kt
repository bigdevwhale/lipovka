package app.lipovka.domain

import kotlin.math.hypot
import kotlin.math.roundToInt

/** A point on the village map (map pixels; the map is [World.W] × [World.H]). */
data class Pt(val x: Double, val y: Double) {
    fun to(o: Pt) = hypot(o.x - x, o.y - y)
}

/** A place on the map where letters can be carried. */
data class House(
    val id: String,
    val district: Int,
    val at: Pt,
    /** Roof colour: R red, B blue, G green, W brown, T thatch, S slate. */
    val roof: Char,
    /** Window frame colour (наличники): W white, B blue, G green, Y yellow. */
    val frame: Char,
    /** What stands around the house in its gate scene. */
    val props: Set<String> = emptySet(),
)

/** The geography: where every house stands, the districts and the roads between them. */
object World {
    const val W = 170
    const val H = 620

    /** Steps for one map pixel along the road. */
    const val STEPS_PER_PX = 16.0

    /** Kilometres walked in total that open each district. */
    val OPENS_AT_KM = intArrayOf(0, 50, 150, 350, 700, 1200)

    val POST = Pt(98.0, 586.0)

    val houses: List<House> = listOf(
        House("shop", 0, Pt(60.0, 560.0), 'G', 'W', setOf("shop")),
        House("club", 0, Pt(140.0, 556.0), 'R', 'Y', setOf("club")),
        House("kuznetsovy", 0, Pt(38.0, 518.0), 'B', 'W', setOf("swing", "tractor")),
        House("vetrovy", 0, Pt(140.0, 508.0), 'R', 'W', setOf("rowan")),
        House("sorokina", 0, Pt(76.0, 500.0), 'W', 'B', setOf("well", "cat")),
        House("ryabininy", 0, Pt(22.0, 466.0), 'S', 'G', setOf("antenna")),
        House("lebedev", 0, Pt(112.0, 466.0), 'G', 'W', setOf("telescope", "books")),
        House("sokolovy", 0, Pt(150.0, 448.0), 'B', 'Y', setOf("goat", "garden")),
        House("apiary", 0, Pt(40.0, 420.0), 'T', 'W', setOf("hives")),
        House("mill", 0, Pt(84.0, 396.0), 'T', 'W', setOf("mill")),
        House("farmstead", 1, Pt(30.0, 262.0), 'T', 'W', setOf("goat", "woodpile")),
        House("forester", 1, Pt(140.0, 270.0), 'G', 'G', setOf("owl", "woodpile")),
        House("workshop", 1, Pt(96.0, 300.0), 'W', 'Y', setOf("carvings")),
        House("lastochkiny", 1, Pt(46.0, 318.0), 'R', 'B', setOf("goat", "cheese")),
        House("halt", 2, Pt(112.0, 198.0), 'S', 'Y', setOf("station", "telegraph")),
        House("stationhouse", 2, Pt(150.0, 194.0), 'W', 'W', setOf("lantern")),
        House("boatshed", 3, Pt(86.0, 150.0), 'W', 'B', setOf("boat", "nets")),
        House("painter", 3, Pt(78.0, 110.0), 'B', 'W', setOf("easel")),
        House("meteo", 4, Pt(150.0, 100.0), 'S', 'W', setOf("meteo")),
        House("belkiny", 4, Pt(124.0, 136.0), 'G', 'Y', setOf("swing", "woodpile")),
        House("newspaper", 5, Pt(70.0, 36.0), 'S', 'W', setOf("town")),
        House("museum", 5, Pt(122.0, 30.0), 'G', 'W', setOf("town", "columns")),
    )
    private val byId = houses.associateBy { it.id }
    fun house(id: String) = byId[id]

    /** Where the road from a district leaves for its parent district, and which one that is. */
    private val gate = mapOf(
        1 to (Pt(104.0, 360.0) to 0),
        2 to (Pt(118.0, 220.0) to 1),
        3 to (Pt(90.0, 188.0) to 2),
        4 to (Pt(134.0, 178.0) to 2),
        5 to (Pt(100.0, 78.0) to 2),
    )

    /** The bridge over the Lipka, between the village and Zarechye. */
    val BRIDGE get() = gate.getValue(1).first

    private fun chain(d: Int): List<Int> {
        val out = mutableListOf(d)
        var c = d
        while (c != 0) { c = gate.getValue(c).second; out += c }
        return out
    }

    /** The map path between two points in two districts: through the gates of the districts in between. */
    fun path(a: Pt, da: Int, b: Pt, db: Int): List<Pt> {
        val ca = chain(da)
        val cb = chain(db)
        val common = ca.first { it in cb }
        val up = ca.takeWhile { it != common }.map { gate.getValue(it).first }
        val down = cb.takeWhile { it != common }.map { gate.getValue(it).first }.reversed()
        return listOf(a) + up + down + listOf(b)
    }

    /** Between districts the Cuckoo train or a passing cart helps: those stretches count for less. */
    const val RIDE = .55

    fun distancePx(a: Pt, da: Int, b: Pt, db: Int): Double {
        val pts = path(a, da, b, db)
        val legs = pts.zipWithNext { p, q -> p.to(q) }
        if (legs.size <= 1) return legs.sum()
        // the first and last stretches are on foot; the ones between gates are ridden part of the way
        return legs.first() + legs.last() + legs.drop(1).dropLast(1).sum() * RIDE
    }

    /** Steps between two places, at least a short walk. */
    fun steps(a: Pt, da: Int, b: Pt, db: Int): Int = (distancePx(a, da, b, db) * STEPS_PER_PX).roundToInt().coerceAtLeast(150)

    /** A spot [t] (0..1) of the way along a path. */
    fun along(path: List<Pt>, t: Double): Pt {
        val legs = path.zipWithNext()
        val total = legs.sumOf { (p, q) -> p.to(q) }
        if (total <= 0) return path.first()
        var left = t.coerceIn(0.0, 1.0) * total
        for ((p, q) in legs) {
            val l = p.to(q)
            if (left <= l) return Pt(p.x + (q.x - p.x) * left / l, p.y + (q.y - p.y) * left / l)
            left -= l
        }
        return path.last()
    }

    fun districtOpen(km: Double, d: Int) = km >= OPENS_AT_KM[d]
}
