package app.lipovka

import androidx.activity.ComponentActivity
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.test.core.app.ApplicationProvider
import app.lipovka.data.DemoSeed
import app.lipovka.data.St
import app.lipovka.domain.Env
import app.lipovka.domain.Look
import app.lipovka.domain.Sky
import app.lipovka.domain.SunTimes
import app.lipovka.domain.WeatherNow
import app.lipovka.ui.Home
import app.lipovka.ui.album.AlbumScreen
import app.lipovka.ui.art.Art
import app.lipovka.ui.diary.DiaryScreen
import app.lipovka.ui.onboarding.Onboarding
import app.lipovka.ui.post.Evening
import app.lipovka.ui.post.Gate
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.unit.dp
import app.lipovka.ui.post.LetterScreen
import app.lipovka.ui.post.PostScreen
import app.lipovka.ui.room.RoomScreen
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.LipovkaTheme
import app.lipovka.ui.village.VillageScreen
import kotlinx.coroutines.runBlocking
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode
import java.io.File
import java.time.LocalDateTime

/** Every main screen over the demo village, drawn to PNGs (run with `-Prender`), in both languages. */
@RunWith(RobolectricTestRunner::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
abstract class ScreensBase {
    @get:Rule val rule = createAndroidComposeRule<ComponentActivity>()
    abstract val lang: String
    private val out by lazy { File(System.getProperty("render.out") ?: "build/art", "screens-$lang").apply { mkdirs() } }

    @Before fun still() {
        Art.still = true
    }

    private fun env(hour: Int, sky: Sky, temp: Double, month: Int = 10, day: Int = 22, looks: Set<Look> = emptySet()): Env =
        Env.build(LocalDateTime.of(2026, month, day, hour, 15), SunTimes(7 * 60 + 20, 17 * 60 + 40), WeatherNow(sky, temp, 3.0, 0), true, looks)

    private fun home(e: Env = env(8, Sky.RAIN, 8.0)): Home = runBlocking {
        val app = ApplicationProvider.getApplicationContext<LipovkaApp>()
        val c = app.container
        DemoSeed.seedIfEmpty(app, c)
        c.post.refresh()
        Home(c.post.state.value!!, c.settings.now(), c.content, c.game, e, LocalDateTime.now().withHour(e.hour).withMinute(15), app.ru)
    }

    private fun shot(name: String, content: @Composable () -> Unit) {
        rule.mainClock.autoAdvance = false
        rule.setContent { LipovkaTheme { Box(Modifier.fillMaxSize().background(C.paper)) { content() } } }
        rule.mainClock.advanceTimeBy(2_000)
        rule.waitForIdle()
        rule.mainClock.advanceTimeBy(500)
        rule.runOnUiThread {
            val view = rule.activity.window.decorView
            val image = android.graphics.Bitmap.createBitmap(view.width, view.height, android.graphics.Bitmap.Config.ARGB_8888)
            view.draw(android.graphics.Canvas(image))
            File(out, "$name.png").outputStream().use { image.compress(android.graphics.Bitmap.CompressFormat.PNG, 100, it) }
        }
    }

    @Test fun welcome() = shot("0-welcome") { Onboarding() }
    @Test fun post() = home().let { h -> shot("1-post") { PostScreen(h, {}, {}, {}) } }
    @Test fun gate() = home().let { h ->
        val m = h.s.mail.lastOrNull { it.state == St.DELIVERED && it.src.startsWith("arc:") } ?: h.s.mail.last { it.state == St.SEEN && it.src.startsWith("arc:") && it.to != "me" }
        shot("2-gate") { Gate(h, m, preview = true) {} }
    }
    @Test fun village() = home(env(13, Sky.CLOUDY, 11.0, month = 9, day = 25, looks = setOf(Look.CRANES))).let { h -> shot("3-village") { VillageScreen(h) {} } }
    @Test fun room() = home(env(21, Sky.SNOW, -5.0, month = 12, day = 30, looks = setOf(Look.NEWYEAR))).let { h -> shot("4-room") { RoomScreen(h) } }
    @Test fun album() = home().let { h -> shot("5-album") { AlbumScreen(h) } }
    @Test fun evening() = home(env(20, Sky.RAIN, 6.0)).let { h -> shot("6-evening") { androidx.compose.foundation.layout.Column(Modifier.padding(16.dp)) { Evening(h) } } }
    @Test fun diary() = home().let { h -> shot("7-diary") { DiaryScreen(h) {} } }
    @Test fun letter() = home().let { h ->
        val m = h.s.mail.last { it.to == "me" && it.src.startsWith("arc:me_") }
        shot("8-letter") { LetterScreen(h, m.id) {} }
    }
}

@Config(sdk = [34], qualifiers = "en-w411dp-h891dp-xxhdpi")
class RenderArtScreensEn : ScreensBase() { override val lang = "en" }

@Config(sdk = [34], qualifiers = "ru-w411dp-h891dp-xxhdpi")
class RenderArtScreensRu : ScreensBase() { override val lang = "ru" }
