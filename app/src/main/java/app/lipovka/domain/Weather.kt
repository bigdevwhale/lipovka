package app.lipovka.domain

import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL
import java.net.URLEncoder
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.ZoneId

enum class Sky { CLEAR, CLOUDY, OVERCAST, FOG, DRIZZLE, RAIN, STORM, SNOW, SLEET;

    val rain get() = this == DRIZZLE || this == RAIN || this == STORM || this == SLEET
    val snow get() = this == SNOW || this == SLEET
    val grey get() = this != CLEAR && this != CLOUDY

    companion object {
        /** The WMO weather code Open-Meteo reports. */
        fun wmo(code: Int): Sky = when (code) {
            0, 1 -> CLEAR
            2 -> CLOUDY
            3 -> OVERCAST
            45, 48 -> FOG
            51, 53, 55, 56, 57 -> DRIZZLE
            61, 63, 65, 80, 81, 82 -> RAIN
            66, 67 -> SLEET
            71, 73, 75, 77, 85, 86 -> SNOW
            95, 96, 99 -> STORM
            else -> CLOUDY
        }

        fun of(s: String?) = entries.firstOrNull { it.name == s }
    }
}

/** The weather now, as last fetched. */
data class WeatherNow(val sky: Sky, val temp: Double, val wind: Double, val at: Long)

/** A place the player picked for their weather. */
data class Place(val name: String, val region: String, val lat: Double, val lon: Double)

object Weather {
    /** Real weather is kept for three hours; older than that the village falls back to its own. */
    const val FRESH_MS = 3 * 60 * 60 * 1000L

    private fun get(url: String): String {
        val c = URL(url).openConnection() as HttpURLConnection
        c.connectTimeout = 6000
        c.readTimeout = 8000
        c.setRequestProperty("User-Agent", "Lipovka/1.0 github.com/bigdevwhale/lipovka")
        try {
            if (c.responseCode !in 200..299) error("HTTP ${c.responseCode}")
            return c.inputStream.bufferedReader().use { it.readText() }
        } finally {
            c.disconnect()
        }
    }

    /**
     * The current weather at a place: from Open-Meteo, or from MET Norway when Open-Meteo can't be
     * reached (some networks block it). No key; nothing but the coordinates is sent.
     */
    fun fetch(lat: Double, lon: Double, now: Long = System.currentTimeMillis()): WeatherNow =
        runCatching { openMeteo(lat, lon, now) }.getOrElse { metNo(lat, lon, now) }

    private fun openMeteo(lat: Double, lon: Double, now: Long): WeatherNow {
        val j = JSONObject(get("https://api.open-meteo.com/v1/forecast?latitude=%.3f&longitude=%.3f&current=temperature_2m,weather_code,wind_speed_10m".format(java.util.Locale.US, lat, lon)))
        val cur = j.getJSONObject("current")
        return WeatherNow(Sky.wmo(cur.getInt("weather_code")), cur.getDouble("temperature_2m"), cur.optDouble("wind_speed_10m", 0.0), now)
    }

    private fun metNo(lat: Double, lon: Double, now: Long): WeatherNow {
        val j = JSONObject(get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=%.3f&lon=%.3f".format(java.util.Locale.US, lat, lon)))
        val first = j.getJSONObject("properties").getJSONArray("timeseries").getJSONObject(0).getJSONObject("data")
        val d = first.getJSONObject("instant").getJSONObject("details")
        val symbol = first.optJSONObject("next_1_hours")?.optJSONObject("summary")?.optString("symbol_code")
            ?: first.optJSONObject("next_6_hours")?.optJSONObject("summary")?.optString("symbol_code") ?: "cloudy"
        return WeatherNow(symbol(symbol), d.getDouble("air_temperature"), d.optDouble("wind_speed", 0.0) * 3.6, now)
    }

    /** MET Norway's symbol codes ("lightrainshowers_day", "fog"…) as the village's skies. */
    fun symbol(code: String): Sky {
        val c = code.substringBefore('_')
        return when {
            "thunder" in c -> Sky.STORM
            "sleet" in c -> Sky.SLEET
            "snow" in c -> Sky.SNOW
            c.startsWith("light") && "rain" in c -> Sky.DRIZZLE
            "rain" in c -> Sky.RAIN
            c == "fog" -> Sky.FOG
            c == "cloudy" -> Sky.OVERCAST
            c == "partlycloudy" -> Sky.CLOUDY
            else -> Sky.CLEAR
        }
    }

    /** Towns matching a name, for the settings search. */
    fun search(name: String, lang: String): List<Place> {
        val q = URLEncoder.encode(name.trim(), "UTF-8")
        val j = JSONObject(get("https://geocoding-api.open-meteo.com/v1/search?name=$q&count=8&language=$lang&format=json"))
        val r = j.optJSONArray("results") ?: return emptyList()
        return (0 until r.length()).map { i ->
            val o = r.getJSONObject(i)
            Place(
                o.getString("name"),
                listOf(o.optString("admin1"), o.optString("country")).filter { it.isNotBlank() }.joinToString(", "),
                o.getDouble("latitude"), o.getDouble("longitude"),
            )
        }
    }

    /**
     * The village's own weather when there is no real one: plausible for the month, the same for
     * everyone at the same hour, changing every three hours.
     */
    fun simulated(at: LocalDateTime, month: Int): WeatherNow {
        val slot = at.toLocalDate().toEpochDay().toInt() * 8 + at.hour / 3
        val r = hash(slot, 77)
        val day = hash(at.toLocalDate().toEpochDay().toInt(), 13)
        val winter = month in listOf(12, 1, 2)
        val sky = when {
            winter && r < .28 -> Sky.SNOW
            winter && r < .55 -> Sky.OVERCAST
            winter && r < .75 -> Sky.CLOUDY
            winter -> Sky.CLEAR
            month in listOf(3, 11) && r < .12 -> Sky.SLEET
            month in listOf(9, 10, 11) && r < .3 -> Sky.RAIN
            month in listOf(9, 10, 11) && r < .42 -> Sky.FOG
            month in listOf(6, 7, 8) && r < .08 -> Sky.STORM
            r < .2 -> Sky.RAIN
            r < .4 -> Sky.OVERCAST
            r < .65 -> Sky.CLOUDY
            else -> Sky.CLEAR
        }
        val base = doubleArrayOf(-9.0, -8.0, -2.0, 6.0, 13.0, 17.0, 19.0, 17.0, 11.0, 5.0, -1.0, -6.0)[month - 1]
        val hourly = -3 * kotlin.math.cos((at.hour - 3) / 24.0 * 2 * Math.PI)
        return WeatherNow(sky, base + hourly + (day - .5) * 8, 2 + r * 6, 0)
    }

    private fun hash(i: Int, j: Int): Double = app.lipovka.ui.art.hash(i, j)

    fun localNow(zone: ZoneId = ZoneId.systemDefault()): LocalDateTime = LocalDateTime.now(zone)
    fun today(zone: ZoneId = ZoneId.systemDefault()): LocalDate = LocalDate.now(zone)
}
