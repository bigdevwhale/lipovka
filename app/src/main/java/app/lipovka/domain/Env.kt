package app.lipovka.domain

import java.time.LocalDate
import java.time.LocalDateTime

/** The light of the day. */
enum class Phase { NIGHT, DAWN, MORNING, DAY, DUSK, EVENING;

    val dark get() = this == NIGHT || this == EVENING
    val lamps get() = this == NIGHT || this == EVENING || this == DUSK || this == DAWN
}

/** How the village looks during a seasonal event. */
enum class Look { FAIR, NEWYEAR, MASLENITSA, KUPALA, HAYMAKING, HARVEST, CRANES, FIRSTSNOW, ICEBREAK, FISHING, RAILWAY,
    APPLES, MUSHROOMS, SCHOOL, LILAC, SWALLOWS, FROST, BERRIES, NONE;

    companion object {
        fun of(s: String?) = entries.firstOrNull { it.name.equals(s, true) } ?: NONE
    }
}

/**
 * Everything a scene needs to know about the world outside right now: the season, the weather,
 * the light, the event going on. Built from the clock, the place and the last weather report.
 */
data class Env(
    val date: LocalDate,
    /** Minutes after midnight. */
    val minute: Int,
    val month: Int,
    val season: Season,
    val leaves: Leaves,
    val snow: Boolean,
    val ice: Boolean,
    val sky: Sky,
    val temp: Int,
    val wind: Double,
    val phase: Phase,
    /** 0 at night … 1 at noon: how much daylight there is. */
    val light: Float,
    val looks: Set<Look>,
    /** Real weather (true) or the village's own. */
    val real: Boolean,
) {
    val look: Look get() = looks.firstOrNull() ?: Look.NONE
    fun has(l: Look) = l in looks
    val hour get() = minute / 60

    companion object {
        fun phase(minute: Int, sun: SunTimes): Phase = when {
            minute < sun.rise - 45 || minute > sun.set + 75 -> Phase.NIGHT
            minute < sun.rise + 40 -> Phase.DAWN
            minute < 11 * 60 && minute < sun.set - 90 -> Phase.MORNING
            minute < sun.set - 70 -> Phase.DAY
            minute < sun.set + 20 -> Phase.DUSK
            else -> Phase.EVENING
        }

        fun light(minute: Int, sun: SunTimes): Float {
            val a = sun.rise - 40
            val b = sun.set + 50
            if (minute <= a || minute >= b) return 0f
            val t = (minute - a).toFloat() / (b - a)
            return (kotlin.math.sin(t * Math.PI)).toFloat().coerceIn(0f, 1f)
        }

        fun build(at: LocalDateTime, sun: SunTimes, weather: WeatherNow, real: Boolean, looks: Set<Look>, south: Boolean = false): Env {
            val d = at.toLocalDate()
            val m = Cal.villageMonth(d, south)
            val minute = at.hour * 60 + at.minute
            var sky = weather.sky
            // Rain below freezing is snow in the picture, snow on a warm day is rain.
            if (sky.rain && weather.temp < -1) sky = Sky.SNOW
            if (sky == Sky.SNOW && weather.temp > 4) sky = Sky.RAIN
            return Env(
                date = d, minute = minute, month = m, season = Cal.season(m), leaves = Cal.leaves(m, d.dayOfMonth),
                snow = Cal.snowGround(m, d.dayOfMonth, if (real) weather.temp else null), ice = Cal.riverIce(m, d.dayOfMonth),
                sky = sky, temp = kotlin.math.round(weather.temp).toInt(), wind = weather.wind,
                phase = phase(minute, sun), light = light(minute, sun), looks = looks, real = real,
            )
        }
    }
}
