package app.lipovka.ui.village

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.data.Mail
import app.lipovka.data.St
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.ItemArt
import app.lipovka.ui.art.MapRound
import app.lipovka.ui.art.MapScene
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.TopBar
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import kotlin.math.hypot
import kotlin.math.roundToInt

/** What the map shows of the round right now. */
fun roundOf(home: Home): MapRound {
    val s = home.s
    val g = home.game
    val road = g.onRoad(s)
    val plan = home.plan
    val later = mutableListOf<app.lipovka.domain.Pt>()
    if (plan.size > 1) {
        var prev = plan.first().house
        later += prev.at
        for (st in plan.drop(1)) { later += World.path(prev.at, prev.district, st.house.at, st.house.district).drop(1); prev = st.house }
    }
    val ahead = if (plan.isEmpty()) emptyList() else {
        // the rest of the current leg, from the postman's spot on
        val total = road.path.zipWithNext().sumOf { (p, q) -> p.to(q) }
        var acc = 0.0
        val out = mutableListOf(road.at)
        for ((p, q) in road.path.zipWithNext()) { acc += p.to(q); if (total > 0 && acc / total > road.t) out += q }
        out
    }
    val startOfDay = home.now.toLocalDate().atStartOfDay(java.time.ZoneId.systemDefault()).toInstant().toEpochMilli()
    val visited = s.mail.filter { (it.state == St.DELIVERED || it.state == St.SEEN) && it.deliveredAt >= startOfDay }
        .mapNotNull { home.resident(it.to)?.house }.toSet()
    val pending = s.bag.mapNotNull { home.resident(it.to)?.house }.toSet()
    return MapRound(ahead, later, road.at, pending, visited - pending, walking = plan.isNotEmpty())
}

@Composable
fun VillageScreen(home: Home, onHouse: (String) -> Unit) {
    val round = roundOf(home)
    val scene = remember(home.env, home.open, round, home.dog) { MapScene(home.env, home.open, round, home.dog) }
    val scroll = rememberScrollState()
    Column(Modifier.fillMaxSize().background(C.paper)) {
        // The hint has its own strip above the map, so it never sits on a house's name.
        Text(stringResource(R.string.village_hint), style = T.Small.copy(color = C.ink, textAlign = TextAlign.Center),
            modifier = Modifier.fillMaxWidth().background(C.paper2).statusBarsPadding().padding(horizontal = 8.dp, vertical = 6.dp))
        BoxWithConstraints(Modifier.fillMaxWidth().weight(1f)) {
            val scale = maxWidth / World.W
            val density = LocalDensity.current
            LaunchedEffect(Unit) {
                // open on the postman
                val y = with(density) { (scale * round.postman.y.toFloat()).toPx() } - with(density) { maxHeight.toPx() } / 2
                scroll.scrollTo(y.roundToInt().coerceAtLeast(0))
            }
            Box(Modifier.fillMaxSize().verticalScroll(scroll)) {
                Box(Modifier.fillMaxWidth().pointerInput(home.open) {
                    detectTapGestures { o ->
                        val x = o.x / size.width * World.W
                        val y = o.y / size.width * World.W
                        val hit = World.houses.filter { it.district <= home.open }.minByOrNull { hypot(it.at.x - x, it.at.y - 8 - y) }
                        if (hit != null && hypot(hit.at.x - x, hit.at.y - 8 - y) < 22) onHouse(hit.id)
                    }
                }) {
                    PixelView(scene, Modifier.fillMaxWidth())
                    for (h in World.houses) {
                        if (h.district > home.open) continue
                        Label(Words.house(h.id, home.ru), h.at.x, h.at.y + 9, scale)
                    }
                    Label(Words.house("post", home.ru), World.POST.x, World.POST.y + 10, scale)
                    val next = (home.open + 1).takeIf { it <= 5 }
                    if (next != null) {
                        val y = when (next) { 1 -> 290.0; 2 -> 200.0; 3 -> 140.0; 4 -> 120.0; else -> 40.0 }
                        val left = (World.OPENS_AT_KM[next] - home.s.km).coerceAtLeast(.1)
                        Label("${Words.district(next, home.ru)} · " + stringResource(R.string.locked, String.format("%.0f", left)), 85.0, y, scale, dim = true)
                    }
                }
            }
        }
    }
}

@Composable
private fun Label(text: String, x: Double, y: Double, scale: Dp, dim: Boolean = false) {
    Box(Modifier.offset(scale * x.toFloat() - 50.dp, scale * y.toFloat()).width(100.dp), contentAlignment = Alignment.TopCenter) {
        Text(text, style = T.Small.copy(color = if (dim) C.muted else C.ink), maxLines = 2,
            modifier = Modifier.background(if (dim) C.paper.copy(alpha = .8f) else C.light.copy(alpha = .9f)).padding(horizontal = 3.dp))
    }
}

/** A house's people: who they are, their story so far, what they gave. */
@Composable
fun ResidentSheet(home: Home, house: String, onClose: () -> Unit) {
    val ctx = LocalContext.current
    val people = home.content.household(house)
    val letters by produceState(emptyList<Mail>(), house, home.s) {
        value = people.flatMap { r -> home.s.mail.filter { it.to == r.id && (it.state == St.SEEN || it.state == St.DELIVERED) } }.sortedByDescending { it.deliveredAt }
    }
    Column(Modifier.fillMaxSize().background(C.paper).clickable(remember { MutableInteractionSource() }, null) {}) {
        TopBar(Words.house(house, home.ru), onClose)
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(horizontal = 16.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            for (r in people) Panel {
                Text(r.name(home.ru), style = T.Heading)
                Text(r.about(home.ru), style = T.Sub)
            }
            val gifts = home.s.items.values.filter { o -> people.any { it.id == o.from } }.sortedByDescending { it.day }
            if (gifts.isNotEmpty()) {
                Eyebrow(stringResource(R.string.gifts_from))
                for (o in gifts) {
                    val it = home.content.items[o.key] ?: continue
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        BufImage(ItemArt.single(it.family, it.variant), scale = 2.dp)
                        Spacer(Modifier.width(8.dp))
                        Text(it.name(home.ru), style = T.Body, modifier = Modifier.weight(1f))
                        Text(Words.date(ctx, o.day), style = T.Small)
                    }
                }
            }
            Eyebrow(stringResource(R.string.story))
            if (letters.isEmpty()) Text(stringResource(R.string.nothing_yet), style = T.Sub)
            for (m in letters) {
                val t = Words.mail(ctx, home.content, m, home.ru, home.year)
                Column(Modifier.fillMaxWidth().pixelBox(C.light).padding(horizontal = 12.dp, vertical = 8.dp)) {
                    Text(Words.date(ctx, java.time.Instant.ofEpochMilli(m.deliveredAt).atZone(java.time.ZoneId.systemDefault()).toLocalDate().toEpochDay()), style = T.Small)
                    Text(t.brief.ifBlank { t.from }, style = T.Body)
                    if (t.news.isNotBlank()) Text(t.news, style = T.Sub)
                }
            }
            Spacer(Modifier.height(12.dp))
        }
    }
}
