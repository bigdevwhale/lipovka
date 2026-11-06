package app.lipovka.ui.post

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
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
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import app.lipovka.R
import app.lipovka.container
import app.lipovka.domain.Sun
import app.lipovka.domain.SunTimes
import app.lipovka.ui.Home
import app.lipovka.ui.art.Air
import app.lipovka.ui.art.Buf
import app.lipovka.ui.art.CalendarScene
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.art.disc
import app.lipovka.ui.art.glow
import app.lipovka.ui.art.rgb
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.Tag
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.format.DateTimeFormatter

/**
 * Today's sheet of the post office's tear-off calendar, read standing at the wall: the calendar close up, then
 * what the sheet says. The folk sign is told like a neighbour's news at the gate; the sun, the moon and the name
 * days sit in their own little boxes; the hint or recipe from the back is last, on newsprint.
 */
@Composable
fun CalendarSheet(home: Home, date: LocalDate, onClose: () -> Unit) {
    Dialog(onDismissRequest = onClose, properties = DialogProperties(usePlatformDefaultWidth = false, decorFitsSystemWindows = false)) {
        Sheet(home, date, onClose)
    }
}

@Composable
private fun Sheet(home: Home, date: LocalDate, onClose: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val ru = home.ru
    val locale = LocalConfiguration.current.locales[0]
    val scene = remember(home.env.phase, home.env.sky, date) { CalendarScene(home.env, date) }
    val sheet = remember(date) { home.content.sheet(date) }
    val p = home.settings.place
    fun sun(d: LocalDate): SunTimes = p?.let { Sun.times(d, it.lat, it.lon) } ?: Sun.fallback(d)
    val today = sun(date)
    val yesterday = sun(date.minusDays(1))
    val length = today.set - today.rise
    val delta = length - (yesterday.set - yesterday.rise)
    val holidays = c.events(date, home.s).map { it.name(ru) }
    val phase = ((Air.moonAge(date) / 29.530588 * 8 + .5).toInt()) % 8
    val red = date.dayOfWeek == DayOfWeek.SATURDAY || date.dayOfWeek == DayOfWeek.SUNDAY
    val weekday = date.format(DateTimeFormatter.ofPattern("EEEE", locale)).replaceFirstChar { it.titlecase(locale) }
    val day = date.format(DateTimeFormatter.ofPattern(if (ru) "d MMMM" else "MMMM d", locale))

    Box(Modifier.fillMaxSize().background(C.paper).clickable(remember { MutableInteractionSource() }, null) {}) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
            PixelView(scene, Modifier.fillMaxWidth())
            Column(Modifier.padding(horizontal = 16.dp, vertical = 12.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Eyebrow(stringResource(R.string.cal_title))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(day, style = T.Title, modifier = Modifier.weight(1f))
                    Tag(weekday, if (red) C.red else C.green)
                }
                for (h in holidays) Text(h, style = T.Heading.copy(color = C.redDeep))
                // the day's sign (or the month's saying), told like the news at a gate
                sheet.sign?.let { s ->
                    if (s.kind == "sign" && s.title(ru).isNotBlank()) Text(s.title(ru), style = T.Heading.copy(color = C.blue))
                    else Eyebrow(stringResource(R.string.cal_saying))
                    Panel(Modifier.fillMaxWidth()) { Text(if (ru) "«${s.text(ru)}»" else "“${s.text(ru)}”", style = T.Letter) }
                }
                Panel(Modifier.fillMaxWidth(), fill = C.paper2) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        BufImage(remember { sunIcon() }, scale = 3.dp)
                        Spacer(Modifier.width(10.dp))
                        Column {
                            Text(stringResource(R.string.cal_sun, clock(today.rise), clock(today.set)), style = T.Body)
                            Text(stringResource(R.string.cal_day, length / 60, length % 60) + " · " +
                                stringResource(R.string.cal_delta, (if (delta > 0) "+" else if (delta < 0) "−" else "±") + kotlin.math.abs(delta)), style = T.Small)
                        }
                    }
                    Spacer(Modifier.height(8.dp))
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        BufImage(remember(date) { moonIcon(date) }, scale = 3.dp)
                        Spacer(Modifier.width(10.dp))
                        Text(stringResource(MOON[phase]), style = T.Body)
                    }
                }
                if (ru && sheet.names.isNotEmpty()) Panel(Modifier.fillMaxWidth(), fill = C.paper2) {
                    Eyebrow(stringResource(R.string.cal_names))
                    Text(sheet.names.joinToString(", "), style = T.Body)
                }
                // the back of the sheet, the way it's read with the morning tea
                sheet.tip?.let { t ->
                    Panel(Modifier.fillMaxWidth(), fill = C.light) {
                        Eyebrow(stringResource(R.string.cal_back))
                        Text(t.title(ru), style = T.Heading.copy(color = C.blue))
                        Spacer(Modifier.height(4.dp))
                        Text(t.text(ru), style = T.Letter)
                    }
                }
                PixelButton(stringResource(R.string.cal_close), onClose, Modifier.fillMaxWidth())
                Spacer(Modifier.height(8.dp))
            }
        }
    }
}

private fun clock(minute: Int) = "%d:%02d".format(minute / 60, minute % 60)

/** A little sun with its rays, the size of an item icon. */
private fun sunIcon(): Buf = Buf(15, 15).also { b ->
    b.glow(7, 7, 7, rgb(0xfff0b0), .5f, 3)
    for ((x, y) in listOf(7 to 0, 7 to 14, 0 to 7, 14 to 7, 2 to 2, 12 to 2, 2 to 12, 12 to 12)) b.p(x, y, rgb(0xd9973a))
    for ((x, y) in listOf(7 to 1, 7 to 13, 1 to 7, 13 to 7)) b.p(x, y, rgb(0xe8bf58))
    b.disc(7, 7, 4, rgb(0xd9973a)); b.disc(7, 7, 3, rgb(0xf4cc5a)); b.p(6, 5, rgb(0xfff4c0)); b.p(5, 6, rgb(0xfff4c0))
}

/** The moon in [date]'s phase, in a scrap of night sky. */
private fun moonIcon(date: LocalDate): Buf = Buf(15, 15).also { b ->
    b.r(1, 1, 13, 13, rgb(0x151d34))
    b.p(3, 3, rgb(0xc8d0e8)); b.p(11, 11, rgb(0x8890a8)); b.p(12, 3, rgb(0x8890a8))
    Air.moon(b, 7, 7, 4, date, rgb(0x151d34))
}

private val MOON = intArrayOf(
    R.string.moon_new, R.string.moon_waxing_crescent, R.string.moon_first_quarter, R.string.moon_waxing_gibbous,
    R.string.moon_full, R.string.moon_waning_gibbous, R.string.moon_last_quarter, R.string.moon_waning_crescent,
)
