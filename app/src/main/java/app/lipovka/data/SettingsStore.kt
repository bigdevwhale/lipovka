package app.lipovka.data

import android.content.Context
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.doublePreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.longPreferencesKey
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import app.lipovka.domain.Place
import app.lipovka.domain.Sky
import app.lipovka.domain.WeatherNow
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.map

private val Context.dataStore by preferencesDataStore("settings")

data class Settings(
    val onboarded: Boolean = false,
    /** Where the weather comes from; null keeps the village's own weather. */
    val place: Place? = null,
    val weather: WeatherNow? = null,
    /** Morning post and gentle evening reminders. */
    val notify: Boolean = true,
    /** The mail day the morning notification was last shown, and the evening one. */
    val notifiedMorning: Long = -1,
    val notifiedEvening: Long = -1,
)

class SettingsStore(context: Context) {
    private val store = context.applicationContext.dataStore

    val settings: Flow<Settings> = store.data.map { it.read() }

    private fun Preferences.read(): Settings {
        val lat = this[LAT]
        val lon = this[LON]
        val sky = Sky.of(this[SKY])
        return Settings(
            onboarded = this[ONBOARDED] ?: false,
            place = if (lat != null && lon != null) Place(this[PLACE] ?: "", this[REGION] ?: "", lat, lon) else null,
            weather = if (sky != null) WeatherNow(sky, this[TEMP] ?: 0.0, this[WIND] ?: 0.0, this[WEATHER_AT] ?: 0) else null,
            notify = this[NOTIFY] ?: true,
            notifiedMorning = this[N_MORNING] ?: -1,
            notifiedEvening = this[N_EVENING] ?: -1,
        )
    }

    suspend fun now(): Settings = settings.first()

    suspend fun update(change: (Settings) -> Settings) {
        store.edit {
            val s = change(it.read())
            it[ONBOARDED] = s.onboarded
            val p = s.place
            if (p != null) {
                it[PLACE] = p.name; it[REGION] = p.region; it[LAT] = p.lat; it[LON] = p.lon
            } else {
                it.remove(PLACE); it.remove(REGION); it.remove(LAT); it.remove(LON)
            }
            val w = s.weather
            if (w != null) {
                it[SKY] = w.sky.name; it[TEMP] = w.temp; it[WIND] = w.wind; it[WEATHER_AT] = w.at
            } else {
                it.remove(SKY); it.remove(TEMP); it.remove(WIND); it.remove(WEATHER_AT)
            }
            it[NOTIFY] = s.notify
            it[N_MORNING] = s.notifiedMorning
            it[N_EVENING] = s.notifiedEvening
        }
    }

    private companion object {
        val ONBOARDED = booleanPreferencesKey("onboarded")
        val PLACE = stringPreferencesKey("place")
        val REGION = stringPreferencesKey("region")
        val LAT = doublePreferencesKey("lat")
        val LON = doublePreferencesKey("lon")
        val SKY = stringPreferencesKey("sky")
        val TEMP = doublePreferencesKey("temp")
        val WIND = doublePreferencesKey("wind")
        val WEATHER_AT = longPreferencesKey("weather_at")
        val NOTIFY = booleanPreferencesKey("notify")
        val N_MORNING = longPreferencesKey("n_morning")
        val N_EVENING = longPreferencesKey("n_evening")
    }
}
