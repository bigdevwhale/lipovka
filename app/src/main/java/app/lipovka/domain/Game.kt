package app.lipovka.domain

import app.lipovka.data.ArcState
import app.lipovka.data.Beat
import app.lipovka.data.Collected
import app.lipovka.data.Content
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.data.Owned
import app.lipovka.data.Resident
import app.lipovka.data.St
import java.time.DayOfWeek
import java.time.LocalDate
import kotlin.math.max

/**
 * Everything the game remembers, in memory. [Post] loads it from the database, lets [Game] change
 * it and writes back what changed ([dirtyMail] and the other dirty sets).
 */
class GameState(
    var start: Long,
    val mail: MutableList<Mail> = mutableListOf(),
    val days: MutableMap<Long, Int> = mutableMapOf(),
    val flags: MutableMap<String, Long> = mutableMapOf(),
    val arcs: MutableMap<String, ArcState> = mutableMapOf(),
    val items: MutableMap<String, Owned> = mutableMapOf(),
    val stamps: MutableMap<String, Collected> = mutableMapOf(),
    /** The house the postman last stopped at, or "post". */
    var at: String = "post",
    /** Steps walked since that stop. */
    var leg: Int = 0,
    /** The last mail day the morning post was sorted. */
    var morning: Long = -1,
    var total: Long = 0,
    /** The last reading of the phone's step counter, and when it was taken. */
    var lastValue: Long = -1,
    var lastAt: Long = 0,
) {
    val dirtyDays = mutableSetOf<Long>()
    val dirtyMail = mutableSetOf<Long>()
    val newMail = mutableListOf<Mail>()
    val dirtyFlags = mutableSetOf<String>()
    val dirtyArcs = mutableSetOf<String>()
    val dirtyItems = mutableSetOf<String>()
    val dirtyStamps = mutableSetOf<String>()
    var nextTempId = -1L

    fun mail(id: Long) = mail.firstOrNull { it.id == id }

    fun put(m: Mail) {
        val i = mail.indexOfFirst { it.id == m.id }
        if (i >= 0) mail[i] = m else mail += m
        if (m.id > 0) dirtyMail += m.id
    }

    fun add(m: Mail): Mail {
        val withId = m.copy(id = nextTempId--)
        mail += withId
        newMail += withId
        return withId
    }

    fun flag(k: String, day: Long) {
        if (k !in flags) { flags[k] = day; dirtyFlags += k }
    }

    fun has(k: String) = k in flags
    val km: Double get() = total * Game.STRIDE_M / 1000.0
    fun open(d: Int) = d == 0 || has("d$d")
    val bag get() = mail.filter { it.state == St.BAG }
    val shelf get() = mail.filter { it.state == St.SHELF }
}

/** One stop on the round: a house and the letters for it. */
data class Stop(val house: House, val mail: List<Mail>, val leg: Int, val cum: Int)

/** Where the postman is on the map now, and the path being walked. */
data class OnRoad(val at: Pt, val path: List<Pt>, val t: Double)

class Game(val content: Content) {
    companion object {
        const val STRIDE_M = 0.72
        val KM = intArrayOf(10, 25, 50, 100, 250, 500, 1000, 2000, 3000)
        const val DOG_DAYS = 7
        const val DOG_STEPS = 3000
        const val BAG_MAX = 9
        const val ARCS_PER_DAY = 3
        const val DEFAULT_TARGET = 5000
    }

    // ---------------------------------------------------------------- places

    fun houseOf(to: String): House? = content.resident(to)?.let { World.house(it.house) }

    fun point(at: String): Pt = World.house(at)?.at ?: World.POST
    fun districtOf(at: String): Int = World.house(at)?.district ?: 0

    private fun legSteps(from: String, to: House) = World.steps(point(from), districtOf(from), to.at, to.district)

    /** The round ahead: telegrams first, then always the nearest house next. */
    fun plan(s: GameState): List<Stop> {
        val byHouse = s.bag.groupBy { houseOf(it.to)?.id }.filterKeys { it != null }
        val left = byHouse.keys.filterNotNull().toMutableSet()
        val out = mutableListOf<Stop>()
        var from = s.at
        var cum = 0
        while (left.isNotEmpty()) {
            val urgent = left.filter { h -> byHouse[h]!!.any { it.kind == Kind.TELEGRAM.name } }
            val pool = urgent.ifEmpty { left.toList() }
            val next = pool.minBy { legSteps(from, World.house(it)!!) * 1000 + it.hashCode() % 997 }
            val h = World.house(next)!!
            val leg = legSteps(from, h)
            cum += leg
            out += Stop(h, byHouse[next]!!, leg, cum)
            left -= next
            from = next
        }
        return out
    }

