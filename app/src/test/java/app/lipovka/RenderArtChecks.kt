package app.lipovka

import android.app.NotificationManager
import androidx.activity.ComponentActivity
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.test.hasSetTextAction
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onAllNodesWithText
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performTextInput
import androidx.compose.ui.test.performTextReplacement
import androidx.compose.ui.unit.dp
import androidx.test.core.app.ApplicationProvider
import app.lipovka.data.DemoSeed
import app.lipovka.data.St
import app.lipovka.domain.Env
import app.lipovka.domain.Place
import app.lipovka.domain.Sky
import app.lipovka.domain.SunTimes
import app.lipovka.domain.WeatherNow
import app.lipovka.ui.Home
import app.lipovka.ui.art.Art
import app.lipovka.ui.post.Evening
import app.lipovka.ui.post.PostScreen
import app.lipovka.ui.settings.SettingsScreen
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.LipovkaTheme
import app.lipovka.work.Notes
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.Shadows.shadowOf
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode
import java.io.File
import java.time.LocalDate
import java.time.LocalDateTime

/** Checks of the evening, the way home, the place field and the delivery note over the demo village (`-Prender`). */
@RunWith(RobolectricTestRunner::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
@Config(sdk = [34], qualifiers = "ru-w411dp-h891dp-xxhdpi")
class RenderArtChecks {
    @get:Rule val rule = createAndroidComposeRule<ComponentActivity>()
    private val out by lazy { File(System.getProperty("render.out") ?: "build/art", "checks").apply { mkdirs() } }
    private val la get() = ApplicationProvider.getApplicationContext<LipovkaApp>()

    @Before fun still() { Art.still = true }

    private fun home(now: LocalDateTime): Home = runBlocking {
        val c = la.container
        DemoSeed.seedIfEmpty(la, c)
        c.post.refresh()
        // November: the sun rises at 7:40 and sets at 16:20
        val env = Env.build(now, SunTimes(7 * 60 + 40, 16 * 60 + 20), WeatherNow(Sky.CLOUDY, 2.0, 3.0, 0), true, emptySet())
        Home(c.post.state.value!!, c.settings.now(), c.content, c.game, env, now, la.ru)
    }

    private fun show(name: String, content: @Composable () -> Unit) {
        rule.mainClock.autoAdvance = false
        rule.setContent { LipovkaTheme { Box(Modifier.fillMaxSize().background(C.paper)) { content() } } }
        rule.mainClock.advanceTimeBy(1_500)
        rule.waitForIdle()
        rule.runOnUiThread {
            val view = rule.activity.window.decorView
            val image = android.graphics.Bitmap.createBitmap(view.width, view.height, android.graphics.Bitmap.Config.ARGB_8888)
            view.draw(android.graphics.Canvas(image))
            File(out, "$name.png").outputStream().use { image.compress(android.graphics.Bitmap.CompressFormat.PNG, 100, it) }
        }
    }

    private fun count(text: String) = rule.onAllNodesWithText(text, substring = true, ignoreCase = true).fetchSemanticsNodes().size

    private val today get() = LocalDate.now()

    /** #37: five past midnight is the night of the day just walked, not an evening of the new one. */
    @Test fun midnight() {
        val h = home(today.atTime(0, 5))
        show("night-0005") { Column(Modifier.padding(16.dp)) { Evening(h) } }
        val tomorrowName = app.lipovka.ui.Words.date(la, today.toEpochDay())
        assertEquals(1, count("Ночь на $tomorrowName"))
        assertEquals(0, count("Вечер,"))
    }

    /** #37: a dark November morning before work has no evening block. */
    @Test fun darkMorning() {
        val h = home(today.atTime(6, 30))
        assertEquals(app.lipovka.domain.Phase.NIGHT, h.env.phase)
        show("post-0630") { PostScreen(h, {}, {}, {}) }
        assertEquals(0, count("дневник почтальона"))
    }

    @Test fun evening() {
        val h = home(today.atTime(19, 0))
        show("post-1900") { PostScreen(h, {}, {}, {}) }
        assertEquals(1, count("дневник почтальона"))
        assertEquals(1, count("Вечер, "))
    }

    /** #45: typing, pasting and replacing in the evening diary doesn't bring the app down. */
    @Test fun diaryTyping() {
        val h = home(today.atTime(21, 0))
        show("evening-typing") { Column(Modifier.padding(16.dp)) { Evening(h) } }
        val field = rule.onNode(hasSetTextAction())
        field.performClick()
        repeat(30) { i -> field.performTextInput(if (i % 5 == 0) "слово за словом, " else "а") }
        field.performTextReplacement("Длинная строка ".repeat(60))
        field.performTextReplacement("коротко")
        field.performTextInput(" и ещё целое предложение из подсказки клавиатуры")
        rule.mainClock.advanceTimeBy(2_000)
        rule.waitForIdle()
    }

    /** #44, #48, #7: the way home, yesterday's steps and "take more" with an empty bag. */
    @Test fun wayHome() {
        runBlocking {
            DemoSeed.seedIfEmpty(la, la.container)
            la.container.post.change { s ->
                for (m in s.bag) s.put(m.copy(state = St.SEEN, deliveredAt = System.currentTimeMillis()))
                s.at = "mill"; s.leg = 300; s.heading = "post"
            }
        }
        val h = home(today.atTime(14, 0))
        assertTrue(h.game.homing(h.s))
        show("post-homing") { PostScreen(h, {}, {}, {}) }
        assertEquals(1, count("иду на почту"))
        assertEquals(1, count("вчера:"))
        assertEquals(1, count("Взять ещё"))
    }

    /** #32: the place chosen is in the search field when settings are opened again. */
    @Test fun placeKept() {
        runBlocking { DemoSeed.seedIfEmpty(la, la.container); la.container.settings.update { it.copy(place = Place("Вологда", "Вологодская область", 59.2, 39.9)) } }
        val h = home(today.atTime(12, 0))
        show("settings-place") { SettingsScreen(h) {} }
        rule.onNode(hasSetTextAction() and hasText("Вологда")).assertExists()
    }

    /** #39: a delivered letter gives a note when asked for, with the next stop. */
    @Test fun deliveredNote() {
        shadowOf(la).grantPermissions(android.Manifest.permission.POST_NOTIFICATIONS)
        val c = la.container
        val mail = runBlocking {
            DemoSeed.seedIfEmpty(la, c)
            c.settings.update { it.copy(notify = true, notifyDelivered = false) }
            c.post.refresh()
            c.post.state.value!!.mail.first { it.state == St.SEEN && it.to != "me" && it.src.startsWith("arc:") }
        }
        val nm = la.getSystemService(NotificationManager::class.java)
        runBlocking { Notes.delivered(la, listOf(mail)) }
        assertEquals("off by default: no note", 0, shadowOf(nm).allNotifications.size)
        runBlocking { c.settings.update { it.copy(notifyDelivered = true) }; Notes.delivered(la, listOf(mail)) }
        val n = shadowOf(nm).allNotifications.single()
        val title = n.extras.getString(android.app.Notification.EXTRA_TITLE)
        val text = n.extras.getCharSequence(android.app.Notification.EXTRA_BIG_TEXT).toString()
        File(out, "note.txt").writeText("$title\n$text")
        assertEquals("Доставлено 1 письмо", title)
        assertTrue(text, text.contains("Дальше:") || text.contains("Сумка пуста"))
    }
}
