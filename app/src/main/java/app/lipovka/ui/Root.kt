package app.lipovka.ui

import androidx.activity.compose.BackHandler
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.isImeVisible
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.Immutable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.LifecycleResumeEffect
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Content
import app.lipovka.data.Settings
import app.lipovka.data.St
import app.lipovka.domain.Env
import app.lipovka.domain.Game
import app.lipovka.domain.GameState
import app.lipovka.ru
import app.lipovka.ui.album.AlbumScreen
import app.lipovka.ui.diary.DiaryScreen
import app.lipovka.ui.onboarding.Onboarding
import app.lipovka.ui.post.LetterScreen
import app.lipovka.ui.post.PostScreen
import app.lipovka.ui.post.VisitScreen
import app.lipovka.ui.room.RoomScreen
import app.lipovka.ui.settings.SettingsScreen
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import app.lipovka.ui.village.ResidentSheet
import app.lipovka.ui.village.VillageScreen
import app.lipovka.work.PostWidget
import app.lipovka.work.WalkService
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.conflate
import kotlinx.coroutines.launch
import java.time.LocalDateTime

/** Everything a screen reads, at one moment. */
@Immutable
class Home(val s: GameState, val settings: Settings, val content: Content, val game: Game, val env: Env, val now: LocalDateTime, val ru: Boolean) {
    val today: Long = game.mailDay(now).toEpochDay()
    val year: Int = ((today - s.start) / 365 + 1).toInt().coerceAtLeast(1)
    val stepsToday: Int = s.days[now.toLocalDate().toEpochDay()] ?: 0
    val plan = game.plan(s)
    val desk = s.mail.filter { it.state == St.DESK }
    val visits = s.mail.filter { it.state == St.DELIVERED }.sortedBy { it.deliveredAt }
    val dog = s.has("dog")
    val open: Int = (5 downTo 1).firstOrNull { s.has("d$it") } ?: 0
    fun resident(id: String) = content.resident(id)
}

enum class Tab { POST, VILLAGE, ROOM, ALBUM, DIARY }

