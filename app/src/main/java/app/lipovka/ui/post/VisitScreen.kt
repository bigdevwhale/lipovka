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
import androidx.compose.runtime.LaunchedEffect
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
import app.lipovka.container
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.domain.World
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.art.GateScene
import app.lipovka.ui.art.ItemArt
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.art.StampArt
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Kind as BtnKind
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.Tag
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T

/**
 * The gates, one after another: the resident opens the letter and tells the news; the gift goes
 * upstairs and the stamp into the album; a reply goes in tomorrow's bag.
 */
@Composable
fun VisitScreen(home: Home, onDone: () -> Unit) {
    val m = home.visits.firstOrNull()
    LaunchedEffect(m == null) { if (m == null) onDone() }
    if (m == null) return
    Gate(home, m, total = home.visits.size, onDone = onDone)
}

@Composable
fun Gate(home: Home, m: Mail, total: Int = 1, preview: Boolean = false, onDone: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val who = home.resident(m.to)
    val house = World.house(who?.house ?: "") ?: World.houses.first()
    val scene = remember(home.env, house.id, who?.id, home.dog) { GateScene(home.env, house, who, home.dog) }
    val t = Words.mail(ctx, home.content, m, home.ru, home.year)
    val kind = Kind.of(m.kind)
    var replied by remember(m.id) { mutableStateOf(false) }
    Box(Modifier.fillMaxSize().background(C.paper).clickable(remember { MutableInteractionSource() }, null) {}) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
            PixelView(scene, Modifier.fillMaxWidth())
            Column(Modifier.padding(horizontal = 16.dp, vertical = 12.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Eyebrow(stringResource(R.string.at_gate, Words.house(house.id, home.ru)), Modifier.weight(1f))
                    if (total > 1) Text("1 / $total", style = T.Small)
                }
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Tag(Words.kind(ctx, kind), if (kind == Kind.TELEGRAM) C.red else C.green)
                    Spacer(Modifier.width(8.dp))
                    Text(t.from, style = T.Sub, maxLines = 2)
                }
                if (m.src.startsWith("evt:")) {
                    Panel(fill = C.telegram) { Text(t.news, style = T.Letter) }
                } else {
                    Text(who?.name?.invoke(home.ru) ?: "", style = T.Heading)
                    Panel { Text("«${t.news}»".let { if (home.ru) it else "“${t.news}”" }, style = T.Letter) }
                }
                val gift = home.content.items[m.gift]
                if (gift != null) Panel(fill = C.paper2) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        BufImage(ItemArt.single(gift.family, gift.variant), scale = 3.dp)
                        Spacer(Modifier.width(10.dp))
                        Column {
                            Text(gift.name(home.ru), style = T.Body)
                            Text(stringResource(R.string.gift_to_room), style = T.Small)
                        }
                    }
                }
                val stamp = home.content.stamps[m.stamp]
                if (stamp != null) Row(verticalAlignment = Alignment.CenterVertically) {
                    BufImage(StampArt.draw(stamp.family, stamp.bg, stamp.value), scale = 2.dp)
                    Spacer(Modifier.width(10.dp))
                    Column {
                        Text(stamp.name(home.ru), style = T.Body)
                        Text(stringResource(R.string.stamp_to_album), style = T.Small)
                    }
                }
                val reply = m.reply
                if (replied) {
                    Text(if (reply == "out") stringResource(R.string.reply_out) else stringResource(R.string.reply_local, home.resident(reply)?.name?.invoke(home.ru) ?: ""), style = T.Sub)
                }
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    if (reply.isNotBlank() && !replied && !preview) {
                        PixelButton(stringResource(R.string.take_reply), { replied = true }, Modifier.weight(1f))
                    } else {
                        PixelButton(stringResource(R.string.thanks), {
                            if (preview) onDone() else c.write { post.open(m.id) }
                        }, Modifier.weight(1f), kind = if (replied) BtnKind.PRIMARY else BtnKind.GHOST)
                    }
                }
                Spacer(Modifier.height(8.dp))
            }
        }
    }
}
