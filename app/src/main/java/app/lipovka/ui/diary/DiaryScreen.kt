package app.lipovka.ui.diary

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.IntrinsicSize
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.ime
import androidx.compose.foundation.relocation.BringIntoViewRequester
import androidx.compose.foundation.relocation.bringIntoViewRequester
import androidx.compose.ui.focus.onFocusChanged
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
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
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.pluralStringResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.TextRange
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.data.St
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.Icons
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.Stat
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.Instant
import java.time.LocalDate
import java.time.YearMonth
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import java.time.format.TextStyle
import java.time.temporal.WeekFields
import app.lipovka.ui.components.Kind as BtnKind

/** As long as the evening's entry may be. */
private const val DIARY_MAX = 2000

/** Room kept under the line being written: the save and cancel buttons. */
private val BUTTONS_ROOM = 72.dp

/** How many letters to the postman show before "all letters". */
private const val TO_ME_FOLDED = 3

/**
 * The postman's notebook: a month on a page, each day tinted by how far it was walked and marked if
 * something was written; a tap on a day opens it below, with its line and the log of what went to whom.
 */
@Composable
fun DiaryScreen(home: Home, onLetter: (Long) -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val diary by c.post.diary.collectAsState(initial = emptyList())
    val lines = diary.associate { it.day to it.text }
    val zone = ZoneId.systemDefault()
    val byDay = home.s.mail.filter { (it.state == St.SEEN || it.state == St.DELIVERED) && it.deliveredAt > 0 && it.to != "me" }
        .groupBy { Instant.ofEpochMilli(it.deliveredAt).atZone(zone).toLocalDate().toEpochDay() }
    val toMe = home.s.mail.filter { it.to == "me" && it.state == St.SEEN }.sortedByDescending { it.day }
    val today = home.today
    var selected by rememberSaveable { mutableStateOf(today) }
    var month by rememberSaveable { mutableStateOf(YearMonth.from(LocalDate.ofEpochDay(today)).let { it.year * 12 + it.monthValue - 1 }) }
    var allToMe by rememberSaveable { mutableStateOf(false) }

    Column(Modifier.fillMaxSize().background(C.paper).verticalScroll(rememberScrollState()).statusBarsPadding().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
        Text(stringResource(R.string.diary_tab), style = T.Display)
        Text(stringResource(R.string.served, home.year), style = T.Sub)
        Row(Modifier.height(IntrinsicSize.Min), horizontalArrangement = Arrangement.spacedBy(10.dp)) {
            Stat(Words.km(home.s.total), stringResource(R.string.s_km), Modifier.weight(1f))
            val n = home.s.mail.count { it.state == St.SEEN || it.state == St.DELIVERED }
            Stat(n.toString(), pluralStringResource(R.plurals.s_letters, n), Modifier.weight(1f))
            val walked = home.s.days.count { it.value > 0 }
            Stat(walked.toString(), pluralStringResource(R.plurals.s_days, walked), Modifier.weight(1f))
        }

        val ym = YearMonth.of(month / 12, month % 12 + 1)
        Calendar(home, ym, selected, lines.keys, byDay,
            first = YearMonth.from(LocalDate.ofEpochDay(minOf(home.s.start, home.s.days.keys.minOrNull() ?: home.s.start))),
            last = YearMonth.from(LocalDate.ofEpochDay(today)),
            onMonth = { m -> month = m.year * 12 + m.monthValue - 1 },
            onDay = { selected = it })
        Day(home, selected, lines[selected], byDay[selected].orEmpty())

        if (toMe.isNotEmpty()) {
            Spacer(Modifier.height(4.dp))
            Eyebrow(stringResource(R.string.letter_for_you))
            for (m in if (allToMe) toMe else toMe.take(TO_ME_FOLDED)) ToMe(home, m) { onLetter(m.id) }
            if (toMe.size > TO_ME_FOLDED) Text(
                if (allToMe) stringResource(R.string.diary_fold) else stringResource(R.string.diary_all_letters, toMe.size),
                style = T.Body.copy(color = C.blue), modifier = Modifier.clickable { allToMe = !allToMe }.padding(vertical = 4.dp),
            )
        }
        Spacer(Modifier.height(12.dp))
    }
}

/** How strongly a day is tinted: by the steps walked on it. */
private fun tint(steps: Int): Color = when {
    steps <= 0 -> Color.Transparent
    steps < 3000 -> C.paper2
    steps < 7000 -> C.telegram
    steps < 10000 -> C.ochre
    else -> C.ochreDeep
}

