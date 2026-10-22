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
import app.lipovka.R
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

/** The stamp album: a page per series, empty frames for the stamps still to come. */
@Composable
fun AlbumScreen(home: Home) {
    val ctx = LocalContext.current
    var open by remember { mutableStateOf<Stamp?>(null) }
    val all = home.content.stamps.values.groupBy { it.series }
    val have = home.s.stamps
    Column(Modifier.fillMaxSize().background(C.greenDeep).verticalScroll(rememberScrollState()).statusBarsPadding().padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(stringResource(R.string.album_title), style = T.Display.copy(color = C.paper))
        Text("${have.size} / ${home.content.stamps.size}", style = T.Sub.copy(color = C.lamp))
        open?.let { st ->
            val got = have[st.key]
            Row(Modifier.fillMaxWidth().pixelBox(C.paper).clickable { open = null }.padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
                BufImage(StampArt.draw(st.family, st.bg, st.value), scale = 3.dp)
                Column(Modifier.padding(start = 12.dp)) {
                    Text(st.name(home.ru), style = T.Heading)
                    if (got != null) Text(stringResource(R.string.stamp_got, Words.date(ctx, got.day)) + if (got.count > 1) " · ×${got.count}" else "", style = T.Small)
                }
            }
        }
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
