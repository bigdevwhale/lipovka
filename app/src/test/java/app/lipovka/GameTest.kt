package app.lipovka

import app.lipovka.data.Content
import app.lipovka.data.Mail
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
    }

    @Test fun counterReadings() {
        val boot = 1_000_000_000L
        val t = boot + 3_600_000L * 24 * 5
        val min15 = 15 * 60_000L
        // An ordinary walk.
        assertEquals(1500L, Steps.delta(10_000, t, 11_500, t + min15, boot))
        // A stale reading a little behind the last one brings nothing.
        assertEquals(0L, Steps.delta(28_600, t, 28_590, t + 1_000, boot))
        // A real reboot: the counter started again from zero.
        assertEquals(300L, Steps.delta(28_600, t, 300, t + min15, t + 60_000))
        // The counter glitches to zero and back: the jump is held to what can be walked meanwhile.
        assertEquals(0L, Steps.delta(28_600, t, 0, t + 1_000, boot))
        assertEquals(Steps.LATE_STEPS + 2L * Steps.MAX_PER_SECOND, Steps.delta(0, t + 1_000, 28_600, t + 3_000, boot))
        // 28 000 steps in 15 minutes can't be walked (#8).
        assertEquals(Steps.LATE_STEPS + 900L * Steps.MAX_PER_SECOND, Steps.delta(400, t, 28_400, t + min15, boot))
        // After a long sleep a whole day's walk still arrives in one reading.
        assertEquals(12_000L, Steps.delta(10_000, t, 22_000, t + 3_600_000L * 10, boot))
    }

    /** Three years with an average walker, starting in each season: mail every day, stories for years. */
    @Test fun healthTotals() {
        val known = mapOf(10L to 5_000, 11L to 300)
        // Only what is new: today grew, yesterday's watch handed its steps over late, a lower total brings nothing.
        assertEquals(mapOf(11L to 1_700, 9L to 4_000), Steps.catchUp(known, mapOf(9L to 4_000L, 10L to 4_800L, 11L to 2_000L)))
        assertEquals(emptyMap<Long, Int>(), Steps.catchUp(known, mapOf(10L to 5_000L)))
        // A glitched total is held to a day's most.
        assertEquals(mapOf(12L to Steps.MAX_PER_DAY), Steps.catchUp(known, mapOf(12L to 1_000_000L)))
    }

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

    /**
     * "Take more" on the way: a letter for a house behind (or just nearer) must not be delivered at once with
     * the steps already walked towards the next house, and that house must stay next.
     */
    @Test fun takeMoreKeepsTheLegBegun() {
        val game = Game(content)
        val date = LocalDate.of(2026, 11, 5)
        val day = date.toEpochDay()
        val s = GameState(start = day - 30, at = "lebedev")
        s.mail += Mail(id = 1, src = "fill:0", kind = "LETTER", to = "fedor", day = day, state = St.BAG)
        s.mail += Mail(id = 2, src = "fill:1", kind = "LETTER", to = "dima", day = day, state = St.SHELF, priority = 2)
        val toMill = game.plan(s).first().leg
        game.walk(s, toMill - 20, day, 0)
        assertEquals("mill", s.heading)

        game.takeMore(s, date)
        assertEquals("the mill stays next", "mill", game.plan(s).first().house.id)
        assertEquals(20, game.toNext(s))
        assertTrue("nothing delivered by one more step", game.walk(s, 1, day, 0).isEmpty())
        assertEquals(listOf("fedor"), game.walk(s, 19, day, 0).map { it.to })
        assertEquals("mill", s.at)
        assertTrue("Dima's letter still in the bag", s.bag.any { it.to == "dima" })
    }

    /** The same from a leg saved before the heading was remembered: no step yet since the update. */
    @Test fun takeMoreKeepsALegSavedWithoutHeading() {
        val game = Game(content)
        val date = LocalDate.of(2026, 11, 5)
        val day = date.toEpochDay()
        val s = GameState(start = day - 30, at = "lebedev")
        s.mail += Mail(id = 1, src = "fill:0", kind = "LETTER", to = "fedor", day = day, state = St.BAG)
        s.mail += Mail(id = 2, src = "fill:1", kind = "LETTER", to = "dima", day = day, state = St.SHELF, priority = 2)
        s.leg = game.plan(s).first().leg - 20
        game.takeMore(s, date)
        assertEquals("mill", game.plan(s).first().house.id)
        assertEquals(listOf("fedor"), game.walk(s, 20, day, 0).map { it.to })
    }

    /** The last letter given out, the postman walks back to the post office instead of staying at the gate. */
    @Test fun walksHomeAfterTheLastLetter() {
        val game = Game(content)
        val date = LocalDate.of(2026, 11, 5)
        val day = date.toEpochDay()
        val s = GameState(start = day - 30, at = "post")
        s.mail += Mail(id = 1, src = "fill:0", kind = "LETTER", to = "fedor", day = day, state = St.BAG)
        val toMill = game.plan(s).first().leg
        assertEquals(listOf("fedor"), game.walk(s, toMill + 10, day, 0).map { it.to })
        assertEquals("mill", s.at)
        assertTrue(game.homing(s))
        assertEquals("the steps past the gate are already on the way home", 10, s.leg)
        val home = game.homeLeg(s)
        game.walk(s, home - 11, day, 0)
        assertEquals("mill", s.at)
        game.walk(s, 1, day, 0)
        assertEquals("post", s.at)
        assertEquals(0, s.leg)
        assertTrue(!game.homing(s))
    }

    /** #49: yesterday's steps handed over by a watch after the morning post count for yesterday, not today's round. */
    @Test fun lateStepsDontCarryTodaysBag() {
        val game = Game(content)
        val date = LocalDate.of(2026, 11, 5)
        val day = date.toEpochDay()
        val s = GameState(start = day - 30, at = "post", morning = day)
        s.mail += Mail(id = 1, src = "fill:0", kind = "LETTER", to = "fedor", day = day, state = St.BAG)
        val leg = game.plan(s).first().leg
        assertTrue("nothing delivered with last night's steps", game.walk(s, leg + 500, day - 1, 0).isEmpty())
        assertEquals(0, s.leg)
        assertEquals(leg + 500, s.days[day - 1])
        assertEquals((leg + 500).toLong(), s.total)
        assertEquals(listOf("fedor"), game.walk(s, leg, day, 0).map { it.to })
    }

    /** On the way home, taking more letters turns the postman round where he stands. */
    @Test fun takeMoreOnTheWayHome() {
        val game = Game(content)
        val date = LocalDate.of(2026, 11, 5)
        val day = date.toEpochDay()
        val s = GameState(start = day - 30, at = "mill", leg = 50, heading = Game.HOME)
        s.mail += Mail(id = 2, src = "fill:1", kind = "LETTER", to = "dima", day = day, state = St.SHELF, priority = 2)
        game.takeMore(s, date)
        assertTrue(s.bag.isNotEmpty())
        assertEquals(0, s.leg)
        assertEquals("", s.heading)
        assertEquals("mill", s.at)
    }

    /** A long walker who empties the bag keeps getting letters: each "take more" adds one, up to a full bag. */
    @Test fun takeMoreAgainAndAgain() {
        val start = LocalDate.of(2026, 3, 2)
        val run = play(start, 20) { 6000 }
        val game = Game(content)
        val s = run.s
        val date = start.plusDays(19)
        val day = date.toEpochDay()
        val got = mutableListOf<Int>()
        for (k in 0 until 6) {
            game.walk(s, 500_000, day, 0)
            repeat(Game.BAG_MAX + 2) { game.takeMore(s, date) }
            got += s.bag.size
        }
        assertTrue("take more gave $got", got.all { it == Game.BAG_MAX })
        game.walk(s, 500_000, day, 0)
        assertTrue(s.bag.isEmpty())
        game.takeMore(s, date)
        assertEquals("one letter per press", 1, s.bag.size)
        // Each press makes the round longer, by a growing share of a usual day (10%, 15%, 20%...), 1 500 steps at least.
        val day2 = day + 1
        val date2 = date.plusDays(1)
        fun presses(open: Boolean): Pair<List<Int>, List<Int>> {
            val s2 = GameState(start = s.start, days = s.days.toMutableMap())
            if (open) for (d in 1..5) s2.flag("d$d", s.start)
            val rounds = mutableListOf(0)
            val mins = mutableListOf<Int>()
            repeat(4) {
                mins += game.moreSteps(s2, day2)
                game.takeMore(s2, date2); rounds += game.plan(s2).last().cum
            }
            return rounds.zipWithNext { a, b -> b - a } to mins
        }
        val (wide, mins) = presses(open = true)
        assertEquals(listOf(1500, 2250, 3000, 3750), mins)
        assertTrue("added $wide, at least $mins", wide.zip(mins).all { (a, m) -> a >= m })
        // Lipovka alone has no house that far: the rest is a roundabout road, and the share holds just the same.
        val (small, _) = presses(open = false)
        assertTrue("added $small, at least $mins", small.zip(mins).all { (a, m) -> a >= m })
        println("presses: wide $wide, small $small, at least $mins")
    }
}

class WeatherTest {
    @Test fun metSymbols() {
        assertEquals(app.lipovka.domain.Sky.DRIZZLE, app.lipovka.domain.Weather.symbol("lightrainshowers_day"))
        assertEquals(app.lipovka.domain.Sky.STORM, app.lipovka.domain.Weather.symbol("heavyrainandthunder"))
        assertEquals(app.lipovka.domain.Sky.OVERCAST, app.lipovka.domain.Weather.symbol("cloudy"))
        assertEquals(app.lipovka.domain.Sky.CLOUDY, app.lipovka.domain.Weather.symbol("partlycloudy_night"))
        assertEquals(app.lipovka.domain.Sky.SNOW, app.lipovka.domain.Weather.symbol("lightsnow"))
        assertEquals(app.lipovka.domain.Sky.CLEAR, app.lipovka.domain.Weather.symbol("clearsky_day"))
    }
}
