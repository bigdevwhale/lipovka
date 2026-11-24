package app.lipovka.ui.share

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import app.lipovka.R
import app.lipovka.ui.art.blit
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import app.lipovka.data.Mail
import app.lipovka.ui.Home
import app.lipovka.ui.components.Kind
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T

/** A small "share" link, for a corner of a screen: opens the card for [period]. */
@Composable
fun ShareLink(home: Home, period: Period, modifier: Modifier = Modifier, color: androidx.compose.ui.graphics.Color = C.blue) {
    val ctx = LocalContext.current
    var open by remember { mutableStateOf(false) }
    ShareIcon(color != C.blue, modifier) { open = true }
    if (open) SharePreview(true, period, { Cards.stats(ctx, home, it) }) { open = false }
}

/** A small "share" link for one thing: a stamp, a gift. */
@Composable
fun ShareThing(make: () -> Card?, modifier: Modifier = Modifier, color: androidx.compose.ui.graphics.Color = C.blue) {
    var open by remember { mutableStateOf(false) }
    ShareIcon(color != C.blue, modifier) { open = true }
    if (open) make()?.let { card -> SharePreview(false, Period.DAY, { card }) { open = false } }
}

/** "Share a card": the card of the stretches of days, starting with the day. */
@Composable
fun SharePeriods(home: Home, modifier: Modifier = Modifier) {
    val ctx = LocalContext.current
    var open by remember { mutableStateOf(false) }
    ShareIcon(false, modifier) { open = true }
    if (open) SharePreview(true, Period.DAY, { Cards.stats(ctx, home, it) }) { open = false }
}

/** Shares one letter as a card. */
@Composable
fun ShareLetter(home: Home, m: Mail, modifier: Modifier = Modifier) {
    val ctx = LocalContext.current
    var open by remember { mutableStateOf(false) }
    ShareIcon(false, modifier) { open = true }
    if (open) SharePreview(false, Period.DAY, { Cards.letter(ctx, home, m) }) { open = false }
}

/** The share icon (a postcard flying off), big enough to hit; [light] for dark pages. */
@Composable
fun ShareIcon(light: Boolean, modifier: Modifier = Modifier, onClick: () -> Unit) {
    val pic = remember(light) { app.lipovka.ui.art.Sprites.get(if (light) "icons/share_light" else "icons/share")?.let { s -> app.lipovka.ui.art.Buf(s.lw, s.lh, s.scale).also { b -> b.blit(s, s.lw / 2, s.lh) } } }
    val label = stringResource(R.string.share)
    Box(modifier.clickable(onClick = onClick).padding(8.dp).semantics { contentDescription = label }, contentAlignment = Alignment.Center) {
        if (pic != null) app.lipovka.ui.components.BufImage(pic, scale = 2.4.dp) else Text(label, style = T.Sub.copy(color = if (light) C.lamp else C.blue))
    }
}

/**
 * The card as it will go out, before it does: with the day, the week, the month or all the time to pick
 * from when [periods], and the buttons to share it or put it away.
 */
@Composable
private fun SharePreview(periods: Boolean, start: Period, make: (Period) -> Card, onClose: () -> Unit) {
    val ctx = LocalContext.current
    var period by remember { mutableStateOf(start) }
    val card = remember(period) { make(period) }
    val bmp = remember(card) { ShareCard.render(ctx, card) }
    Dialog(onClose, DialogProperties(usePlatformDefaultWidth = false)) {
        Column(Modifier.fillMaxWidth().padding(16.dp).pixelBox(C.paper).padding(12.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Image(bmp.asImageBitmap(), null, Modifier.fillMaxWidth().aspectRatio(ShareCard.W / ShareCard.H.toFloat()), filterQuality = FilterQuality.Medium)
            if (periods) Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                for ((p, label) in listOf(Period.DAY to R.string.share_p_day, Period.WEEK to R.string.share_p_week, Period.MONTH to R.string.share_p_month, Period.ALL to R.string.share_p_all)) {
                    // plain tabs, small enough for "Неделя" to stay on one line
                    val sel = p == period
                    Box(Modifier.weight(1f).pixelBox(if (sel) C.green else C.light).clickable { period = p }.padding(vertical = 8.dp), contentAlignment = Alignment.Center) {
                        Text(stringResource(label), style = T.Body.copy(color = if (sel) C.light else C.green), maxLines = 1, textAlign = TextAlign.Center)
                    }
                }
            }
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                PixelButton(stringResource(R.string.close), onClose, Modifier.weight(1f), kind = Kind.GHOST)
                PixelButton(stringResource(R.string.share), { ShareCard.send(ctx, bmp); onClose() }, Modifier.weight(1f))
            }
        }
    }
}
