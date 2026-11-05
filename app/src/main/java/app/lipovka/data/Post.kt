package app.lipovka.data

import android.os.SystemClock
import androidx.room.withTransaction
import app.lipovka.domain.Game
import app.lipovka.domain.GameState
import app.lipovka.domain.Steps
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.time.LocalDateTime
import java.time.ZoneId

/**
 * The post office's books: loads the whole [GameState] from the database, lets [Game] change it
 * and writes back what changed, one change at a time. [state] always holds the latest books.
 */
class Post(private val db: PostDb, val game: Game, private val zone: () -> ZoneId = { ZoneId.systemDefault() }) {
    private val dao = db.dao()
    private val lock = Mutex()
    private val _state = MutableStateFlow<GameState?>(null)
    val state: StateFlow<GameState?> = _state

    private suspend fun load(): GameState {
        val meta = dao.metaFlowOnce()
        fun m(k: String) = meta[k]
        val s = GameState(
            start = m("start")?.toLongOrNull() ?: LocalDateTime.now(zone()).let { game.mailDay(it).toEpochDay() },
            at = m("at") ?: "post",
            leg = m("leg")?.toIntOrNull() ?: 0,
            heading = m("heading") ?: "",
            morning = m("morning")?.toLongOrNull() ?: -1,
            total = m("total")?.toLongOrNull() ?: 0,
            lastValue = m("lastValue")?.toLongOrNull() ?: -1,
            lastAt = m("lastAt")?.toLongOrNull() ?: 0,
        )
        s.mail += dao.all()
        dao.days().forEach { s.days[it.day] = it.steps }
        dao.flags().forEach { s.flags[it.key] = it.day }
        dao.arcs().forEach { s.arcs[it.arc] = it }
        dao.itemsOnce().forEach { s.items[it.key] = it }
        dao.stampsOnce().forEach { s.stamps[it.key] = it }
        if (m("start") == null) dao.putMeta(Meta("start", s.start.toString()))
        return s
    }

    private suspend fun save(s: GameState) {
        val ids = mutableMapOf<Long, Long>()
        for (m in s.newMail) {
            val real = s.mail.firstOrNull { it.id == m.id } ?: m
            ids[m.id] = dao.insert(real.copy(id = 0))
        }
        for (id in s.dirtyMail) s.mail.firstOrNull { it.id == id }?.let { dao.update(it) }
        for (d in s.dirtyDays) dao.putDay(DayLog(d, s.days[d] ?: 0))
        for (k in s.dirtyFlags) dao.setFlag(Flag(k, s.flags.getValue(k)))
        for (k in s.dirtyArcs) dao.putArc(s.arcs.getValue(k))
        for (k in s.dirtyItems) dao.addItem(s.items.getValue(k))
        for (k in s.dirtyStamps) dao.putStamp(s.stamps.getValue(k))
        dao.putMeta(Meta("at", s.at))
        dao.putMeta(Meta("leg", s.leg.toString()))
        dao.putMeta(Meta("heading", s.heading))
        dao.putMeta(Meta("morning", s.morning.toString()))
        dao.putMeta(Meta("total", s.total.toString()))
        dao.putMeta(Meta("lastValue", s.lastValue.toString()))
        dao.putMeta(Meta("lastAt", s.lastAt.toString()))
    }

    /** Runs one change against the books, saved as a single transaction. */
    suspend fun <T> change(block: (GameState) -> T): T = lock.withLock {
        var out: T? = null
        db.withTransaction {
            val s = load()
            out = block(s)
            save(s)
        }
        _state.value = db.withTransaction { load() }
        @Suppress("UNCHECKED_CAST")
        out as T
    }

    suspend fun refresh() {
        lock.withLock { _state.value = db.withTransaction { load() } }
    }

    private fun now() = LocalDateTime.now(zone())

    /** Sorts the morning post if it's a new mail day. */
    suspend fun tick(): Boolean = change { s -> game.morning(s, game.mailDay(now()), System.currentTimeMillis()) }

