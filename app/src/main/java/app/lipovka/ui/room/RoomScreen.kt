package app.lipovka.ui.room

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.pluralStringResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.Gift
import app.lipovka.ui.art.ItemArt
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.art.RoomScene
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T

/** The room above the post office and everything the village has given. */
@Composable
fun RoomScreen(home: Home) {
    val ctx = LocalContext.current
    val owned = home.s.items.values.sortedByDescending { it.day }
    val gifts = owned.mapNotNull { home.content.items[it.key] }.map { Gift(it.family, it.variant) }
    val scene = remember(home.env, gifts, home.dog) { RoomScene(home.env, gifts, home.dog) }
    Column(Modifier.fillMaxSize().background(C.paper).verticalScroll(rememberScrollState())) {
        PixelView(scene, Modifier.fillMaxWidth())
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Row(verticalAlignment = Alignment.Bottom) {
                Text(stringResource(R.string.room_title), style = T.Title, modifier = Modifier.weight(1f))
                Text(pluralStringResource(R.plurals.things, owned.size, owned.size), style = T.Small)
            }
            if (owned.isEmpty()) Text(stringResource(R.string.room_empty), style = T.Sub)
            for (o in owned) {
                val item = home.content.items[o.key] ?: continue
                val from = home.resident(o.from)?.name?.invoke(home.ru)
                    ?: home.content.beat(o.from.removePrefix("arc:"))?.from?.invoke(home.ru) ?: ""
                Row(verticalAlignment = Alignment.CenterVertically) {
                    BufImage(ItemArt.single(item.family, item.variant), scale = 2.dp)
                    Spacer(Modifier.width(10.dp))
                    Column(Modifier.weight(1f)) {
                        Text(item.name(home.ru), style = T.Body)
                        Text(stringResource(R.string.from_whom, from, Words.date(ctx, o.day)), style = T.Small)
                    }
                }
            }
            Spacer(Modifier.height(12.dp))
        }
    }
}