@Composable
private fun Calendar(
    home: Home, ym: YearMonth, selected: Long, written: Set<Long>, byDay: Map<Long, List<Mail>>,
    first: YearMonth, last: YearMonth, onMonth: (YearMonth) -> Unit, onDay: (Long) -> Unit,
) {
    val locale = LocalConfiguration.current.locales[0]
    val firstDow = WeekFields.of(locale).firstDayOfWeek
    val today = home.today
    Column(Modifier.fillMaxWidth().pixelBox(C.light).padding(10.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            val canBack = ym > first
            val canOn = ym < last
            Text("‹", style = T.Title.copy(color = if (canBack) C.ink else C.paper2),
                modifier = Modifier.clickable(enabled = canBack) { onMonth(ym.minusMonths(1)) }.padding(horizontal = 14.dp))
            val title = ym.atDay(1).format(DateTimeFormatter.ofPattern("LLLL yyyy", locale)).replaceFirstChar { it.titlecase(locale) }
            Text(title, style = T.Heading, textAlign = TextAlign.Center, modifier = Modifier.weight(1f))
            Text("›", style = T.Title.copy(color = if (canOn) C.ink else C.paper2),
                modifier = Modifier.clickable(enabled = canOn) { onMonth(ym.plusMonths(1)) }.padding(horizontal = 14.dp))
        }
        Row {
            for (i in 0 until 7) {
                val d = firstDow.plus(i.toLong())
                Text(d.getDisplayName(TextStyle.SHORT_STANDALONE, locale), style = T.Small, textAlign = TextAlign.Center, modifier = Modifier.weight(1f))
            }
        }
        val start = ym.atDay(1)
        val lead = (start.dayOfWeek.value - firstDow.value + 7) % 7
        val cells = (List(lead) { null } + (1..ym.lengthOfMonth()).map { start.withDayOfMonth(it) }).chunked(7)
        for (week in cells) Row(horizontalArrangement = Arrangement.spacedBy(3.dp)) {
            for (i in 0 until 7) {
                val date = week.getOrNull(i)
                Box(Modifier.weight(1f).height(44.dp)) {
                    if (date != null) {
                        val day = date.toEpochDay()
                        val steps = home.s.days[day] ?: 0
                        val future = day > today
                        val bg = tint(steps)
                        Box(
                            Modifier.fillMaxSize().background(bg)
                                .then(if (day == selected) Modifier.border(2.dp, C.blue) else if (day == today) Modifier.border(1.dp, C.muted) else Modifier)
                                .clickable(enabled = !future) { onDay(day) },
                        ) {
                            Text(date.dayOfMonth.toString(), style = T.Body.copy(color = when {
                                future -> C.paper2
                                bg == C.ochreDeep -> C.light
                                else -> C.ink
                            }), modifier = Modifier.align(Alignment.Center))
                            // a pen mark for a written day, a tiny envelope count for the letters
                            if (day in written) Box(Modifier.align(Alignment.TopEnd).padding(3.dp).size(6.dp).background(C.blue))
                            val n = byDay[day]?.size ?: 0
                            if (n > 0) Text(n.toString(), style = T.Small.copy(color = if (bg == C.ochreDeep) C.light else C.muted),
                                modifier = Modifier.align(Alignment.BottomEnd).padding(end = 3.dp))
                        }
                    }
                }
            }
        }
        // the month in one line
        val days = (1..ym.lengthOfMonth()).map { ym.atDay(it).toEpochDay() }
        val steps = days.sumOf { (home.s.days[it] ?: 0).toLong() }
        val letters = days.sumOf { byDay[it]?.size ?: 0 }
        val notes = days.count { it in written }
        Spacer(Modifier.height(2.dp))
        Text(listOf(stringResource(R.string.km_short, Words.km(steps)), pluralStringResource(R.plurals.letters_n, letters, letters),
            pluralStringResource(R.plurals.notes_n, notes, notes)).joinToString(" · "), style = T.Small)
    }
}