    /**
     * A reading of the step counter: the steps since the last one are spread over the days they were
     * walked on and carried round the village. Returns the letters delivered.
     */
    suspend fun reading(
        value: Long,
        at: Long = System.currentTimeMillis(),
        bootAt: Long = System.currentTimeMillis() - SystemClock.elapsedRealtime(),
    ): List<Mail> = change { s ->
        val out = mutableListOf<Mail>()
        if (s.lastValue >= 0) {
            val d = Steps.delta(s.lastValue, s.lastAt, value, at, bootAt)
            for ((day, n) in Steps.spread(d, if (s.lastAt > 0) s.lastAt else at, at, zone()).toSortedMap()) {
                out += game.walk(s, n, day, at)
            }
        }
        s.lastValue = value
        s.lastAt = at
        game.morning(s, game.mailDay(now()), at)
        out
    }

    /**
     * Day totals from Health Connect: whatever they hold beyond the village's own count for those days is
     * carried round. The step counter's baseline is dropped, so going back to it later starts afresh.
     */
    suspend fun health(totals: Map<Long, Long>, at: Long = System.currentTimeMillis()): List<Mail> = change { s ->
        val out = mutableListOf<Mail>()
        for ((day, n) in Steps.catchUp(s.days, totals).toSortedMap()) out += game.walk(s, n, day, at)
        s.lastValue = -1
        s.lastAt = 0
        game.morning(s, game.mailDay(now()), at)
        out
    }

    /** Steps added by hand (debug and demo builds). */
    suspend fun addSteps(n: Int) = change { s ->
        val day = now().toLocalDate().toEpochDay()
        game.walk(s, n, day, System.currentTimeMillis())
    }

    suspend fun open(id: Long) = change { s -> game.open(s, id, now().toLocalDate().toEpochDay()) }

    suspend fun takeMore() = change { s -> game.takeMore(s, game.mailDay(now())) }

    suspend fun diary(day: Long, text: String) {
        if (text.isBlank()) dao.dropDiary(day) else dao.putDiary(Diary(day, text.trim()))
    }

    val diary get() = dao.diaryFlow()

    /** Every table of the books, for a backup. The step counter's raw readings stay behind: they belong to this phone. */
    suspend fun snapshot(): Books = lock.withLock {
        db.withTransaction {
            Books(
                mail = dao.all(), days = dao.days(), flags = dao.flags(), arcs = dao.arcs(),
                items = dao.itemsOnce(), stamps = dao.stampsOnce(), diary = dao.diaryOnce(),
                meta = dao.metaFlowOnce() - COUNTER_KEYS,
            )
        }
    }

    /**
     * Replaces the books with a backup's. The counter baseline is dropped, so the next reading on this phone
     * only sets it and no steps are made up from another phone's count.
     */
    suspend fun restore(b: Books) {
        lock.withLock {
            db.withTransaction {
                dao.clearMail(); dao.clearDays(); dao.clearReadings(); dao.clearFlags(); dao.clearArcs()
                dao.clearItems(); dao.clearStamps(); dao.clearDiary(); dao.clearMeta()
                dao.putMail(b.mail); dao.putDays(b.days); dao.putFlags(b.flags); dao.putArcs(b.arcs)
                dao.putItems(b.items); dao.putStamps(b.stamps); dao.putDiaries(b.diary)
                dao.putMetas((b.meta - COUNTER_KEYS).map { (k, v) -> Meta(k, v) })
            }
            _state.value = db.withTransaction { load() }
        }
    }

    private companion object {
        /** The phone's step counter baseline: meaningless on another phone, or after a restore. */
        val COUNTER_KEYS = setOf("lastValue", "lastAt")
    }
}

/** Everything the post office keeps, as plain rows: what a backup carries. */
data class Books(
    val mail: List<Mail>,
    val days: List<DayLog>,
    val flags: List<Flag>,
    val arcs: List<ArcState>,
    val items: List<Owned>,
    val stamps: List<Collected>,
    val diary: List<Diary>,
    val meta: Map<String, String>,
)

private suspend fun PostDao.metaFlowOnce(): Map<String, String> = metaAll().associate { it.k to it.v }
