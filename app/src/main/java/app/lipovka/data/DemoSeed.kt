package app.lipovka.data

import android.content.Context
import app.lipovka.AppContainer
import app.lipovka.domain.Game
import app.lipovka.domain.GameState
import java.time.LocalDate
import java.time.ZoneId

/**
 * The demo build (`-Pdemo`) starts four months into the job: the rounds of those months are really
 * walked through the game, so the village, the room and the album look lived in. Today's bag is
 * half done and two neighbours wait at their gates.
 */
object DemoSeed {
    const val DAYS = 125

    private val LINES = listOf(
        "Шёл через мост под дождём, Бублик провожал до самой пасеки." to "Crossed the bridge in the rain; Bublik saw me all the way to the apiary.",
        "Агафья Петровна опять сунула пирожок. Отказаться невозможно." to "Agafya Petrovna slipped me a pie again. Impossible to say no.",
        "Туман над Липкой такой, что мельница шумела из ниоткуда." to "Fog over the Lipka so thick the mill was rumbling out of nowhere.",
        "Варя спросила, бывают ли письма без марок. Бывают, но грустные." to "Varya asked if there are letters without stamps. There are, but they're sad.",
        "Первый снег. Следы до самого клуба, и все мои." to "First snow. Footprints all the way to the club, and every one of them mine.",
        "Сургуч спал на заказном. Пришлось ждать." to "Surguch slept on the registered letter. I had to wait.",
    )

    suspend fun seedIfEmpty(context: Context, c: AppContainer) {
        if (c.db.dao().all().isNotEmpty()) return
        val ru = context.resources.configuration.locales[0].language == "ru"
        c.settings.update { it.copy(onboarded = true) }
        val zone = ZoneId.systemDefault()
        val today = LocalDate.now()
        val lines = mutableListOf<Pair<Long, String>>()
        c.post.change { s ->
            s.start = today.minusDays(DAYS.toLong()).toEpochDay()
            walkDays(c.game, s, today, zone)
            for (i in 0 until DAYS step 9) {
                val d = today.minusDays((DAYS - i).toLong()).toEpochDay()
                val (r, e) = LINES[(i / 9) % LINES.size]
                lines += d to if (ru) r else e
            }
        }
        for ((d, t) in lines) c.post.diary(d, t)
    }

    /** Walks every past day: the morning post, a day's steps in five outings, every gate visited. */
    fun walkDays(game: Game, s: GameState, today: LocalDate, zone: ZoneId) {
        for (i in DAYS downTo 1) {
            val date = today.minusDays(i.toLong())
            val day = date.toEpochDay()
            game.morning(s, date, date.atTime(7, 0).atZone(zone).toInstant().toEpochMilli())
            val steps = 5200 + (app.lipovka.ui.art.hash(day.toInt(), 5) * 6200).toInt()
            for (k in 0 until 5) {
                val at = date.atTime(9 + k * 2, 30).atZone(zone).toInstant().toEpochMilli()
                game.walk(s, steps / 5, day, at)
            }
            for (m in s.mail.filter { it.state == St.DELIVERED || it.state == St.DESK }) game.open(s, m.id, day)
        }
        // today: the post sorted, half the round walked, two gates waiting
        val now = System.currentTimeMillis()
        game.morning(s, today, now)
        val plan = game.plan(s)
        if (plan.size >= 2) game.walk(s, plan[1].cum + 120, today.toEpochDay(), now) else game.walk(s, 3100, today.toEpochDay(), now)
    }
}
