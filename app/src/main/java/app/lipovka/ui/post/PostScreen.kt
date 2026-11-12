package app.lipovka.ui.post

import android.Manifest
import android.os.Build
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.IntrinsicSize
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.ime
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.relocation.BringIntoViewRequester
import androidx.compose.foundation.relocation.bringIntoViewRequester
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.focus.onFocusChanged
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalFocusManager
import androidx.compose.ui.res.pluralStringResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.ui.text.TextRange
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.compose.LifecycleEventEffect
import app.lipovka.BuildConfig
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.data.St
import app.lipovka.domain.Game
import app.lipovka.domain.Phase
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.Art
import app.lipovka.ui.art.EveningScene
import app.lipovka.ui.art.TEAR_TICKS
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
import app.lipovka.work.PostWidget
import java.time.format.DateTimeFormatter
import kotlin.math.max
import kotlinx.coroutines.delay

/** The post office: the scene, the bag and the round, the gates, and the evening with the diary. */
@Composable
fun PostScreen(home: Home, onVisits: () -> Unit, onLetter: (Long) -> Unit, onSettings: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val s = home.s
    val ru = home.ru
    val waiting = s.bag.size + home.desk.size
    // The calendar on the wall shows yesterday until its sheet is torn off; the scene keeps tearing to itself,
    // so the sheet can finish falling, and only learns from the settings that it's already been torn.
    val day = home.env.date.toEpochDay()
    val torn = home.settings.calendarTorn == day
    // Tapped, the calendar's sheet is held up to read: once the torn one has fallen, or straight away.
    var sheetAsk by remember { mutableIntStateOf(0) }
    var sheetWait by remember { mutableStateOf(0L) }
    var sheetOpen by remember { mutableStateOf(false) }
    val scene = remember(home.env, waiting, home.dog) {
        PostOffice(home.env, waiting, home.dog, torn) { tore ->
            if (tore) c.write {
                settings.update { it.copy(calendarTorn = day) }
                runCatching { PostWidget.updateAll(app) }
            }
            sheetWait = if (tore) TEAR_TICKS * Art.FRAME_MS else 250L
            sheetAsk++
        }
    }
    LaunchedEffect(scene, torn) { if (torn) scene.torn = true }
    LaunchedEffect(sheetAsk) { if (sheetAsk > 0) { delay(sheetWait); sheetOpen = true } }
    if (sheetOpen) CalendarSheet(home, home.env.date) { sheetOpen = false }
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
            // Today's walk; the whole road so far is in the line under the bag.
            Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                Eyebrow(stringResource(R.string.today))
                Row(Modifier.height(IntrinsicSize.Min), horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    val n = delivered(home)
                    Stat(Words.num(home.stepsToday), pluralStringResource(R.plurals.s_steps, Words.q(home.stepsToday)), Modifier.weight(1f))
                    Stat(Words.km(home.stepsToday.toLong()), stringResource(R.string.s_km), Modifier.weight(1f))
                    Stat(n.toString(), pluralStringResource(R.plurals.s_letters, n), Modifier.weight(1f))
                }
                Before(home)
            }
            Bag(home)
            val shelf = s.shelf.size
            // One more letter per press, up to a full bag; with the shelf empty, an everyday one for a neighbour.
            if (s.bag.size < Game.BAG_MAX) {
                Text(if (shelf > 0) stringResource(R.string.shelf_hint, shelf) else stringResource(R.string.more_hint), style = T.Sub)
                PixelButton(stringResource(R.string.bag_more), { c.write { post.takeMore() } }, Modifier.fillMaxWidth(), kind = BtnKind.GHOST)
            }
            NextDistrict(home)
            if (eveningTime(home)) Evening(home)
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
    // With Health Connect the phone's own counter isn't used; its state shows in settings.
    if (home.settings.healthFrom >= 0) return
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
        if (home.game.homing(home.s)) {
            // Everything given out: the way back to the post office.
            val leg = home.game.homeLeg(home.s)
            val left = max(0, leg - home.s.leg)
            Panel(fill = C.paper2) {
                Eyebrow(stringResource(R.string.going_home))
                Text(stringResource(R.string.bag_empty), style = T.Body)
                Spacer(Modifier.height(6.dp))
                Segments(home.s.leg.coerceAtMost(leg).toFloat() / leg)
                Spacer(Modifier.height(4.dp))
                Text(pluralStringResource(R.plurals.steps_left, Words.q(left), Words.num(left)), style = T.Body, modifier = Modifier.align(Alignment.End))
            }
        } else Panel(fill = C.paper2) { Text(stringResource(R.string.bag_empty), style = T.Body) }
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
        // A gap between the two, and the steps-left line sits on the last line when the left one wraps.
        Row(horizontalArrangement = Arrangement.spacedBy(12.dp), verticalAlignment = Alignment.Bottom) {
            // A road begun on an earlier day says so, or "walked 1 134" next to 134 steps today looks like a mistake.
            val todayPart = home.stepsToday.coerceAtMost(walked)
            Text(if (walked > todayPart) stringResource(R.string.steps_walked_today, Words.num(walked), Words.num(todayPart))
                else stringResource(R.string.steps_walked, Words.num(walked)), style = T.Small, modifier = Modifier.weight(1f))
            Text(pluralStringResource(R.plurals.steps_left, Words.q(left), Words.num(left)), style = T.Body)
        }
        // The road round the whole bag: it grows with every letter taken, while the next gate stays as near.
        if (home.plan.size > 1) {
            val all = max(0, home.plan.last().cum - home.s.leg)
            Text(pluralStringResource(R.plurals.bag_left, Words.q(all), Words.num(all)), style = T.Small, modifier = Modifier.align(Alignment.End))
        }
    }
}

