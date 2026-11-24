package app.lipovka.ui.settings

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.container
import androidx.compose.ui.platform.LocalContext
import app.lipovka.ui.art.Postman
import app.lipovka.ui.components.BufImage
import app.lipovka.ui.components.Kind
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.theme.C

/** Who carries the post: a man or a woman, then one of three of them, shown as they'll stand at the gates. */
@Composable
fun PostmanPicker(current: String) {
    val c = LocalContext.current.container
    fun pick(look: String) = c.write { settings.update { it.copy(postman = look) } }
    val female = Postman.female(current)
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        // switching keeps the same place in the row: the second man becomes the second woman
        val at = (if (female) Postman.WOMEN else Postman.MEN).indexOf(current).coerceAtLeast(0)
        app.lipovka.ui.components.Tabs(listOf(stringResource(R.string.postman_man), stringResource(R.string.postman_woman)), if (female) 1 else 0) { k ->
            pick((if (k == 1) Postman.WOMEN else Postman.MEN)[at])
        }
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            for (look in if (female) Postman.WOMEN else Postman.MEN) {
                val pic = remember(look) { Postman.portrait(look) }
                Panel(Modifier.weight(1f), fill = if (look == current) C.telegram else C.light, onClick = { pick(look) }, padding = PaddingValues(vertical = 6.dp)) {
                    if (pic != null) BufImage(pic, Modifier.align(Alignment.CenterHorizontally), scale = 1.6.dp)
                }
            }
        }
    }
}
