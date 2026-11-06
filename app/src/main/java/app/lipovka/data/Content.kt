package app.lipovka.data

import android.content.Context
import app.lipovka.domain.Cal
import java.time.LocalDate

/** A pair of texts, Russian and English. */
data class Tx(val ru: String, val en: String) {
    operator fun invoke(ru: Boolean) = if (ru) this.ru.ifBlank { en } else en.ifBlank { this.ru }

    companion object {
        val EMPTY = Tx("", "")
    }
}

enum class Kind { LETTER, POSTCARD, PARCEL, TELEGRAM, REGISTERED, NEWSPAPER, NOTICE;

    companion object {
        fun of(s: String) = entries.firstOrNull { it.name.equals(s, true) } ?: LETTER
    }
}

data class Resident(
    val id: String,
    val house: String,
    val district: Int,
    val sprite: String,
    val look: List<String>,
    /** "MM-DD" */
    val birthday: String,
    val name: Tx,
    val about: Tx,
) {
    val old get() = sprite.endsWith("_old")
    val child get() = sprite == "girl" || sprite == "boy" || sprite == "teen"
    val young get() = sprite.endsWith("_young") || sprite == "teen"
}

/** One piece of a story: a letter that comes after the one before it was delivered. */
data class Beat(
    val arc: String,
    val n: Int,
    val gap: Int,
    val months: Set<Int>,
    /** "MM-DD" or empty. */
    val on: String,
    val needs: List<String>,
    val kind: Kind,
    val to: String,
    val from: Tx,
    val brief: Tx,
    val news: Tx,
    val reply: String,
    val gift: String,
    val stamp: String,
    val sets: String,
) {
    val key get() = "$arc:$n"
}

data class Item(val key: String, val family: String, val variant: String, val name: Tx)

data class Stamp(val key: String, val family: String, val bg: String, val value: Int, val name: Tx, val series: String)

data class Template(
    val key: String,
    val every: String,
    val day: String,
    val months: Set<Int>,
    val to: List<String>,
    val kind: Kind,
    val from: Tx,
    val brief: Tx,
    val variants: List<Tx>,
    val stamp: String,
)

data class Filler(val index: Int, val tags: Set<String>, val from: Tx, val brief: Tx, val news: Tx)

data class Event(
    val key: String,
    val start: String,
    val end: String,
    val district: Int,
    val look: String,
    val name: Tx,
    val notice: Tx,
    val brief: Tx,
    val stamp: String,
)

/**
 * A line for the tear-off calendar. [kind] is "sign" (a folk saint's day and its weather sign, [on] = "MM-DD"),
 * "saying" (a month's saying, [on] = "MM"), "tip" (a hint or recipe for the back of a month's sheets, [on] = "MM")
 * or "name" (a name in [text], whose name days are the "MM-DD" dates in [on]).
 */
data class CalNote(val kind: String, val on: String, val title: Tx, val text: Tx)

/** What a calendar sheet prints for its day: the day's sign or the month's saying, the name days, and the back. */
data class Sheet(val sign: CalNote?, val names: List<String>, val tip: CalNote?)

