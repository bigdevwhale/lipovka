package app.lipovka.domain

import java.time.LocalDate

enum class Season { WINTER, SPRING, SUMMER, AUTUMN }

/** What the trees are doing. */
enum class Leaves { BARE, BUDS, BLOSSOM, GREEN, GOLD, FALLING }

object Cal {
    /** Orthodox Easter (Julian computus, shifted to the Gregorian calendar). */
    fun easter(year: Int): LocalDate {
        val a = year % 4
        val b = year % 7
        val c = year % 19
        val d = (19 * c + 15) % 30
        val e = (2 * a + 4 * b - d + 34) % 7
        val month = (d + e + 114) / 31
        val day = (d + e + 114) % 31 + 1
        return LocalDate.of(year, month, day).plusDays(13)
    }

    /** "MM-DD" or "easter±N" in a given year. */
    fun resolve(spec: String, year: Int): LocalDate? {
        if (spec.startsWith("easter")) {
            val n = spec.removePrefix("easter").toIntOrNull() ?: 0
            return easter(year).plusDays(n.toLong())
        }
        val p = spec.split('-')
        if (p.size != 2) return null
        val m = p[0].toIntOrNull() ?: return null
        val d = p[1].toIntOrNull() ?: return null
        return runCatching { LocalDate.of(year, m, d.coerceAtMost(LocalDate.of(year, m, 1).lengthOfMonth())) }.getOrNull()
    }

    /** Is [date] within a start..end window that may wrap over New Year? */
    fun within(date: LocalDate, start: String, end: String): Boolean {
        for (y in listOf(date.year - 1, date.year)) {
            val s = resolve(start, y) ?: return false
            var e = resolve(end, y) ?: return false
            if (e.isBefore(s)) e = resolve(end, y + 1) ?: return false
            if (!date.isBefore(s) && !date.isAfter(e)) return true
        }
        return false
    }

    fun mmdd(date: LocalDate) = "%02d-%02d".format(date.monthValue, date.dayOfMonth)

    /** The month as the village feels it: south of the equator the seasons turn round. */
    fun villageMonth(date: LocalDate, south: Boolean): Int = if (south) (date.monthValue + 5) % 12 + 1 else date.monthValue

    fun season(month: Int): Season = when (month) {
        12, 1, 2 -> Season.WINTER
        3, 4, 5 -> Season.SPRING
        6, 7, 8 -> Season.SUMMER
        else -> Season.AUTUMN
    }

    fun leaves(month: Int, day: Int): Leaves = when (month) {
        11, 12, 1, 2, 3 -> Leaves.BARE
        4 -> if (day < 20) Leaves.BARE else Leaves.BUDS
        5 -> if (day < 20) Leaves.BLOSSOM else Leaves.GREEN
        6, 7, 8 -> Leaves.GREEN
        9 -> if (day < 15) Leaves.GREEN else Leaves.GOLD
        else -> if (day < 15) Leaves.GOLD else Leaves.FALLING
    }

    /** Snow on the ground, by the calendar; real cold or warmth nudges the edges. */
    fun snowGround(month: Int, day: Int, temp: Double?): Boolean {
        val core = month in listOf(12, 1, 2) || (month == 11 && day >= 18) || (month == 3 && day <= 22)
        if (temp == null) return core
        return when {
            core && temp > 8 -> false
            !core && month in listOf(10, 11, 3, 4) && temp < -3 -> true
            else -> core
        }
    }

    /** The river is frozen from deep winter until the ice breaks in April. */
    fun riverIce(month: Int, day: Int): Boolean = month in listOf(1, 2, 3) || (month == 12 && day >= 10) || (month == 4 && day < 8)
}
