package app.lipovka.ui.album

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
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import app.lipovka.R
import app.lipovka.data.Kind
import app.lipovka.data.Stamp
import app.lipovka.data.Tx
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.StampArt
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T

private val SERIES = listOf(
    "lipovka" to Tx("Липовка", "Lipovka"), "seasons" to Tx("Времена года", "Seasons"), "holidays" to Tx("Праздники", "Holidays"),
    "post" to Tx("Почта", "The post"), "radio" to Tx("Радио", "Radio"), "far" to Tx("Дальние страны", "Far away"),
    "zarechye" to Tx("Заречье", "Zarechye"), "station" to Tx("Разъезд", "The halt"), "ozerki" to Tx("Озёрки", "Ozyorki"),
    "kordon" to Tx("Сосновый кордон", "Pine Cordon"), "gorodok" to Tx("Городок", "Gorodok"),
)

/** What the stamp came on, as it's named after "off the …". */
private val OFF = mapOf(
    Kind.LETTER to Tx("с конверта", "the envelope"), Kind.POSTCARD to Tx("с открытки", "the postcard"),
    Kind.PARCEL to Tx("с посылки", "the parcel"), Kind.TELEGRAM to Tx("с телеграммы", "the telegram"),
    Kind.REGISTERED to Tx("с заказного письма", "the registered letter"), Kind.NEWSPAPER to Tx("с газеты", "the newspaper"),
    Kind.NOTICE to Tx("с афиши", "the poster"),
)

/**
 * How the stamp came to the album, told from the first letter that brought it: who it was addressed to, and
 * how they handed the stamp over. A [he, she] pair for each Russian line, since the verbs follow the person.
 */
private val STORIES = listOf(
    Triple("%1\$s отпарил её %2\$s над чайником и отдал вам на крыльце.", "%1\$s отпарила её %2\$s над чайником и отдала вам на крыльце.",
        "%1\$s steamed it off %2\$s over the kettle and handed it to you on the porch."),
    Triple("%1\$s сам отклеил её %2\$s: «Берите, вам для альбома».", "%1\$s сама отклеила её %2\$s: «Берите, вам для альбома».",
        "%1\$s peeled it off %2\$s: “Take it, it'll be happier in an album.”"),
    Triple("%1\$s вынес её на блюдечке — вместе с пирожком.", "%1\$s вынесла её на блюдечке — вместе с пирожком.",
        "%1\$s brought it out on a saucer, with a pie beside it."),
    Triple("%1\$s долго разглядывал её на свету, а потом всё-таки подарил вам.", "%1\$s долго разглядывала её на свету, а потом всё-таки подарила вам.",
        "%1\$s held it up to the light for a long while, then gave it to you after all."),
    Triple("%1\$s аккуратно срезал её %2\$s ножницами, оставив поля.", "%1\$s аккуратно срезала её %2\$s ножницами, оставив поля.",
        "%1\$s trimmed it off %2\$s with scissors, margins and all."),
)

/** The little story of a stamp, and who the letter it came on was from; null if that letter isn't in the books. */
private fun story(ctx: android.content.Context, home: Home, st: Stamp): Pair<String, String>? {
    val m = home.s.mail.filter { it.stamp == st.key && it.deliveredAt > 0 }.minByOrNull { it.deliveredAt } ?: return null
    val t = Words.mail(ctx, home.content, m, home.ru, home.year)
    val from = t.from.takeIf { it.isNotBlank() }
    val kind = Kind.of(m.kind)
    val off = OFF[kind]?.invoke(home.ru) ?: ""
    val r = home.resident(m.to)
    val line = if (r == null) {
        // a letter to the postman: the stamp was theirs from the start
        if (home.ru) "Пришла на письме лично вам, так что просить её ни у кого не пришлось." else "It came on a letter to you, so there was no one to ask for it."
    } else {
        val (he, she, en) = STORIES[Math.floorMod(st.key.hashCode(), STORIES.size)]
        val female = r.sprite.startsWith("woman") || r.sprite == "girl"
        val pattern = if (!home.ru) en else if (female) she else he
        String.format(pattern, r.name(home.ru), off).replaceFirstChar { it.titlecase() }
    }
    val sender = from?.let { if (home.ru) "от: $it" else "from $it" }
    return line to (sender ?: "")
}

/** The stamp album: a page per series, empty frames for the stamps still to come. */
@Composable
fun AlbumScreen(home: Home) {
    val ctx = LocalContext.current
    var open by remember { mutableStateOf<Stamp?>(null) }
    val all = home.content.stamps.values.groupBy { it.series }
    val have = home.s.stamps
    // A tapped stamp is held up over the page, wherever in the album it was: no scrolling back to the top to read it.
    open?.let { st ->
        val got = have[st.key]
        Dialog(onDismissRequest = { open = null }) {
            Column(Modifier.fillMaxWidth().pixelBox(C.paper).clickable { open = null }.padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(8.dp)) {
                BufImage(StampArt.draw(st.family, st.bg, st.value), scale = 4.dp)
                Text(st.name(home.ru), style = T.Heading)
                val story = remember(st.key, home.ru) { story(ctx, home, st) }
                story?.let { Text(it.first, style = T.Body, modifier = Modifier.fillMaxWidth()) }
                if (got != null) Text(listOfNotNull(story?.second?.takeIf { it.isNotEmpty() }, stringResource(R.string.stamp_got, Words.date(ctx, got.day)),
                    if (got.count > 1) "×${got.count}" else null).joinToString(" · "), style = T.Small, modifier = Modifier.fillMaxWidth())
            }
        }
    }
    Column(Modifier.fillMaxSize().background(C.greenDeep).verticalScroll(rememberScrollState()).statusBarsPadding().padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(stringResource(R.string.album_title), style = T.Display.copy(color = C.paper))
        Text("${have.size} / ${home.content.stamps.size}", style = T.Sub.copy(color = C.lamp))
        for ((key, title) in SERIES) {
            val list = all[key].orEmpty().sortedBy { it.key }
            if (list.isEmpty()) continue
            val n = list.count { it.key in have }
            Column(Modifier.fillMaxWidth().pixelBox(C.paper2).padding(10.dp)) {
                Row { Text(title(home.ru), style = T.Heading, modifier = Modifier.weight(1f)); Text("$n / ${list.size}", style = T.Small) }
                Spacer(Modifier.height(8.dp))
                // collected first, then the empty frames
                val sorted = list.sortedBy { if (it.key in have) 0 else 1 }
                for (row in sorted.chunked(4)) {
                    Row(Modifier.fillMaxWidth().padding(vertical = 4.dp), horizontalArrangement = Arrangement.SpaceEvenly) {
                        for (st in row) {
                            val got = st.key in have
                            Box(Modifier.clickable(enabled = got) { open = st }) {
                                BufImage(StampArt.draw(st.family, st.bg, st.value, empty = !got), scale = 2.dp)
                            }
                        }
                        repeat(4 - row.size) { Spacer(Modifier.width(68.dp)) }
                    }
                }
            }
        }
        Text(stringResource(R.string.album_hint), style = T.Sub.copy(color = C.paper2))
        Spacer(Modifier.height(12.dp))
    }
}
