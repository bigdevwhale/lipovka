package app.lipovka.ui.onboarding

import android.Manifest
import android.os.Build
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Settings
import app.lipovka.ru
import app.lipovka.ui.art.GateScene
import app.lipovka.ui.art.PixelView
import app.lipovka.ui.art.PostOffice
import app.lipovka.ui.components.Kind
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.settings.PlacePicker
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import java.time.LocalDateTime

/** Four short pages: the appointment, the steps, the weather, the notifications. */
@Composable
fun Onboarding(startPage: Int = 0) {
    val ctx = LocalContext.current
    val c = ctx.container
    var page by rememberSaveable { mutableIntStateOf(startPage) }
    var picked by remember { mutableStateOf<String?>(null) }
    val env = remember { c.env(LocalDateTime.now(), Settings(), null) }
    val stepsPerm = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { page = 2 }
    val notifyPerm = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { finish(c) }
    Column(Modifier.fillMaxSize().background(C.paper).verticalScroll(rememberScrollState())) {
        val scene = remember(page) {
            when (page) {
                0 -> PostOffice(env, 4, false)
                1 -> PostOffice(env, 6, false)
                2 -> GateScene(env, app.lipovka.domain.World.house("vetrovy")!!, c.content.resident("anna"), false)
                else -> PostOffice(env.copy(minute = 21 * 60, phase = app.lipovka.domain.Phase.EVENING), 0, false)
            }
        }
        PixelView(scene, Modifier.fillMaxWidth())
        Column(Modifier.padding(horizontal = 18.dp, vertical = 16.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            when (page) {
                0 -> {
                    Text(stringResource(R.string.ob_title), style = T.Display)
                    Text(stringResource(R.string.ob_text), style = T.Letter)
                    PixelButton(stringResource(R.string.next), { page = 1 }, Modifier.fillMaxWidth())
                }
                1 -> {
                    Text(stringResource(R.string.ob_steps_title), style = T.Title)
                    Text(stringResource(R.string.ob_steps_text), style = T.Letter)
                    PixelButton(stringResource(R.string.allow), {
                        if (Build.VERSION.SDK_INT >= 29) stepsPerm.launch(Manifest.permission.ACTIVITY_RECOGNITION) else page = 2
                    }, Modifier.fillMaxWidth())
                }
                2 -> {
                    Text(stringResource(R.string.ob_weather_title), style = T.Title)
                    Text(stringResource(R.string.ob_weather_text), style = T.Letter)
                    picked?.let { Text("✓ $it", style = T.Heading.copy(color = C.green)) }
                    PlacePicker(ctx.ru) { p -> picked = p.name; c.write { settings.update { it.copy(place = p) }; refreshWeather(force = true) } }
                    PixelButton(stringResource(if (picked != null) R.string.next else R.string.skip), { page = 3 }, Modifier.fillMaxWidth(), kind = if (picked != null) Kind.PRIMARY else Kind.GHOST)
                }
                else -> {
                    Text(stringResource(R.string.ob_notify_title), style = T.Title)
                    Text(stringResource(R.string.ob_notify_text), style = T.Letter)
                    PixelButton(stringResource(R.string.ob_start), {
                        if (Build.VERSION.SDK_INT >= 33) notifyPerm.launch(Manifest.permission.POST_NOTIFICATIONS) else finish(c)
                    }, Modifier.fillMaxWidth(), kind = Kind.LAMP)
                }
            }
            Spacer(Modifier.height(8.dp))
        }
    }
}

private fun finish(c: app.lipovka.AppContainer) = c.write {
    settings.update { it.copy(onboarded = true) }
    sync()
}