    /** Steps left to the next stop (0 with an empty bag). */
    fun toNext(s: GameState): Int = plan(s).firstOrNull()?.let { max(0, it.leg - s.leg) } ?: 0

    fun onRoad(s: GameState): OnRoad {
        val next = plan(s).firstOrNull() ?: return OnRoad(point(s.at), listOf(point(s.at)), 0.0)
        val path = World.path(point(s.at), districtOf(s.at), next.house.at, next.house.district)
        val t = (s.leg.toDouble() / next.leg).coerceIn(0.0, 1.0)
        return OnRoad(World.along(path, t), path, t)
    }

    // ---------------------------------------------------------------- walking

    /** Real steps walked: the bag goes round, letters are delivered, milestones are reached. */
    fun walk(s: GameState, steps: Int, day: Long, now: Long): List<Mail> {
        if (steps <= 0) return emptyList()
        s.total += steps
        s.days[day] = (s.days[day] ?: 0) + steps
        s.dirtyDays += day
        val delivered = mutableListOf<Mail>()
        if (s.bag.isEmpty()) {
            s.leg = 0
        } else {
            s.leg += steps
            while (true) {
                val next = plan(s).firstOrNull() ?: break
                if (s.leg < next.leg) break
                s.leg -= next.leg
                s.at = next.house.id
                for (m in next.mail) delivered += deliver(s, m, day, now)
            }
            if (s.bag.isEmpty()) s.leg = 0
        }
        milestones(s, day)
        return delivered
    }

    private fun deliver(s: GameState, m: Mail, day: Long, now: Long): Mail {
        val d = m.copy(state = St.DELIVERED, deliveredAt = now)
        s.put(d)
        if (d.id < 0) s.newMail.replaceAll { if (it.id == d.id) d else it }
        advanceArc(s, d, day)
        return d
    }

    private fun advanceArc(s: GameState, m: Mail, day: Long) {
        if (!m.src.startsWith("arc:")) return
        val b = content.beat(m.src.removePrefix("arc:")) ?: return
        s.arcs[b.arc] = ArcState(b.arc, b.n, day)
        s.dirtyArcs += b.arc
        if (b.sets.isNotBlank()) s.flag(b.sets, day)
    }

    fun milestones(s: GameState, day: Long) {
        val km = s.km
        for (k in KM) if (km >= k) s.flag("km$k", day)
        for (d in 1..5) if (World.districtOpen(km, d)) s.flag("d$d", day)
        if (!s.has("dog") && s.days.count { it.value >= DOG_STEPS } >= DOG_DAYS) s.flag("dog", day)
    }

    // ---------------------------------------------------------------- the morning post

    /** How many steps a usual day holds for this postman: the median of recent walking days. */
    fun target(s: GameState, today: Long): Int {
        val recent = s.days.filter { it.key in (today - 14) until today && it.value >= 800 }.values.sorted()
        val med = if (recent.size >= 3) recent[recent.size / 2] else DEFAULT_TARGET
        return (med * 0.85).toInt().coerceIn(2000, 14000)
    }

    /** The cost in steps of walking round these houses from where the postman is. */
    fun cost(s: GameState, houses: Collection<String>): Int {
        var from = s.at
        var total = 0
        val left = houses.toMutableSet()
        while (left.isNotEmpty()) {
            val n = left.minBy { legSteps(from, World.house(it)!!) }
            total += legSteps(from, World.house(n)!!)
            from = n
            left -= n
        }
        return total
    }

    private fun yearServed(s: GameState, today: Long) = ((today - s.start) / 365 + 1).toInt()

    fun residentsOpen(s: GameState): List<Resident> = content.residents.filter { s.open(it.district) }

    private fun inFlight(s: GameState, arc: String) = s.mail.any {
        (it.state == St.SHELF || it.state == St.BAG) && it.src.startsWith("arc:$arc:")
    }

    /** The day an arc's clock starts: the game's start, or the day its district opened. */
    private fun arcStart(s: GameState, arc: String): Long {
        val d = content.arcDistrict(arc)
        return max(s.start, if (d == 0) s.start else s.flags["d$d"] ?: Long.MAX_VALUE / 2)
    }

