package app.lipovka

import android.app.Application
import android.content.Context
import android.content.res.Configuration
import androidx.appcompat.app.AppCompatDelegate
import app.lipovka.data.Content
import app.lipovka.data.DemoSeed
import app.lipovka.data.Event
import app.lipovka.data.Post
import app.lipovka.data.PostDb
import app.lipovka.data.Settings
import app.lipovka.data.SettingsStore
import app.lipovka.domain.Cal
import app.lipovka.domain.Env
import app.lipovka.domain.Game
import app.lipovka.domain.GameState
import app.lipovka.domain.Look
import app.lipovka.domain.Sun
import app.lipovka.domain.Weather
import app.lipovka.work.Alarms
import app.lipovka.work.StepSensor
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.time.LocalDate
import java.time.LocalDateTime

class AppContainer(context: Context) {
    val app = context.applicationContext
    val db = PostDb.create(app)
    val settings = SettingsStore(app)
    val content = Content.load(app)
    val game = Game(content)
    val post = Post(db, game)
    val sensor = StepSensor(app)
    val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

    /** Fire-and-forget so a write survives the screen being closed right after tapping. */
    fun write(block: suspend AppContainer.() -> Unit) {
        scope.launch { block() }
    }

    /** The events going on today in the districts already open. */
    fun events(date: LocalDate, s: GameState?): List<Event> =
        content.events.filter { Cal.within(date, it.start, it.end) && (s == null || s.open(it.district)) }

    /** The world outside right now, as the scenes should draw it. */
    fun env(now: LocalDateTime, settings: Settings, s: GameState?): Env {
        val p = settings.place
        val sun = p?.let { Sun.times(now.toLocalDate(), it.lat, it.lon) } ?: Sun.fallback(now.toLocalDate())
        val w = settings.weather
        val fresh = p != null && w != null && System.currentTimeMillis() - w.at < Weather.FRESH_MS
        val south = (p?.lat ?: 1.0) < 0
        val weather = if (fresh) w!! else Weather.simulated(now, Cal.villageMonth(now.toLocalDate(), south))
        val looks = events(now.toLocalDate(), s).map { Look.of(it.look) }.filter { it != Look.NONE }.toSet()
        return Env.build(now, sun, weather, fresh, looks, south)
    }

    /** Fetches the weather if a place is set and the last report is over an hour old. */
    suspend fun refreshWeather(force: Boolean = false) {
        val s = settings.now()
        val p = s.place ?: return
        val w = s.weather
        if (!force && w != null && System.currentTimeMillis() - w.at < 60 * 60 * 1000L) return
        val now = runCatching { withContext(Dispatchers.IO) { Weather.fetch(p.lat, p.lon) } }.getOrNull() ?: return
        settings.update { it.copy(weather = now) }
    }

    /** Reads the step counter and sorts the morning post. */
    suspend fun sync() {
        val v = sensor.read()
        if (v != null) post.reading(v) else post.tick()
    }
}

class LipovkaApp : Application() {
    lateinit var container: AppContainer
        private set

    override fun onCreate() {
        super.onCreate()
        container = AppContainer(this)
        if (BuildConfig.DEMO) container.scope.launch { DemoSeed.seedIfEmpty(this@LipovkaApp, container) }
        runCatching { Alarms.schedule(this) }
    }
}

val Context.container: AppContainer get() = (applicationContext as LipovkaApp).container

/** Resources in the in-app language, which AppCompat doesn't localise outside activities before Android 13. */
fun Context.localized(): Context {
    val tags = AppCompatDelegate.getApplicationLocales()
    if (tags.isEmpty) return this
    val config = Configuration(resources.configuration)
    config.setLocale(tags[0])
    return createConfigurationContext(config)
}

/** Is this context in Russian? */
val Context.ru: Boolean get() = resources.configuration.locales[0].language == "ru"
