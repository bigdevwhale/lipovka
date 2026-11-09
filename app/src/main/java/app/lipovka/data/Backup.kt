package app.lipovka.data

import app.lipovka.domain.Place
import org.json.JSONArray
import org.json.JSONObject

/** What a backup restores from the settings: the town for the weather and the notifications. The step source stays the phone's own. */
data class Carried(val place: Place?, val notify: Boolean)

/**
 * A backup file: the post office's books and a few settings as JSON, so progress moves to a new phone.
 * The format is versioned; a file from a newer app is refused rather than half read.
 */
object Backup {
    const val VERSION = 1
    private const val APP = "lipovka"

    fun mime() = "application/json"

    fun fileName(today: java.time.LocalDate) = "lipovka-$today.json"

    fun write(b: Books, c: Carried, at: Long = System.currentTimeMillis()): String = JSONObject().apply {
        put("app", APP)
        put("version", VERSION)
        put("at", at)
        put("mail", JSONArray(b.mail.map { m ->
            JSONObject().put("id", m.id).put("src", m.src).put("kind", m.kind).put("to", m.to).put("day", m.day)
                .put("state", m.state).put("variant", m.variant).put("priority", m.priority).put("deliveredAt", m.deliveredAt)
                .put("gift", m.gift).put("stamp", m.stamp).put("reply", m.reply).put("from", m.from).put("detour", m.detour)
        }))
        put("days", JSONArray(b.days.map { JSONObject().put("day", it.day).put("steps", it.steps) }))
        put("flags", JSONArray(b.flags.map { JSONObject().put("key", it.key).put("day", it.day) }))
        put("arcs", JSONArray(b.arcs.map { JSONObject().put("arc", it.arc).put("n", it.n).put("day", it.day) }))
        put("items", JSONArray(b.items.map { JSONObject().put("key", it.key).put("from", it.from).put("day", it.day) }))
        put("stamps", JSONArray(b.stamps.map { JSONObject().put("key", it.key).put("day", it.day).put("count", it.count) }))
        put("diary", JSONArray(b.diary.map { JSONObject().put("day", it.day).put("text", it.text) }))
        put("meta", JSONObject(b.meta))
        put("settings", JSONObject().apply {
            put("notify", c.notify)
            c.place?.let { p -> put("place", JSONObject().put("name", p.name).put("region", p.region).put("lat", p.lat).put("lon", p.lon)) }
        })
    }.toString()

    /** Reads a backup; throws if it isn't one this app can restore (not JSON, another app, a newer version, rows missing). */
    fun read(text: String): Pair<Books, Carried> {
        val o = runCatching { JSONObject(text) }.getOrElse { throw IllegalArgumentException("not JSON", it) }
        require(o.optString("app") == APP) { "not a Lipovka backup" }
        val v = o.optInt("version", 0)
        require(v in 1..VERSION) { "unsupported version $v" }
        fun rows(key: String): List<JSONObject> = o.getJSONArray(key).let { a -> List(a.length()) { a.getJSONObject(it) } }
        val books = Books(
            mail = rows("mail").map { m ->
                Mail(
                    id = m.getLong("id"), src = m.getString("src"), kind = m.getString("kind"), to = m.getString("to"),
                    day = m.getLong("day"), state = m.getInt("state"), variant = m.optInt("variant"), priority = m.optInt("priority"),
                    deliveredAt = m.optLong("deliveredAt"), gift = m.optString("gift"), stamp = m.optString("stamp"),
                    reply = m.optString("reply"), from = m.optString("from"), detour = m.optInt("detour"),
                )
            },
            days = rows("days").map { DayLog(it.getLong("day"), it.getInt("steps")) },
            flags = rows("flags").map { Flag(it.getString("key"), it.getLong("day")) },
            arcs = rows("arcs").map { ArcState(it.getString("arc"), it.getInt("n"), it.getLong("day")) },
            items = rows("items").map { Owned(it.getString("key"), it.getString("from"), it.getLong("day")) },
            stamps = rows("stamps").map { Collected(it.getString("key"), it.getLong("day"), it.optInt("count", 1)) },
            diary = rows("diary").map { Diary(it.getLong("day"), it.getString("text")) },
            meta = o.getJSONObject("meta").let { m -> m.keys().asSequence().associateWith { m.getString(it) } },
        )
        require(books.meta.containsKey("start")) { "no start day" }
        val s = o.optJSONObject("settings")
        val p = s?.optJSONObject("place")
        val carried = Carried(
            place = p?.let { Place(it.getString("name"), it.optString("region"), it.getDouble("lat"), it.getDouble("lon")) },
            notify = s?.optBoolean("notify", true) ?: true,
        )
        return books to carried
    }
}