    fun eligible(s: GameState, b: Beat, date: LocalDate, since: Long): Boolean {
        val today = date.toEpochDay()
        if (today - since < b.gap) return false
        if (b.months.isNotEmpty() && date.monthValue !in b.months) return false
        if (b.on.isNotBlank() && b.on != Cal.mmdd(date)) return false
        if (b.needs.any { !s.has(it) }) return false
        if (b.to != "me") {
            val r = content.resident(b.to) ?: return false
            if (!s.open(r.district)) return false
        }
        return true
    }

    /** The beats due today, the most overdue first. */
    fun dueBeats(s: GameState, date: LocalDate): List<Beat> {
        val today = date.toEpochDay()
        val due = mutableListOf<Pair<Beat, Long>>()
        for ((arc, beats) in content.arcs) {
            val st = s.arcs[arc]
            val n = (st?.n ?: 0) + 1
            val b = beats.getOrNull(n - 1) ?: continue
            if (b.n != n) continue
            if (inFlight(s, arc)) continue
            val since = if (st == null) arcStart(s, arc) else st.day
            if (since > today) continue
            if (eligible(s, b, date, since)) due += b to (today - since - b.gap)
        }
        val dated = due.filter { it.first.on.isNotBlank() }.map { it.first }
        val rest = due.filter { it.first.on.isBlank() }.sortedByDescending { it.second }.map { it.first }
        return dated + rest.take(ARCS_PER_DAY)
    }

    fun mailDay(now: java.time.LocalDateTime): LocalDate = now.minusHours(5).toLocalDate()

    /**
     * Sorts the morning post once per mail day: today's stories, newspapers, birthdays and notices
     * arrive; the bag is filled up to about a usual day's walk; the rest waits on the shelf.
     */
    fun morning(s: GameState, date: LocalDate, now: Long): Boolean {
        val today = date.toEpochDay()
        if (s.morning >= today) return false
        s.morning = today
        if (s.bag.isEmpty()) { s.at = "post"; s.leg = 0 }
        milestones(s, today)

        // Old everyday letters that never fitted into a day are quietly dropped.
        for (m in s.shelf) if (m.src.startsWith("fill:") && today - m.day > 5) s.put(m.copy(state = St.GONE))

        // Seasonal events: a poster to a few houses on the first day.
        for (e in content.events) {
            if (!s.open(e.district)) continue
            val first = Cal.resolve(e.start, date.year) ?: continue
            if (first != date) continue
            val homes = residentsOpen(s).filter { it.district == e.district }.distinctBy { it.house }
                .sortedBy { kotlin.math.abs((it.house + e.key + date.year).hashCode()) }.take(3)
            homes.forEachIndexed { i, r ->
                s.add(Mail(src = "evt:${e.key}", kind = Kind.NOTICE.name, to = r.id, day = today, state = St.SHELF, priority = 3,
                    stamp = if (i == 0) e.stamp else ""))
            }
        }

        // Recurring mail: newspapers, pensions, magazines, birthdays, holiday cards.
        val year = yearServed(s, today)
        for (t in content.templates) {
            if (t.months.isNotEmpty() && date.monthValue !in t.months) continue
            val due = when (t.every) {
                "weekly" -> date.dayOfWeek == DayOfWeek.of(t.day.toIntOrNull() ?: 4)
                "monthly" -> date.dayOfMonth == (t.day.toIntOrNull() ?: 1)
                "yearly" -> t.day == Cal.mmdd(date)
                else -> false
            }
            for (id in t.to) {
                val r = content.resident(id) ?: continue
                if (!s.open(r.district)) continue
                val birthday = t.every == "birthday" && r.birthday == Cal.mmdd(date)
                if (!due && !birthday) continue
                val v = Math.floorMod((id + t.key).hashCode() + year * 7 + date.dayOfYear * 13, t.variants.size)
                s.add(Mail(src = "tpl:${t.key}", kind = t.kind.name, to = id, day = today, state = St.SHELF, variant = v,
                    priority = if (birthday || t.every == "yearly") 3 else 1, stamp = t.stamp))
            }
        }

        // The stories.
        for (b in dueBeats(s, date)) {
            val m = Mail(src = "arc:${b.key}", kind = b.kind.name, to = b.to, day = today,
                state = if (b.to == "me") St.DESK else St.SHELF,
                priority = when {
                    b.kind == Kind.TELEGRAM -> 5
                    b.on.isNotBlank() -> 4
                    else -> 2
                },
                gift = b.gift, stamp = b.stamp, reply = b.reply)
            val added = s.add(m)
            if (b.to == "me") advanceArc(s, added, today)
        }

        fillBag(s, date)
        return true
    }

