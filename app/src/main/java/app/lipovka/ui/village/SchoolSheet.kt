package app.lipovka.ui.village

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.data.Event
import app.lipovka.domain.Cal
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.Tag
import app.lipovka.ui.components.TopBar
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

/** The village events the school takes part in, in the order of a school year. */
private val SCHOOL_EVENTS = listOf("knowledge_day", "subbotnik", "swallows", "last_bell", "starfall")

/** The retired teacher who taught at the school. */
private const val TEACHER = "teacher"

/** What the school is doing at this moment: an event, the holidays, lessons, or nothing. */
private fun schoolNow(now: LocalDateTime, events: List<Event>, ru: Boolean, str: (Int) -> String): String {
    val date = now.toLocalDate()
    events.firstOrNull { Cal.within(date, it.start, it.end) }?.let { return it.brief(ru) }
    val md = date.monthValue * 100 + date.dayOfMonth
    return str(when {
        date.monthValue in 6..8 -> R.string.school_holidays
        md >= 1230 || md <= 108 -> R.string.school_winter_break
        date.dayOfWeek == DayOfWeek.SUNDAY -> R.string.school_sunday
        now.hour in 8..13 -> R.string.school_lessons
        now.hour in 14..17 -> R.string.school_after
        else -> R.string.school_night
    })
}

/** "1 September", or "24–25 May" for an event that lasts a few days. */
private fun span(e: Event, year: Int, fmt: DateTimeFormatter): String {
    val s = Cal.resolve(e.start, year) ?: return ""
    val end = Cal.resolve(e.end, year) ?: s
    return if (end == s) s.format(fmt) else "${s.format(fmt)} – ${end.format(fmt)}"
}

/** The school: no one lives there, so instead of letters it shows what is going on, its pupils and its year. */
@Composable
fun SchoolSheet(home: Home, onHouse: (String) -> Unit, onClose: () -> Unit) {
    val ctx = LocalContext.current
    val events = SCHOOL_EVENTS.mapNotNull { home.content.eventByKey[it] }
    val now = schoolNow(home.now, events, home.ru, ctx::getString)
    val pupils = home.content.residents.filter { it.child && it.district <= home.open }
    val teacher = home.resident(TEACHER)
    val today: LocalDate = home.now.toLocalDate()
    val fmt = DateTimeFormatter.ofPattern("d MMMM", LocalConfiguration.current.locales[0])
    Column(Modifier.fillMaxSize().background(C.paper).clickable(remember { MutableInteractionSource() }, null) {}) {
        TopBar(Words.house(World.SCHOOL_ID, home.ru), onClose)
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(horizontal = 16.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Panel { Text(stringResource(R.string.school_about), style = T.Body) }

            Eyebrow(stringResource(R.string.school_today))
            Text(now, style = T.Body)

            if (pupils.isNotEmpty()) {
                Eyebrow(stringResource(R.string.school_pupils))
                for (r in pupils) Panel(Modifier.fillMaxWidth(), onClick = { onHouse(r.house) }) {
                    Text(r.name(home.ru), style = T.Heading)
                    Text(r.about(home.ru), style = T.Sub)
                    Text(Words.house(r.house, home.ru), style = T.Small)
                }
            }
            if (teacher != null) {
                Eyebrow(stringResource(R.string.school_teacher))
                Panel(Modifier.fillMaxWidth(), onClick = { onHouse(teacher.house) }) {
                    Text(teacher.name(home.ru), style = T.Heading)
                    Text(teacher.about(home.ru), style = T.Sub)
                }
            }

            Eyebrow(stringResource(R.string.school_year))
            for (e in events) {
                val on = Cal.within(today, e.start, e.end)
                Panel(Modifier.fillMaxWidth(), fill = if (on) C.paper2 else C.light) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(e.name(home.ru), style = T.Body, modifier = Modifier.weight(1f))
                        if (on) { Tag(stringResource(R.string.school_now)); Spacer(Modifier.width(6.dp)) }
                        Text(span(e, today.year, fmt), style = T.Small)
                    }
                    Text(e.notice(home.ru), style = T.Sub)
                }
            }
            Spacer(Modifier.height(12.dp))
        }
    }
}
