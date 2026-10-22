package app.lipovka.ui.post

import android.Manifest
import android.os.Build
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.pluralStringResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.BuildConfig
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.data.St
import app.lipovka.domain.Phase
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.EveningScene
import app.lipovka.ui.art.Icons
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.art.PostOffice
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Kind as BtnKind
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.Segments
import app.lipovka.ui.components.Stat
import app.lipovka.ui.components.Tag
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.format.DateTimeFormatter
import kotlin.math.max

/** The post office: the scene, the bag and the round, the gates, and the evening with the diary. */
@Composable
fun PostScreen(home: Home, onVisits: () -> Unit, onLetter: (Long) -> Unit, onSettings: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val s = home.s
    val ru = home.ru
    val waiting = s.bag.size + home.desk.size
    val scene = remember(home.env, waiting, home.dog) { PostOffice(home.env, waiting, home.dog) }
    Column(Modifier.fillMaxSize().background(C.paper).verticalScroll(rememberScrollState())) {
        Box {
            PixelView(scene, Modifier.fillMaxWidth())
            Box(Modifier.align(Alignment.TopEnd).statusBarsPadding().padding(10.dp).pixelBox(C.light).clickable(onClick = onSettings).padding(6.dp)) {
                BufImage(Icons.gear(), scale = 2.dp)
            }
        }
        Column(Modifier.padding(horizontal = 16.dp, vertical = 12.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Header(home)
            Permissions(home)
            for (m in home.desk) DeskCard(home, m) { onLetter(m.id) }
            if (home.visits.isNotEmpty()) VisitsCard(home, onVisits)
            Round(home)
            Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                Stat(Words.num(home.stepsToday), stringResource(R.string.steps_today), Modifier.weight(1f))
                Stat(Words.km(s.total), stringResource(R.string.s_km), Modifier.weight(1f))
                Stat(delivered(home).toString(), stringResource(R.string.s_letters), Modifier.weight(1f))
            }
            Bag(home)
            val shelf = s.shelf.size
            if (shelf > 0) {
                Text(stringResource(R.string.shelf_hint, shelf), style = T.Sub)
                PixelButton(stringResource(R.string.bag_more), { c.write { post.takeMore() } }, Modifier.fillMaxWidth(), kind = BtnKind.GHOST)
            }
            NextDistrict(home)
            if (home.env.phase in setOf(Phase.DUSK, Phase.EVENING, Phase.NIGHT) || home.now.hour >= 18) Evening(home)
            if (BuildConfig.DEBUG || BuildConfig.DEMO) PixelButton(stringResource(R.string.add_steps), { c.write { post.addSteps(1000) } }, Modifier.fillMaxWidth(), kind = BtnKind.GHOST)
            Spacer(Modifier.height(8.dp))
        }
    }
}

private fun delivered(home: Home): Int {
    val start = home.now.toLocalDate().atStartOfDay(java.time.ZoneId.systemDefault()).toInstant().toEpochMilli()
    return home.s.mail.count { (it.state == St.DELIVERED || it.state == St.SEEN) && it.deliveredAt >= start }
}

@Composable
private fun Header(home: Home) {
    val locale = androidx.compose.ui.platform.LocalConfiguration.current.locales[0]
    val e = home.env
    val date = home.now.toLocalDate().format(DateTimeFormatter.ofPattern("EEEE, d MMMM", locale))
    Column {
        Text(stringResource(R.string.bag_title), style = T.Display)
        Text("$date · ${Words.sky(e.sky, home.ru)}, ${if (e.temp > 0) "+" else ""}${e.temp}°", style = T.Sub)
    }
}

@Composable
private fun Permissions(home: Home) {
    val ctx = LocalContext.current
    val c = ctx.container
    if (app.lipovka.ui.art.Art.still) return
    var allowed by remember { mutableStateOf(c.sensor.allowed) }
    val launcher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { ok -> allowed = ok; if (ok) c.write { sync() } }
    if (!c.sensor.present) {
        Panel(fill = C.paper2) { Text(stringResource(R.string.no_sensor), style = T.Sub) }
    } else if (!allowed && Build.VERSION.SDK_INT >= 29) {
        Panel(fill = C.telegram) {
            Text(stringResource(R.string.steps_permission), style = T.Body)
            Spacer(Modifier.height(8.dp))
            PixelButton(stringResource(R.string.allow), { launcher.launch(Manifest.permission.ACTIVITY_RECOGNITION) }, Modifier.fillMaxWidth())
        }
    }
}

@Composable
private fun DeskCard(home: Home, m: Mail, onOpen: () -> Unit) {
    val ctx = LocalContext.current
    val t = Words.mail(ctx, home.content, m, home.ru, home.year)
    Panel(fill = C.telegram, onClick = onOpen) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            BufImage(Icons.kind(Kind.of(m.kind)), scale = 2.dp)
            Spacer(Modifier.width(10.dp))
            Column(Modifier.weight(1f)) {
                Text(stringResource(R.string.letter_for_you), style = T.Heading.copy(color = C.redDeep))
                Text(t.from, style = T.Sub)
            }
        }
    }
}

@Composable
private fun VisitsCard(home: Home, onVisits: () -> Unit) {
    val n = home.visits.size
    val names = home.visits.mapNotNull { home.resident(it.to)?.name?.invoke(home.ru) }.distinct().joinToString(", ")
    Panel(fill = C.lamp, onClick = onVisits) {
        Text(pluralStringResource(R.plurals.visits, n, n), style = T.Heading)
        Text(names, style = T.Sub.copy(color = C.ink))
        Spacer(Modifier.height(8.dp))
        PixelButton(stringResource(R.string.visit_go), onVisits, Modifier.fillMaxWidth())
    }
}

