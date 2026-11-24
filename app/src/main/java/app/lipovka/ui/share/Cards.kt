package app.lipovka.ui.share

import android.content.Context
import app.lipovka.R
import app.lipovka.data.Mail
import app.lipovka.data.St
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.GateScene
import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId

/** What a card can tell. */
enum class Period { DAY, WEEK, MONTH, ALL }

/** Builds the share cards from the game: a stretch of days in numbers, or one letter. */
object Cards {
    /** The band of the gate scene a card shows: the house, the gate and who stands at it. */
    private val GATE_ROWS = 44..189

    /** The mail day a letter was handed over on (the day turns over at five in the morning, as everywhere in the game). */
    private fun dayOf(m: Mail): Long =
        Instant.ofEpochMilli(m.deliveredAt).atZone(ZoneId.systemDefault()).toLocalDateTime().minusHours(5).toLocalDate().toEpochDay()

    private fun handed(home: Home): List<Mail> =
        home.s.mail.filter { (it.state == St.DELIVERED || it.state == St.SEEN) && it.deliveredAt > 0 && it.to != "me" }

    fun stats(ctx: Context, home: Home, p: Period): Card {
        val res = ctx.resources
        val today = home.today
        val days: LongRange = when (p) {
            Period.DAY -> today..today
            Period.WEEK -> today - 6..today
            Period.MONTH -> LocalDate.ofEpochDay(today).withDayOfMonth(1).toEpochDay()..today
            Period.ALL -> minOf(home.s.start, home.s.days.keys.minOrNull() ?: home.s.start)..today
        }
        val steps = if (p == Period.ALL) home.s.total else days.sumOf { (home.s.days[it] ?: 0).toLong() }
        val letters = handed(home).count { dayOf(it) in days }
        val walked = days.count { (home.s.days[it] ?: 0) > 0 }
        val title = ctx.getString(when (p) {
            Period.DAY -> R.string.share_day_title
            Period.WEEK -> R.string.share_week_title
            Period.MONTH -> R.string.share_month_title
            Period.ALL -> R.string.share_all_title
        })
        val first = Words.date(ctx, days.first)
        val sub = when (p) {
            Period.DAY -> Words.date(ctx, today)
            Period.ALL -> ctx.getString(R.string.served, home.year)
            else -> "$first — ${Words.date(ctx, today)}"
        }
        val stats = buildList {
            add(Words.num(steps) to res.getQuantityString(R.plurals.s_steps, Words.q(steps)))
            add(Words.km(steps) to ctx.getString(R.string.s_km))
            add(letters.toString() to res.getQuantityString(R.plurals.s_letters, letters))
            if (p == Period.ALL) add(home.s.stamps.size.toString() to ctx.getString(R.string.share_stamps))
            else if (p != Period.DAY) add(walked.toString() to res.getQuantityString(R.plurals.s_days, walked))
        }
        return Card(title, sub, stats, art = p.name.lowercase())
    }

    /** A stamp from the album, held up large, with the letter it came on. */
    fun stamp(ctx: Context, home: Home, st: app.lipovka.data.Stamp): Card {
        val got = home.s.stamps[st.key]
        val story = app.lipovka.ui.album.story(ctx, home, st)
        val sub = listOfNotNull(story?.second?.takeIf { it.isNotEmpty() }, got?.let { ctx.getString(R.string.stamp_got, Words.date(ctx, it.day)) }).joinToString(" · ")
            .ifEmpty { ctx.getString(R.string.share_stamp_sub) }
        return Card(st.name(home.ru), sub, quote = story?.first, picture = app.lipovka.ui.art.StampArt.draw(st.family, st.bg, st.value))
    }

    /** A gift from a neighbour, held up large, with who gave it and when. */
    fun gift(ctx: Context, home: Home, o: app.lipovka.data.Owned): Card? {
        val item = home.content.items[o.key] ?: return null
        val from = home.resident(o.from)?.name?.invoke(home.ru) ?: home.content.beat(o.from.removePrefix("arc:"))?.from?.invoke(home.ru) ?: ""
        return Card(item.name(home.ru), ctx.getString(R.string.from_whom, from, Words.date(ctx, o.day)),
            quote = ctx.getString(R.string.share_gift_line, from), picture = app.lipovka.ui.art.ItemArt.single(item.family, item.variant))
    }

    /** One letter: who it is from and to, its lines, and the gate where it was read. */
    fun letter(ctx: Context, home: Home, m: Mail): Card {
        val t = Words.mail(ctx, home.content, m, home.ru, home.year)
        // at the gate stands whoever the letter is for; a letter for the postman shows the neighbour who wrote it
        val to = home.resident(m.to)?.name?.invoke(home.ru)
        val who = home.resident(m.to) ?: home.resident(m.from)
        val house = World.house(who?.house ?: "") ?: World.house("vetrovy")!!
        val sub = if (to != null) "${t.from} → $to" else t.from
        val quote = if (home.ru) "«${t.news}»" else "“${t.news}”"
        // a letter from outside the village (the district office, a stranger) has no gate to show: the desk it was read at
        if (who == null) return Card(ctx.getString(R.string.share_letter_title), sub, quote = quote, art = "letter")
        return Card(ctx.getString(R.string.share_letter_title), sub, quote = quote, scene = GateScene(home.env, house, who, home.dog), rows = GATE_ROWS)
    }
}
