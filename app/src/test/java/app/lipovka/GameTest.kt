package app.lipovka

import app.lipovka.data.Content
import app.lipovka.data.St
import app.lipovka.domain.Cal
import app.lipovka.domain.Game
import app.lipovka.domain.GameState
import app.lipovka.domain.Steps
import app.lipovka.domain.World
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File
import java.time.LocalDate
import java.time.ZoneId

/** Plays the game for years with a typical walker and checks the post keeps coming and the stories keep going. */
class GameTest {
    private val content: Content by lazy {
        val dir = listOf(File("src/main/assets/content"), File("app/src/main/assets/content")).first { it.exists() }
        fun all(sub: String) = File(dir, sub).listFiles().orEmpty().filter { it.name.endsWith(".tsv") }.sortedBy { it.name }.map { it.readText() }
        fun opt(name: String) = File(dir, name).takeIf { it.exists() }?.readText().orEmpty()
        Content.parse(File(dir, "residents.tsv").readText(), all("arcs"), all("items"), all("stamps"), opt("templates.tsv"), opt("fillers.tsv"), opt("events.tsv"))
    }
    private val zone = ZoneId.of("Europe/Moscow")

    private class Run(val s: GameState, val emptyDays: Int, val arcEnds: Map<String, Long>, val delivered: Int, val perDay: List<Int>)

    private fun play(start: LocalDate, days: Int, steps: (Int) -> Int): Run {
        val game = Game(content)
        val s = GameState(start = start.toEpochDay())
        var empty = 0
        val ends = mutableMapOf<String, Long>()
        val perDay = mutableListOf<Int>()
        for (i in 0 until days) {
            val date = start.plusDays(i.toLong())
            val day = date.toEpochDay()
            game.morning(s, date, date.atTime(7, 0).atZone(zone).toInstant().toEpochMilli())
            val before = s.mail.count { it.state == St.DELIVERED || it.state == St.SEEN }
            val n = steps(i)
            for (k in 0 until 4) game.walk(s, n / 4, day, date.atTime(9 + k * 3, 0).atZone(zone).toInstant().toEpochMilli())
            for (m in s.mail.filter { it.state == St.DELIVERED || it.state == St.DESK }) game.open(s, m.id, day)
            val got = s.mail.count { it.state == St.DELIVERED || it.state == St.SEEN } - before
            perDay += got
            if (got == 0 && s.bag.isEmpty()) empty++
            for ((arc, beats) in content.arcs) if (arc !in ends && (s.arcs[arc]?.n ?: 0) >= beats.size) ends[arc] = day - start.toEpochDay()
        }
        return Run(s, empty, ends, s.mail.count { it.state == St.SEEN }, perDay)
    }

    @Test fun contentLoads() {
        assertTrue("arcs", content.arcs.size > 40)
        assertTrue("beats", content.beats.size > 500)
        for (b in content.beats) if (b.to != "me") assertTrue("${b.key} to ${b.to}", content.resident(b.to) != null)
        for (r in content.residents) assertTrue("house of ${r.id}", World.house(r.house) != null)
    }

    @Test fun easter() {
        assertEquals(LocalDate.of(2025, 4, 20), Cal.easter(2025))
        assertEquals(LocalDate.of(2026, 4, 12), Cal.easter(2026))
        assertEquals(LocalDate.of(2027, 5, 2), Cal.easter(2027))
    }

    @Test fun stepsSpreadOverDays() {
        val from = LocalDate.of(2026, 3, 1).atTime(20, 0).atZone(zone).toInstant().toEpochMilli()
        val to = LocalDate.of(2026, 3, 2).atTime(8, 0).atZone(zone).toInstant().toEpochMilli()
        val m = Steps.spread(1200, from, to, zone)
        assertEquals(1200, m.values.sum())
        assertEquals(2, m.size)
        assertEquals(500L, Steps.delta(1000, 500))
    }

    /** Three years with an average walker, starting in each season: mail every day, stories for years. */
    @Test fun yearsOfPost() {
        for (month in listOf(1, 4, 7, 10)) {
            val start = LocalDate.of(2026, month, 3)
            val r = play(start, 3 * 365) { i -> 5200 + ((i * 7919) % 3000) }
            val s = r.s
            println("start month $month: km=${"%.0f".format(s.km)}, delivered=${r.delivered}, empty days=${r.emptyDays}, " +
                "arcs finished=${r.arcEnds.size}/${content.arcs.size}, items=${s.items.size}/${content.items.size}, stamps=${s.stamps.size}/${content.stamps.size}")
            val early = content.arcs.keys.filter { r.arcEnds[it] != null && r.arcEnds.getValue(it) < 365 }
            println("  arcs finished in the first year: $early")
            val unfinished = content.arcs.keys - r.arcEnds.keys
            println("  unfinished after 3 years: ${unfinished.map { "$it:${s.arcs[it]?.n ?: 0}/${content.arcs.getValue(it).size}" }}")
            assertTrue("too many days without post: ${r.emptyDays}", r.emptyDays < 30)
            assertTrue("all districts open", (1..5).all { s.has("d$it") })
            assertTrue("most stories reach their end", r.arcEnds.size >= content.arcs.size * 0.7)
            assertTrue("stories don't burn out in the first year", early.size <= content.arcs.size / 6)
            // after the stories, the post keeps coming
            val perYear = r.perDay.chunked(365).map { "%.1f".format(it.average()) }
            println("  letters a day by year: $perYear")
            val lastMonth = r.perDay.takeLast(30).sum()
            assertTrue("the post keeps coming in year 3: $lastMonth", lastMonth > 45)
        }
    }

    /** A light walker still gets a full bag sized to their days, and the stories still move. */
    @Test fun lightWalker() {
        val r = play(LocalDate.of(2026, 9, 1), 365) { 2600 }
        println("light walker: km=${"%.0f".format(r.s.km)}, delivered=${r.delivered}, empty=${r.emptyDays}")
        assertTrue(r.delivered > 365)
        assertTrue(r.emptyDays < 40)
    }
}