/** Yesterday's and the day before's steps, to set today against. */
@Composable
private fun Before(home: Home) {
    val today = home.now.toLocalDate().toEpochDay()
    val parts = listOf(1L to R.string.yesterday, 2L to R.string.day_before).mapNotNull { (back, name) ->
        val n = home.s.days[today - back] ?: return@mapNotNull null
        stringResource(name) + ": " + pluralStringResource(R.plurals.steps_n, Words.q(n), Words.num(n))
    }
    if (parts.isNotEmpty()) Text(parts.joinToString(" · "), style = T.Small)
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
                        Text(pluralStringResource(R.plurals.s_steps, Words.q(left)), style = T.Small)
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
        val letters = home.s.mail.count { (it.state == St.SEEN || it.state == St.DELIVERED) && it.to != "me" }
        Text(stringResource(R.string.km_total, Words.km(home.s.total)) + " · " + pluralStringResource(R.plurals.letters_n, letters, letters), style = T.Small)
        Text(text, style = T.Small)
    }
}

/**
 * The evening lasts from dusk (or six o'clock) until the mail day turns over in the small hours. A dark
 * winter morning before work is not an evening, even though the sun isn't up yet.
 */
private fun eveningTime(home: Home): Boolean {
    val h = home.now.hour
    val dark = home.env.phase == Phase.DUSK || home.env.phase == Phase.EVENING || home.env.phase == Phase.NIGHT
    return h >= 18 || home.now.toLocalDate() != home.game.mailDay(home.now) || (h >= 12 && dark)
}

/** How long a day's line in the diary can be: a page, not a tweet. */
private const val DIARY_MAX = 2000

/** How many lines of a written entry show while it rests folded. */
private const val DIARY_FOLDED = 3

/** How long after the last keystroke the diary entry saves itself. */
private const val DIARY_SAVE_MS = 1000L

