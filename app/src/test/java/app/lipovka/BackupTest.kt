package app.lipovka

import android.app.Application
import app.lipovka.data.Backup
import app.lipovka.data.Carried
import app.lipovka.data.Content
import app.lipovka.data.Post
import app.lipovka.data.PostDb
import app.lipovka.domain.Game
import app.lipovka.domain.Place
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment
import org.robolectric.annotation.Config
import java.io.File

/** A backup written on one phone restores the same post office on another. */
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34], application = Application::class)
class BackupTest {
    private val content: Content by lazy {
        val dir = listOf(File("src/main/assets/content"), File("app/src/main/assets/content")).first { it.exists() }
        fun all(sub: String) = File(dir, sub).listFiles().orEmpty().filter { it.name.endsWith(".tsv") }.sortedBy { it.name }.map { it.readText() }
        fun opt(name: String) = File(dir, name).takeIf { it.exists() }?.readText().orEmpty()
        Content.parse(File(dir, "residents.tsv").readText(), all("arcs"), all("items"), all("stamps"), opt("templates.tsv"), opt("fillers.tsv"), opt("events.tsv"))
    }

    private fun post() = Post(PostDb.memory(RuntimeEnvironment.getApplication()), Game(content))

    @Test fun roundTrip() = runBlocking {
        val a = post()
        a.tick()
        repeat(12) { a.addSteps(1500) }
        a.state.value!!.mail.filter { it.state == app.lipovka.data.St.DELIVERED || it.state == app.lipovka.data.St.DESK }.forEach { a.open(it.id) }
        a.reading(5000)
        a.diary(a.state.value!!.start, "Первый день. Кот спит на письмах.")
        val before = a.snapshot()
        assertTrue("something was delivered", before.mail.any { it.state == app.lipovka.data.St.SEEN })
        assertTrue("days", before.days.isNotEmpty())
        assertFalse("the counter baseline stays on the phone", "lastValue" in before.meta)

        val place = Place("Тверь", "Тверская область", 56.86, 35.9)
        val text = Backup.write(before, Carried(place, notify = false))
        val (books, carried) = Backup.read(text)
        assertEquals(before, books)
        assertEquals(place, carried.place)
        assertFalse(carried.notify)

        val b = post()
        b.tick()
        b.restore(books)
        assertEquals(before, b.snapshot())
        val sa = a.state.value!!
        val sb = b.state.value!!
        assertEquals(sa.mail, sb.mail)
        assertEquals(sa.days, sb.days)
        assertEquals(sa.total, sb.total)
        assertEquals(sa.at, sb.at)
        assertEquals(sa.start, sb.start)
        assertEquals("the counter starts afresh", -1L, sb.lastValue)
        // and the game goes on from there
        b.addSteps(3000)
        assertTrue(b.state.value!!.total >= sa.total + 3000)
    }

    @Test fun refusesOtherFiles() {
        for (bad in listOf("", "hello", "{}", """{"app":"other","version":1}""", """{"app":"lipovka","version":99}"""))
            assertTrue(bad, runCatching { Backup.read(bad) }.isFailure)
    }
}
