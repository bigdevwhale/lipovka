package app.lipovka.ui.post

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
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
import app.lipovka.ui.art.ItemArt
import app.lipovka.ui.art.StampArt
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.TopBar
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T

/** A letter addressed to the postman, read at the desk. */
@Composable
fun LetterScreen(home: Home, id: Long, onDone: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val m = home.s.mail(id)
    LaunchedEffect(m?.state) { if (m == null || (m.state != St.DESK && m.state != St.SEEN)) onDone() }
    if (m == null) return
    val t = Words.mail(ctx, home.content, m, home.ru, home.year)
    Column(Modifier.fillMaxSize().background(C.bg).clickable(remember { MutableInteractionSource() }, null) {}) {
        TopBar(stringResource(R.string.letter_for_you), onDone, dark = true)
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(horizontal = 16.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Column(Modifier.fillMaxWidth().pixelBox(C.light).padding(horizontal = 18.dp, vertical = 16.dp)) {
                Eyebrow(stringResource(R.string.letter_date, Words.date(ctx, m.day)))
                Text(t.from, style = T.Heading.copy(color = C.blue))
                Spacer(Modifier.width(1.dp))
                Text(t.news, style = T.Letter, modifier = Modifier.padding(top = 10.dp))
            }
            val gift = home.content.items[m.gift]
            if (gift != null) Row(Modifier.pixelBox(C.paper2).padding(10.dp).fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                BufImage(ItemArt.single(gift.family, gift.variant), scale = 3.dp)
                Spacer(Modifier.width(10.dp))
                Column { Text(gift.name(home.ru), style = T.Body); Text(stringResource(R.string.gift_to_room), style = T.Small) }
            }
            val stamp = home.content.stamps[m.stamp]
            if (stamp != null) Row(verticalAlignment = Alignment.CenterVertically) {
                BufImage(StampArt.draw(stamp.family, stamp.bg, stamp.value), scale = 2.dp)
                Spacer(Modifier.width(10.dp))
                Text(stamp.name(home.ru), style = T.Body.copy(color = C.light))
            }
            if (m.state == St.DESK) PixelButton(stringResource(R.string.letter_put), { c.write { post.open(m.id) } }, Modifier.fillMaxWidth())
        }
    }
}
