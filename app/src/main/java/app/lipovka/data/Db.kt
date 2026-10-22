package app.lipovka.data

import android.content.Context
import androidx.room.Dao
import androidx.room.Database
import androidx.room.Entity
import androidx.room.Index
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.PrimaryKey
import androidx.room.Query
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.Upsert
import kotlinx.coroutines.flow.Flow

/** Where a piece of mail is. */
object St {
    /** Waiting at the post office for a lighter day. */
    const val SHELF = 0
    /** In the bag, on today's round. */
    const val BAG = 1
    /** Delivered; the visit at the gate hasn't been seen yet. */
    const val DELIVERED = 2
    /** Delivered and seen. */
    const val SEEN = 3
    /** A letter to the postman, lying on the desk unread. */
    const val DESK = 4
    /** Thrown out unused (an old filler that waited too long). */
    const val GONE = 5
}

/**
 * One piece of mail. [src] says where its words come from: `arc:<arc>:<n>`, `tpl:<key>`, `fill:<index>`,
 * `evt:<key>` or `reply:<mail id>`; [variant] picks a template's variant.
 */
@Entity(tableName = "mail", indices = [Index("state"), Index("to")])
data class Mail(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val src: String,
    val kind: String,
    val to: String,
    /** The epoch day it arrived at the post office. */
    val day: Long,
    val state: Int,
    val variant: Int = 0,
    /** Higher goes into the bag first: telegrams and dated mail before everyday letters. */
    val priority: Int = 0,
    val deliveredAt: Long = 0,
    val gift: String = "",
    val stamp: String = "",
    val reply: String = "",
    /** For a reply: who wrote it. */
    val from: String = "",
)

/** Steps walked on one day. */
@Entity(tableName = "day")
data class DayLog(@PrimaryKey val day: Long, val steps: Int)

/** A raw reading of the phone's step counter (it counts from boot). */
@Entity(tableName = "reading")
data class Reading(@PrimaryKey(autoGenerate = true) val id: Long = 0, val at: Long, val value: Long)

@Entity(tableName = "flag")
data class Flag(@PrimaryKey val key: String, val day: Long)

/** How far an arc has gone: [n] beats delivered, the last on [day]. */
@Entity(tableName = "arc")
data class ArcState(@PrimaryKey val arc: String, val n: Int, val day: Long)

@Entity(tableName = "item")
data class Owned(@PrimaryKey val key: String, val from: String, val day: Long)

@Entity(tableName = "stamp")
data class Collected(@PrimaryKey val key: String, val day: Long, val count: Int = 1)

@Entity(tableName = "diary")
data class Diary(@PrimaryKey val day: Long, val text: String)

/** Small values: the round's position, the counter baseline, the start day. */
@Entity(tableName = "meta")
data class Meta(@PrimaryKey val k: String, val v: String)

@Dao
interface PostDao {
    @Query("SELECT * FROM mail WHERE state IN (0,1,2,4) ORDER BY id")
    fun liveFlow(): Flow<List<Mail>>

    @Query("SELECT * FROM mail WHERE state IN (0,1,2,4) ORDER BY id")
    suspend fun live(): List<Mail>

    @Query("SELECT * FROM mail ORDER BY id")
    fun allFlow(): Flow<List<Mail>>

    @Query("SELECT * FROM mail ORDER BY id")
    suspend fun all(): List<Mail>

    @Query("SELECT * FROM mail WHERE `to` = :to AND state IN (2,3) ORDER BY deliveredAt")
    suspend fun deliveredTo(to: String): List<Mail>

    @Query("SELECT * FROM mail WHERE id = :id")
    suspend fun mail(id: Long): Mail?

    @Insert
    suspend fun insert(m: Mail): Long

    @Upsert
    suspend fun update(m: Mail)

    @Query("UPDATE mail SET state = :state WHERE id = :id")
    suspend fun setState(id: Long, state: Int)

    @Query("SELECT * FROM day ORDER BY day")
    fun daysFlow(): Flow<List<DayLog>>

    @Query("SELECT * FROM day ORDER BY day")
    suspend fun days(): List<DayLog>

    @Query("SELECT * FROM day WHERE day = :day")
    suspend fun day(day: Long): DayLog?

    @Upsert
    suspend fun putDay(d: DayLog)

    @Query("SELECT * FROM reading ORDER BY id DESC LIMIT 1")
    suspend fun lastReading(): Reading?

    @Insert
    suspend fun addReading(r: Reading)

    @Query("DELETE FROM reading WHERE id < (SELECT MAX(id) - 200 FROM reading)")
    suspend fun trimReadings()

    @Query("SELECT * FROM flag")
    fun flagsFlow(): Flow<List<Flag>>

    @Query("SELECT * FROM flag")
    suspend fun flags(): List<Flag>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun setFlag(f: Flag)

    @Query("SELECT * FROM arc")
    suspend fun arcs(): List<ArcState>

    @Upsert
    suspend fun putArc(a: ArcState)

    @Query("SELECT * FROM item ORDER BY day DESC")
    fun itemsFlow(): Flow<List<Owned>>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun addItem(o: Owned)

    @Query("SELECT * FROM stamp ORDER BY day DESC")
    fun stampsFlow(): Flow<List<Collected>>

    @Query("SELECT * FROM stamp WHERE `key` = :key")
    suspend fun stamp(key: String): Collected?

    @Upsert
    suspend fun putStamp(c: Collected)

    @Query("SELECT * FROM diary ORDER BY day DESC")
    fun diaryFlow(): Flow<List<Diary>>

    @Upsert
    suspend fun putDiary(d: Diary)

    @Query("DELETE FROM diary WHERE day = :day")
    suspend fun dropDiary(day: Long)

    @Query("SELECT * FROM meta")
    fun metaFlow(): Flow<List<Meta>>

    @Query("SELECT * FROM meta")
    suspend fun metaAll(): List<Meta>

    @Query("SELECT * FROM item")
    suspend fun itemsOnce(): List<Owned>

    @Query("SELECT * FROM stamp")
    suspend fun stampsOnce(): List<Collected>

    @Query("SELECT v FROM meta WHERE k = :k")
    suspend fun meta(k: String): String?

    @Upsert
    suspend fun putMeta(m: Meta)
}

@Database(
    entities = [Mail::class, DayLog::class, Reading::class, Flag::class, ArcState::class, Owned::class, Collected::class, Diary::class, Meta::class],
    version = 1,
    exportSchema = true,
)
abstract class PostDb : RoomDatabase() {
    abstract fun dao(): PostDao

    companion object {
        fun create(context: Context): PostDb = Room.databaseBuilder(context, PostDb::class.java, "lipovka.db").build()
        fun memory(context: Context): PostDb = Room.inMemoryDatabaseBuilder(context, PostDb::class.java).build()
    }
}
