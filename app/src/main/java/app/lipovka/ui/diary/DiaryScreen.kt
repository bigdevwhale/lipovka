package app.lipovka.ui.diary

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
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
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.St
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.Icons
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.Stat
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.Instant
import java.time.ZoneId

/** The postman's notebook: every day walked, its letters and its line; and the letters to the postman. */
@Composable
fun DiaryScreen(home: Home, onLetter: (Long) -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val diary by c.post.diary.collectAsState(initial = emptyList())
    val lines = diary.associate { it.day to it.text }
    val zone = ZoneId.systemDefault()
    val byDay = home.s.mail.filter { (it.state == St.SEEN || it.state == St.DELIVERED) && it.deliveredAt > 0 }
        .groupBy { Instant.ofEpochMilli(it.deliveredAt).atZone(zone).toLocalDate().toEpochDay() }
    val days = (home.s.days.filter { it.value > 0 }.keys + lines.keys).distinct().sortedDescending()
    val toMe = home.s.mail.filter { it.to == "me" && it.state == St.SEEN }.sortedByDescending { it.day }
    Column(Modifier.fillMaxSize().background(C.paper).verticalScroll(rememberScrollState()).statusBarsPadding().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
        Text(stringResource(R.string.diary_tab), style = T.Display)
        Text(stringResource(R.string.served, home.year), style = T.Sub)
        Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
            Stat(Words.km(home.s.total), stringResource(R.string.s_km), Modifier.weight(1f))
            Stat(home.s.mail.count { it.state == St.SEEN || it.state == St.DELIVERED }.toString(), stringResource(R.string.s_letters), Modifier.weight(1f))
            Stat(home.s.days.count { it.value > 0 }.toString(), if (home.ru) "дней" else "days", Modifier.weight(1f))
        }
        if (toMe.isNotEmpty()) {
            Eyebrow(stringResource(R.string.letter_for_you))
            for (m in toMe.take(30)) {
                val t = Words.mail(ctx, home.content, m, home.ru, home.year)
                Panel(onClick = { onLetter(m.id) }) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        BufImage(Icons.kind(app.lipovka.data.Kind.of(m.kind)), scale = 2.dp)
                        Spacer(Modifier.width(10.dp))
                        Column(Modifier.weight(1f)) {
                            Text(t.from, style = T.Body.copy(color = C.blue))
                            Text(t.brief, style = T.Small)
                        }
                        Text(Words.date(ctx, m.day), style = T.Small)
                    }
                }
            }
        }
        if (days.isEmpty()) Text(stringResource(R.string.no_days), style = T.Sub)
        for (d in days) {
            val steps = home.s.days[d] ?: 0
            val letters = byDay[d].orEmpty().filter { it.to != "me" }
            Column(Modifier.fillMaxWidth().pixelBox(C.light).padding(horizontal = 12.dp, vertical = 8.dp)) {
                Row {
                    Text(Words.date(ctx, d), style = T.Heading, modifier = Modifier.weight(1f))
                    Text(stringResource(R.string.day_line, Words.num(steps), letters.size), style = T.Small)
                }
                lines[d]?.let { Text(it, style = T.Hand, modifier = Modifier.padding(top = 4.dp)) }
                val names = letters.mapNotNull { home.resident(it.to)?.name?.invoke(home.ru) }.distinct()
                if (names.isNotEmpty()) Text(names.joinToString(", "), style = T.Small, modifier = Modifier.padding(top = 2.dp))
            }
        }
        Spacer(Modifier.height(12.dp))
    }
}
