package app.lipovka

import app.lipovka.data.Content
import app.lipovka.domain.Env
import app.lipovka.domain.Look
import app.lipovka.domain.Sky
import app.lipovka.domain.SunTimes
import app.lipovka.domain.WeatherNow
import app.lipovka.domain.World
import app.lipovka.ui.art.Art
import app.lipovka.ui.art.Buf
import app.lipovka.ui.art.EveningScene
import app.lipovka.ui.art.GateScene
import app.lipovka.ui.art.Gift
import app.lipovka.ui.art.MapRound
import app.lipovka.ui.art.MapScene
import app.lipovka.ui.art.PostOffice
import app.lipovka.ui.art.RoomScene
import app.lipovka.ui.art.Scene
import app.lipovka.ui.art.StampArt
import app.lipovka.ui.art.ItemArt
import org.junit.Test
import java.io.File
import java.time.LocalDateTime

/** Draws the scenes in different seasons, weathers and hours to app/build/art/scenes (run with `-Prender`). */
class RenderArtScenes {
    private val out = File(System.getProperty("render.out") ?: "build/art", "scenes").apply { mkdirs() }
    private val content by lazy {
        val dir = File("src/main/assets/content")
        fun all(sub: String) = File(dir, sub).listFiles().orEmpty().filter { it.name.endsWith(".tsv") }.sortedBy { it.name }.map { it.readText() }
        fun opt(n: String) = File(dir, n).takeIf { it.exists() }?.readText().orEmpty()
        Content.parse(File(dir, "residents.tsv").readText(), all("arcs"), all("items"), all("stamps"), opt("templates.tsv"), opt("fillers.tsv"), opt("events.tsv"))
    }

    private fun env(month: Int, day: Int, hour: Int, sky: Sky, temp: Double, looks: Set<Look> = emptySet()): Env =
        Env.build(LocalDateTime.of(2026, month, day, hour, 10), SunTimes(7 * 60 + 10, 18 * 60 + 20), WeatherNow(sky, temp, 3.0, 0), true, looks)

    private val envs = listOf(
        "autumn-morning-rain" to env(10, 22, 8, Sky.RAIN, 8.0),
        "autumn-day-clear" to env(9, 28, 13, Sky.CLEAR, 14.0, setOf(Look.CRANES)),
        "winter-night-snow" to env(12, 30, 21, Sky.SNOW, -6.0, setOf(Look.NEWYEAR)),
        "winter-day-frost" to env(1, 20, 12, Sky.CLEAR, -18.0),
        "spring-dusk" to env(5, 12, 18, Sky.CLOUDY, 12.0, setOf(Look.LILAC)),
        "summer-day" to env(7, 10, 12, Sky.CLEAR, 24.0, setOf(Look.HAYMAKING)),
        "summer-storm" to env(7, 18, 16, Sky.STORM, 21.0),
        "autumn-fog" to env(10, 30, 9, Sky.FOG, 4.0),
    )

    private fun save(name: String, b: Buf, scale: Int = 3) = Png.write(File(out, "$name.png"), b, scale)

    private fun frame(s: Scene) = s.frame(9)

    @Test fun scenes() {
        Art.still = true
        val gifts = content.items.values.take(22).map { Gift(it.family, it.variant) }
        for ((k, pair) in envs.withIndex()) {
            val (name, e) = pair
            save("post-$name", frame(PostOffice(e, 4, true)))
            save("gate-$name", frame(GateScene(e, World.house("vetrovy")!!, content.resident("anna"), true)))
            save("room-$name", frame(RoomScene(e, gifts, true)))
            save("evening-$name", frame(EveningScene(e)))
            save("map-$name", frame(MapScene(e, k % 6, MapRound(postman = World.house("lebedev")!!.at, pending = setOf("mill", "apiary"), walking = true), true)), 2)
        }
        val e = envs.first().second
        for (r in content.residents) save("who-${r.id}", frame(GateScene(e, World.house(r.house)!!, r, false)), 2)
    }

    @Test fun sheets() {
        val items = content.items.values.toList()
        val cols = 12
        val sheet = Buf(cols * 18, ((items.size + cols - 1) / cols) * 20)
        sheet.r(0, 0, sheet.w, sheet.h, 0xFFF2E2BB.toInt())
        items.forEachIndexed { i, it -> ItemArt.draw(sheet, it.family, it.variant, (i % cols) * 18 + 9, (i / cols) * 20 + 18) }
        save("items", sheet)
        val stamps = content.stamps.values.toList()
        val st = Buf(cols * 36, ((stamps.size + cols - 1) / cols) * 42)
        st.r(0, 0, st.w, st.h, 0xFF1B2B22.toInt())
        stamps.forEachIndexed { i, s ->
            val b = StampArt.draw(s.family, s.bg, s.value)
            for (y in 0 until b.h) for (x in 0 until b.w) if (b.d[y * b.w + x] ushr 24 != 0) st.p((i % cols) * 36 + 1 + x, (i / cols) * 42 + 1 + y, b.d[y * b.w + x])
        }
        save("stamps", st, 2)
    }
}