/** Everything written for the game, read once from assets/content. */
class Content(
    val residents: List<Resident>,
    val beats: List<Beat>,
    val items: Map<String, Item>,
    val stamps: Map<String, Stamp>,
    val templates: List<Template>,
    val fillers: List<Filler>,
    val events: List<Event>,
    val calendar: List<CalNote> = emptyList(),
) {
    val byId = residents.associateBy { it.id }
    val arcs: Map<String, List<Beat>> = beats.groupBy { it.arc }.mapValues { (_, b) -> b.sortedBy { it.n } }
    private val beatByKey = beats.associateBy { it.key }
    fun beat(key: String) = beatByKey[key]
    fun beat(arc: String, n: Int) = arcs[arc]?.getOrNull(n - 1)
    fun resident(id: String) = byId[id]
    val templateByKey = templates.associateBy { it.key }
    val eventByKey = events.associateBy { it.key }

    /** The district of an arc: where its first letter goes (the postman's own letters count as the village). */
    fun arcDistrict(arc: String): Int = arcs[arc]?.firstOrNull()?.to?.let { byId[it]?.district } ?: 0

    /** The tear-off calendar's sheet for [date]: the same day always prints the same things. */
    fun sheet(date: LocalDate): Sheet {
        val day = Cal.mmdd(date)
        val month = "%02d".format(date.monthValue)
        fun pick(kind: String) = calendar.filter { it.kind == kind && it.on == month }.let { it.getOrNull(date.dayOfMonth % it.size.coerceAtLeast(1)) }
        val sign = calendar.firstOrNull { it.kind == "sign" && it.on == day } ?: pick("saying")
        val names = calendar.filter { it.kind == "name" && day in it.on.split(',') }.flatMap { it.text.ru.split(", ") }
        return Sheet(sign, names, pick("tip"))
    }

    /** Residents who live in a house. */
    fun household(house: String) = residents.filter { it.house == house }

    companion object {
        fun load(context: Context): Content {
            val a = context.assets
            fun read(path: String): String = a.open("content/$path").bufferedReader().use { it.readText() }
            fun list(dir: String) = a.list("content/$dir").orEmpty().filter { it.endsWith(".tsv") }.sorted().map { read("$dir/$it") }
            fun opt(path: String) = runCatching { read(path) }.getOrDefault("")
            return parse(
                residents = read("residents.tsv"),
                arcs = list("arcs"),
                items = list("items"),
                stamps = list("stamps"),
                templates = opt("templates.tsv"),
                fillers = opt("fillers.tsv"),
                events = opt("events.tsv"),
                calendar = opt("calendar.tsv"),
            )
        }

        private fun rows(tsv: String): List<List<String>> =
            tsv.lineSequence().drop(1).filter { it.isNotBlank() }.map { it.split('\t') }.toList()

        private fun months(s: String) = s.split(',').mapNotNull { it.trim().toIntOrNull() }.toSet()

        fun parse(
            residents: String,
            arcs: List<String>,
            items: List<String>,
            stamps: List<String>,
            templates: String,
            fillers: String,
            events: String,
            calendar: String = "",
        ): Content = Content(
            residents = rows(residents).map { f ->
                Resident(f[0], f[1], f[2].toInt(), f[3], f[4].split(','), f[5], Tx(f[6], f[7]), Tx(f[8], f[9]))
            },
            beats = arcs.flatMap { rows(it) }.filter { it.size >= 18 }.map { f ->
                Beat(
                    arc = f[0], n = f[1].toInt(), gap = f[2].toIntOrNull() ?: 0, months = months(f[3]), on = f[4],
                    needs = f[5].split(',').map { it.trim() }.filter { it.isNotEmpty() }, kind = Kind.of(f[6]), to = f[7],
                    from = Tx(f[8], f[9]), brief = Tx(f[10], f[11]), news = Tx(f[12], f[13]),
                    reply = f[14], gift = f[15], stamp = f[16], sets = f[17],
                )
            },
            items = items.flatMap { rows(it) }.filter { it.size >= 5 }.map { f -> Item(f[0], f[1], f[2], Tx(f[3], f[4])) }.associateBy { it.key },
            stamps = stamps.flatMap { rows(it) }.filter { it.size >= 7 }.map { f ->
                Stamp(f[0], f[1], f[2], f[3].toIntOrNull() ?: 1, Tx(f[4], f[5]), f[6])
            }.associateBy { it.key },
            templates = rows(templates).filter { it.size >= 13 }.map { f ->
                val ru = f[10].split(" | ")
                val en = f[11].split(" | ")
                Template(
                    key = f[0], every = f[1], day = f[2], months = months(f[3]), to = f[4].split(',').map { it.trim() },
                    kind = Kind.of(f[5]), from = Tx(f[6], f[7]), brief = Tx(f[8], f[9]),
                    variants = ru.indices.map { Tx(ru[it], en.getOrElse(it) { en.first() }) }, stamp = f[12],
                )
            },
            fillers = rows(fillers).filter { it.size >= 7 }.mapIndexed { i, f ->
                Filler(i, f[0].split(',').map { it.trim() }.toSet(), Tx(f[1], f[2]), Tx(f[3], f[4]), Tx(f[5], f[6]))
            },
            events = rows(events).filter { it.size >= 12 }.map { f ->
                Event(f[0], f[1], f[2], f[3].toIntOrNull() ?: 0, f[4], Tx(f[5], f[6]), Tx(f[7], f[8]), Tx(f[9], f[10]), f[11])
            },
            calendar = rows(calendar).filter { it.size >= 6 }.map { f -> CalNote(f[0], f[1], Tx(f[2], f[3]), Tx(f[4], f[5])) },
        )
    }
}