/** The day picked on the calendar: its line (written or to write) and the log of what went to whom. */
@Composable
private fun Day(home: Home, day: Long, line: String?, letters: List<Mail>) {
    val ctx = LocalContext.current
    val c = ctx.container
    // A day written or added to after the fact: a line remembered the next morning still has its place.
    var editing by remember(day) { mutableStateOf(false) }
    var draft by remember(day) { mutableStateOf(TextFieldValue("")) }
    val focus = remember { FocusRequester() }
    LaunchedEffect(editing) { if (editing) runCatching { focus.requestFocus() } }
    // The field doesn't follow its own cursor once the keyboard is up: keep the line being written, and the
    // buttons under it, in sight above the keyboard.
    val cursorView = remember { BringIntoViewRequester() }
    var layout by remember { mutableStateOf<TextLayoutResult?>(null) }
    var focused by remember { mutableStateOf(false) }
    val ime = WindowInsets.ime.getBottom(LocalDensity.current)
    val below = with(LocalDensity.current) { BUTTONS_ROOM.toPx() }
    LaunchedEffect(focused, ime, draft.selection, draft.text, layout) {
        val l = layout ?: return@LaunchedEffect
        if (!focused || ime == 0) return@LaunchedEffect
        val r = runCatching { l.getCursorRect(draft.selection.end.coerceIn(0, l.layoutInput.text.length)) }.getOrNull() ?: return@LaunchedEffect
        cursorView.bringIntoView(r.copy(bottom = r.bottom + below))
    }
    val steps = home.s.days[day] ?: 0
    Column(Modifier.fillMaxWidth().pixelBox(C.light).padding(horizontal = 12.dp, vertical = 8.dp)) {
        Row {
            Text(Words.date(ctx, day), style = T.Heading, modifier = Modifier.weight(1f))
            Text(stringResource(R.string.day_line, pluralStringResource(R.plurals.steps_n, Words.q(steps), Words.num(steps)), pluralStringResource(R.plurals.letters_n, letters.size, letters.size)), style = T.Small)
        }
        if (editing) {
            BasicTextField(
                value = draft,
                onValueChange = { v -> draft = if (v.text.length <= DIARY_MAX) v else v.copy(text = v.text.take(DIARY_MAX), selection = TextRange(DIARY_MAX)) },
                textStyle = T.Hand, cursorBrush = SolidColor(C.blue),
                onTextLayout = { layout = it },
                modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp).focusRequester(focus)
                    .bringIntoViewRequester(cursorView).onFocusChanged { focused = it.isFocused },
                decorationBox = { inner -> Box { if (draft.text.isEmpty()) Text(stringResource(R.string.diary_hint_past), style = T.Hand.copy(color = C.faint)); inner() } },
            )
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                PixelButton(stringResource(R.string.diary_save), {
                    val t = draft.text
                    c.write { post.diary(day, t) }
                    editing = false
                }, Modifier.weight(1f))
                PixelButton(stringResource(R.string.diary_cancel), { editing = false }, Modifier.weight(1f), kind = BtnKind.GHOST)
            }
        } else {
            if (line != null) Text(line, style = T.Hand, modifier = Modifier.padding(top = 4.dp))
            Text(stringResource(if (line == null) R.string.diary_write else R.string.diary_edit), style = T.Small.copy(color = C.blue),
                modifier = Modifier.padding(vertical = 6.dp).clickable {
                    val t = line.orEmpty()
                    draft = TextFieldValue(t, TextRange(t.length))
                    editing = true
                })
        }
        if (!editing && letters.isEmpty() && steps == 0 && line == null) Text(stringResource(R.string.day_rest), style = T.Sub)
        // the delivery log: what went to whom, in the order it was carried
        if (letters.isNotEmpty()) Column(Modifier.padding(top = 2.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            for (m in letters.sortedBy { it.deliveredAt }) {
                val t = Words.mail(ctx, home.content, m, home.ru, home.year)
                val kind = Kind.of(m.kind)
                val name = home.resident(m.to)?.name?.invoke(home.ru).orEmpty()
                // a brief that doesn't say whose letter it was gets the name in front
                val first = name.substringBefore(' ')
                val brief = t.brief.ifBlank { Words.kind(ctx, kind) }
                val text = if (name.isEmpty() || first.length >= 3 && brief.contains(first.dropLast(1))) brief else "$name · $brief"
                Row(verticalAlignment = Alignment.CenterVertically) {
                    BufImage(Icons.kind(kind), scale = 1.dp)
                    Spacer(Modifier.width(8.dp))
                    Text(text, style = T.Small)
                }
            }
        }
    }
}

@Composable
private fun ToMe(home: Home, m: Mail, onOpen: () -> Unit) {
    val ctx = LocalContext.current
    val t = Words.mail(ctx, home.content, m, home.ru, home.year)
    Panel(onClick = onOpen) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            BufImage(Icons.kind(Kind.of(m.kind)), scale = 2.dp)
            Spacer(Modifier.width(10.dp))
            Column(Modifier.weight(1f)) {
                Text(t.from, style = T.Body.copy(color = C.blue))
                Text(t.brief, style = T.Small)
            }
            Text(Words.date(ctx, m.day), style = T.Small)
        }
    }
}