@Composable
private fun Round(home: Home) {
    val next = home.plan.firstOrNull()
    if (next == null) {
        Panel(fill = C.paper2) { Text(stringResource(R.string.bag_empty), style = T.Body) }
        return
    }
    val walked = home.s.leg.coerceAtMost(next.leg)
    val left = max(0, next.leg - home.s.leg)
    val names = next.mail.mapNotNull { home.resident(it.to)?.name?.invoke(home.ru) }.distinct().joinToString(", ")
    Panel {
        Eyebrow(stringResource(R.string.going_to, Words.house(next.house.id, home.ru)))
        Text(names, style = T.Heading.copy(color = C.blue))
        Spacer(Modifier.height(6.dp))
        Segments(walked.toFloat() / next.leg)
        Spacer(Modifier.height(4.dp))
        Row {
            Text(stringResource(R.string.steps_walked, Words.num(walked)), style = T.Small, modifier = Modifier.weight(1f))
            Text(stringResource(R.string.steps_left, Words.num(left)), style = T.Body)
        }
    }
}

@Composable
private fun Bag(home: Home) {
    val ctx = LocalContext.current
    if (home.plan.isEmpty()) return
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        Text(pluralStringResource(R.plurals.n_bag, home.s.bag.size, home.s.bag.size), style = T.Sub)
        for (stop in home.plan) for (m in stop.mail) {
            val t = Words.mail(ctx, home.content, m, home.ru, home.year)
            val kind = Kind.of(m.kind)
            val left = max(0, stop.cum - home.s.leg)
            Panel(fill = if (kind == Kind.TELEGRAM) C.telegram else C.light, padding = androidx.compose.foundation.layout.PaddingValues(horizontal = 10.dp, vertical = 8.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    BufImage(Icons.kind(kind), scale = 2.dp)
                    Spacer(Modifier.width(10.dp))
                    Column(Modifier.weight(1f)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(t.title, style = T.Body.copy(color = if (kind == Kind.TELEGRAM) C.redDeep else C.blue))
                            if (kind == Kind.TELEGRAM) { Spacer(Modifier.width(6.dp)); Tag(stringResource(R.string.urgent)) }
                        }
                        Text("${Words.kind(ctx, kind)} · ${t.from}", style = T.Small, maxLines = 1)
                    }
                    Column(horizontalAlignment = Alignment.End) {
                        Text(Words.num(left), style = T.Heading)
                        Text(stringResource(R.string.s_steps), style = T.Small)
                    }
                }
            }
        }
    }
}

@Composable
private fun NextDistrict(home: Home) {
    val km = home.s.km
    val next = (1..5).firstOrNull { !home.s.has("d$it") }
    val text = if (next == null) stringResource(R.string.all_open) else {
        val left = World.OPENS_AT_KM[next] - km
        stringResource(R.string.next_district, Words.district(next, home.ru), String.format("%.1f", left.coerceAtLeast(.1)).replace('.', ','))
    }
    Column {
        Text(stringResource(R.string.km_total, Words.km(home.s.total)), style = T.Small)
        Text(text, style = T.Small)
    }
}

@Composable
fun Evening(home: Home) {
    val ctx = LocalContext.current
    val c = ctx.container
    val scene = remember(home.env) { EveningScene(home.env) }
    val day = home.now.toLocalDate().toEpochDay()
    val diary by c.post.diary.collectAsState(initial = emptyList())
    var text by rememberSaveable(day) { mutableStateOf("") }
    LaunchedEffect(diary, day) { if (text.isEmpty()) text = diary.firstOrNull { it.day == day }?.text.orEmpty() }
    val start = home.now.toLocalDate().atStartOfDay(java.time.ZoneId.systemDefault()).toInstant().toEpochMilli()
    val today = home.s.mail.filter { (it.state == St.SEEN || it.state == St.DELIVERED) && it.deliveredAt >= start }
    val news = today.map { Words.mail(ctx, home.content, it, home.ru, home.year).brief }.filter { it.isNotBlank() }.distinct() +
        c.events(home.now.toLocalDate(), home.s).map { it.brief(home.ru) }
    Column(Modifier.pixelBox(C.night).padding(4.dp)) {
        PixelView(scene, Modifier.fillMaxWidth())
        Column(Modifier.pixelBox(C.paper).padding(horizontal = 14.dp, vertical = 12.dp)) {
            Text(stringResource(R.string.evening_title, Words.date(ctx, day)), style = T.Title)
            Spacer(Modifier.height(8.dp))
            Eyebrow(stringResource(R.string.evening_news))
            if (news.isEmpty()) Text(stringResource(R.string.evening_none), style = T.Body)
            for (n in news.take(8)) Row(Modifier.padding(vertical = 2.dp)) {
                Box(Modifier.padding(top = 7.dp).width(6.dp).height(6.dp).background(C.ochre))
                Spacer(Modifier.width(8.dp))
                Text(n, style = T.Body)
            }
            Spacer(Modifier.height(10.dp))
            Eyebrow(stringResource(R.string.diary_title))
            BasicTextField(
                value = text, onValueChange = { text = it.take(240) },
                textStyle = T.Hand, cursorBrush = SolidColor(C.blue),
                modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp),
                decorationBox = { inner -> Box { if (text.isEmpty()) Text(stringResource(R.string.diary_hint), style = T.Hand.copy(color = C.faint)); inner() } },
            )
            PixelButton(stringResource(R.string.lamp_off), { c.write { post.diary(day, text) } }, Modifier.fillMaxWidth(), kind = BtnKind.LAMP)
        }
    }
}