@Composable
fun Evening(home: Home) {
    val ctx = LocalContext.current
    val c = ctx.container
    val focus = LocalFocusManager.current
    // The evening belongs to the mail day: written after midnight, the line still goes to the day just walked.
    val day = home.today
    val night = home.now.toLocalDate().toEpochDay() != day
    // The lamp is remembered: put out tonight, it stays out when you come back to the screen.
    val lit = home.settings.lampOut != day
    fun light(on: Boolean) = c.write {
        settings.update { it.copy(lampOut = if (on) -1 else day) }
        // the evening widget shows the same lamp
        runCatching { PostWidget.updateAll(app) }
    }
    val scene = remember(home.env, lit) { EveningScene(home.env, lit) }
    val diary by c.post.diary.collectAsState(initial = emptyList())
    var field by rememberSaveable(day, stateSaver = TextFieldValue.Saver) { mutableStateOf(TextFieldValue("")) }
    val text = field.text
    // Set once the person has changed the text: until then the field may still be empty only because the
    // saved entry hasn't loaded, and saving that would wipe it.
    var dirty by rememberSaveable(day) { mutableStateOf(false) }
    LaunchedEffect(diary, day) {
        if (!dirty && text.isEmpty()) diary.firstOrNull { it.day == day }?.text?.let { field = TextFieldValue(it, TextRange(it.length)) }
    }
    // The entry saves itself: a moment after typing stops, on leaving the screen, and when the app goes to
    // the background, so closing the app without putting out the lamp doesn't lose what was written.
    val latest by rememberUpdatedState(text)
    fun save() { if (dirty) { val t = latest; c.write { post.diary(day, t) } } }
    LaunchedEffect(text) { if (dirty) { delay(DIARY_SAVE_MS); save() } }
    LifecycleEventEffect(Lifecycle.Event.ON_STOP) { save() }
    DisposableEffect(day) { onDispose { save() } }
    // The field doesn't follow its own cursor once the keyboard is up, so a long entry, or one near the
    // bottom of the screen, would be typed behind the keyboard: keep the cursor's line in sight.
    val cursorView = remember { BringIntoViewRequester() }
    var layout by remember { mutableStateOf<TextLayoutResult?>(null) }
    var focused by remember { mutableStateOf(false) }
    // A written entry rests folded to a few lines, after the lamp is put out and when coming back to the
    // screen; a tap opens it for writing again.
    var editing by remember(day) { mutableStateOf(false) }
    val folded = !editing && text.isNotEmpty()
    val focusField = remember { FocusRequester() }
    LaunchedEffect(editing) { if (editing) runCatching { focusField.requestFocus() } }
    val ime = WindowInsets.ime.getBottom(LocalDensity.current)
    LaunchedEffect(focused, ime, field.selection, text, layout) {
        val l = layout ?: return@LaunchedEffect
        if (!focused || ime == 0) return@LaunchedEffect
        // The layout can still be the previous text's for a moment (a word from the keyboard's suggestions
        // lands all at once): asking it about an offset past its own text throws, so stay within what it laid out.
        val r = runCatching { l.getCursorRect(field.selection.end.coerceIn(0, l.layoutInput.text.length)) }.getOrNull()
            ?: return@LaunchedEffect
        // a little room below the line, so it doesn't sit flush on the keyboard
        cursorView.bringIntoView(r.copy(bottom = r.bottom + r.height))
    }
    val date = java.time.LocalDate.ofEpochDay(day)
    val start = date.atStartOfDay(java.time.ZoneId.systemDefault()).toInstant().toEpochMilli()
    val today = home.s.mail.filter { (it.state == St.SEEN || it.state == St.DELIVERED) && it.deliveredAt >= start }
    val news = today.map { Words.mail(ctx, home.content, it, home.ru, home.year).brief }.filter { it.isNotBlank() }.distinct() +
        c.events(date, home.s).map { it.brief(home.ru) }
    Column(Modifier.pixelBox(C.night).padding(4.dp)) {
        PixelView(scene, Modifier.fillMaxWidth())
        Column(Modifier.pixelBox(C.paper).padding(horizontal = 14.dp, vertical = 12.dp)) {
            // After midnight it's no longer an evening but the night: "the night before the 8th".
            Text(if (night) stringResource(R.string.night_title, Words.date(ctx, day + 1))
                else stringResource(R.string.evening_title, Words.date(ctx, day)), style = T.Title)
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
            if (folded) Text(text, style = T.Hand, maxLines = DIARY_FOLDED, overflow = TextOverflow.Ellipsis,
                modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp).clickable {
                    field = field.copy(selection = TextRange(text.length))
                    editing = true
                })
            else BasicTextField(
                value = field,
                onValueChange = { v ->
                    val typed = v.text != text
                    if (typed) dirty = true
                    field = if (v.text.length <= DIARY_MAX) v else v.copy(text = v.text.take(DIARY_MAX), selection = TextRange(DIARY_MAX))
                    if (typed && !lit) light(true)
                },
                textStyle = T.Hand, cursorBrush = SolidColor(C.blue),
                onTextLayout = { layout = it },
                modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp).focusRequester(focusField).bringIntoViewRequester(cursorView).onFocusChanged { focused = it.isFocused },
                decorationBox = { inner -> Box { if (text.isEmpty()) Text(stringResource(R.string.diary_hint), style = T.Hand.copy(color = C.faint)); inner() } },
            )
            // Putting the lamp out writes the line down and ends the evening; lighting it again lets you go on.
            PixelButton(stringResource(if (lit) R.string.lamp_off else R.string.lamp_on), {
                if (lit) { focus.clearFocus(); editing = false; c.write { post.diary(day, text) } }
                light(!lit)
            }, Modifier.fillMaxWidth(), kind = if (lit) BtnKind.LAMP else BtnKind.GHOST)
        }
    }
}