    /** Puts shelf mail into the bag by priority until the round is about a usual day's walk. */
    fun fillBag(s: GameState, date: LocalDate, extra: Int = 0) {
        val today = date.toEpochDay()
        val budget = target(s, today) + extra
        val houses = s.bag.mapNotNull { houseOf(it.to)?.id }.toMutableSet()
        var count = s.bag.size
        for (m in s.shelf.sortedWith(compareByDescending<Mail> { it.priority }.thenBy { it.day }.thenBy { it.id })) {
            val h = houseOf(m.to)?.id ?: continue
            if (count >= BAG_MAX && m.priority < 4) break
            val cost = cost(s, houses + h)
            if (m.priority < 3 && cost > budget && count > 0) continue
            houses += h
            count++
            take(s, m)
        }
        // Everyday letters fill a light day.
        var tries = 0
        while (count < 6 && cost(s, houses) < budget * 0.8 && tries++ < 12) {
            val m = filler(s, date, houses) ?: break
            val h = houseOf(m.to)!!.id
            if (cost(s, houses + h) > budget * 1.15 && count > 0) break
            houses += h
            count++
            s.add(m.copy(state = St.BAG))
        }
        if (s.bag.isEmpty() && s.leg == 0) s.at = "post"
    }

    private fun take(s: GameState, m: Mail) {
        val b = m.copy(state = St.BAG)
        s.put(b)
        if (b.id < 0) s.newMail.replaceAll { if (it.id == b.id) b else it }
    }

    /** An everyday letter for someone who hasn't had post for a couple of days, the nearer the likelier. */
    private fun filler(s: GameState, date: LocalDate, houses: Set<String>): Mail? {
        if (content.fillers.isEmpty()) return null
        val today = date.toEpochDay()
        val recent = s.mail.filter { today - it.day < 3 }.map { it.to }.toSet()
        val people = residentsOpen(s).filter { it.id !in recent && World.house(it.house)?.id !in houses }
        if (people.isEmpty()) return null
        val r = people.minBy { legSteps(s.at, World.house(it.house)!!) * (0.6 + rndOf(it.id, today)) }
        val tags = buildSet {
            add("any")
            if (r.old) add("old")
            if (r.young) add("young")
            if (r.child) add("child")
            if (!r.child && !r.old) add("family")
        }
        val used = s.mail.filter { it.to == r.id && it.src.startsWith("fill:") && today - it.day < 365 }.map { it.src }.toSet()
        val pool = content.fillers.filter { it.tags.any { t -> t in tags } && "fill:${it.index}" !in used }
        if (pool.isEmpty()) return null
        val f = pool[Math.floorMod((r.id + today).hashCode(), pool.size)]
        return Mail(src = "fill:${f.index}", kind = Kind.LETTER.name, to = r.id, day = today, state = St.SHELF, priority = 0)
    }

    private fun rndOf(id: String, day: Long) = app.lipovka.ui.art.hash(id.hashCode(), day.toInt())

    /** Takes more letters from the shelf on a day the postman wants a longer walk. */
    fun takeMore(s: GameState, date: LocalDate) = fillBag(s, date, extra = 4000)

    // ---------------------------------------------------------------- at the gate

    /** The visit is seen: the gift goes upstairs, the stamp into the album, a reply into tomorrow's bag. */
    fun open(s: GameState, id: Long, day: Long) {
        val m = s.mail(id) ?: return
        if (m.state != St.DELIVERED && m.state != St.DESK) return
        s.put(m.copy(state = St.SEEN))
        collect(s, m, day)
        if (m.reply.isNotBlank() && m.reply != "out" && content.resident(m.reply) != null) {
            s.add(Mail(src = "reply:${m.id}", kind = Kind.LETTER.name, to = m.reply, day = day, state = St.SHELF, priority = 2, from = m.to))
        }
    }

    private fun collect(s: GameState, m: Mail, day: Long) {
        if (m.gift.isNotBlank() && m.gift !in s.items && content.items.containsKey(m.gift)) {
            s.items[m.gift] = Owned(m.gift, m.to.takeIf { it != "me" } ?: m.src, day)
            s.dirtyItems += m.gift
        }
        if (m.stamp.isNotBlank() && content.stamps.containsKey(m.stamp)) {
            val c = s.stamps[m.stamp]
            s.stamps[m.stamp] = c?.copy(count = c.count + 1) ?: Collected(m.stamp, day)
            s.dirtyStamps += m.stamp
        }
    }
}