sealed interface Overlay {
    data object Visits : Overlay
    data class Letter(val id: Long) : Overlay
    data class Resident(val house: String) : Overlay
    data object Settings : Overlay
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun LipovkaRoot(settings: Settings) {
    val ctx = LocalContext.current
    val c = ctx.container
    val state by c.post.state.collectAsStateWithLifecycle()
    var now by remember { mutableStateOf(LocalDateTime.now()) }
    LaunchedEffect(Unit) {
        c.post.refresh()
        while (true) { delay(20_000); now = LocalDateTime.now() }
    }
    // While the app is open: read the counter as it ticks, sort the post, fetch the weather.
    LifecycleResumeEffect(Unit) {
        now = LocalDateTime.now()
        WalkService.stop(ctx)
        val job = c.scope.launch {
            launch { runCatching { c.refreshWeather() } }
            // The counter's own first value comes as soon as it's subscribed, so no separate read to wait on.
            c.post.tick()
            if (c.sensor.allowed) c.sensor.live().conflate().collect { v -> c.post.reading(v); delay(1000) }
        }
        // Locked with the app open: a quiet foreground service keeps counting until it's open again.
        onPauseOrDispose { job.cancel(); WalkService.startIfLocked(ctx); c.write { PostWidget.updateAll(app) } }
    }
    if (!settings.onboarded) {
        Onboarding()
        return
    }
    val s = state ?: run { Box(Modifier.fillMaxSize().background(C.bg)); return }
    val env = remember(now.hour, now.minute / 5, settings, s.flags.size) { c.env(now, settings, s) }
    val home = Home(s, settings, c.content, c.game, env, now, ctx.ru)

    var tab by remember { mutableStateOf(Tab.POST) }
    val overlays = remember { mutableStateListOf<Overlay>() }
    fun push(o: Overlay) = overlays.add(o)
    fun pop() { if (overlays.isNotEmpty()) overlays.removeAt(overlays.lastIndex) }
    BackHandler(enabled = overlays.isNotEmpty() || tab != Tab.POST) { if (overlays.isNotEmpty()) pop() else tab = Tab.POST }

    // The keyboard pushes everything up, so the field being typed in stays in sight.
    Box(Modifier.fillMaxSize().background(C.bg).imePadding()) {
        Column(Modifier.fillMaxSize()) {
            Box(Modifier.weight(1f).fillMaxWidth()) {
                when (tab) {
                    Tab.POST -> PostScreen(home, onVisits = { push(Overlay.Visits) }, onLetter = { push(Overlay.Letter(it)) }, onSettings = { push(Overlay.Settings) })
                    Tab.VILLAGE -> VillageScreen(home) { push(Overlay.Resident(it)) }
                    Tab.ROOM -> RoomScreen(home)
                    Tab.ALBUM -> AlbumScreen(home)
                    Tab.DIARY -> DiaryScreen(home) { push(Overlay.Letter(it)) }
                }
            }
            if (!WindowInsets.isImeVisible) TabBar(tab, home) { tab = it }
        }
        when (val o = overlays.lastOrNull()) {
            Overlay.Visits -> VisitScreen(home, onDone = { pop() })
            is Overlay.Letter -> LetterScreen(home, o.id, onDone = { pop() })
            is Overlay.Resident -> ResidentSheet(home, o.house, onClose = { pop() })
            Overlay.Settings -> SettingsScreen(home, onBack = { pop() })
            null -> Unit
        }
    }
}

@Composable
private fun TabBar(tab: Tab, home: Home, onTab: (Tab) -> Unit) {
    val items = listOf(
        Tab.POST to R.string.tab_post, Tab.VILLAGE to R.string.tab_village, Tab.ROOM to R.string.tab_room,
        Tab.ALBUM to R.string.tab_album, Tab.DIARY to R.string.tab_diary,
    )
    Row(Modifier.fillMaxWidth().background(C.ink).navigationBarsPadding().padding(top = 2.dp)) {
        for ((t, label) in items) {
            val sel = t == tab
            Column(
                Modifier.weight(1f).clickable { onTab(t) }.background(if (sel) C.paper else C.paper2).padding(top = 6.dp, bottom = 8.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
            ) {
                TabIcon(t, sel, badge = t == Tab.POST && (home.visits.isNotEmpty() || home.desk.isNotEmpty()))
                Text(stringResource(label), style = T.Small.copy(color = if (sel) C.ink else C.muted))
            }
        }
    }
}

/** Tiny pixel icons for the tabs. */
@Composable
private fun TabIcon(t: Tab, sel: Boolean, badge: Boolean) {
    val ink = if (sel) C.ink else C.muted
    val accent = if (sel) C.red else C.faint
    Canvas(Modifier.size(24.dp).padding(2.dp)) {
        val p = size.width / 10
        fun r(x: Int, y: Int, w: Int, h: Int, col: androidx.compose.ui.graphics.Color = ink) = drawRect(col, Offset(x * p, y * p), Size(w * p, h * p))
        when (t) {
            Tab.POST -> { r(0, 2, 10, 7); r(1, 3, 8, 5, C.light); r(1, 3, 1, 1); r(2, 4, 1, 1); r(3, 5, 1, 1); r(4, 6, 2, 1); r(6, 5, 1, 1); r(7, 4, 1, 1); r(8, 3, 1, 1); r(4, 5, 2, 1, accent) }
            Tab.VILLAGE -> { r(1, 4, 1, 5); r(8, 4, 1, 5); r(1, 8, 8, 1); r(0, 4, 10, 1); r(1, 3, 8, 1); r(2, 2, 6, 1); r(3, 1, 4, 1, accent); r(4, 6, 2, 3) }
            Tab.ROOM -> { r(4, 0, 2, 3); r(2, 3, 6, 3, C.ochre); r(2, 3, 6, 1); r(4, 6, 2, 3); r(2, 9, 6, 1) }
            Tab.ALBUM -> { for (i in 0 until 5) { r(i * 2, 0, 1, 1); r(i * 2, 9, 1, 1); r(0, i * 2, 1, 1); r(9, i * 2, 1, 1) }; r(1, 1, 8, 8, accent); r(2, 2, 6, 6, C.light); r(3, 5, 4, 2, ink) }
            Tab.DIARY -> { r(1, 0, 8, 10); r(2, 1, 6, 8, C.light); r(3, 3, 4, 1); r(3, 5, 4, 1); r(3, 7, 3, 1); r(0, 1, 1, 8, accent) }
        }
        if (badge) drawRect(C.red, Offset(8 * p, -p), Size(3 * p, 3 * p))
    }
}
