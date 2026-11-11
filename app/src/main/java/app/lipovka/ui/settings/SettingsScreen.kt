package app.lipovka.ui.settings

import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.appcompat.app.AppCompatDelegate
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
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.dp
import androidx.core.os.LocaleListCompat
import app.lipovka.R
import app.lipovka.container
import app.lipovka.domain.Place
import app.lipovka.domain.Weather
import app.lipovka.ui.Home
import app.lipovka.ui.Words
import app.lipovka.ui.components.CommunityLinks
import app.lipovka.ui.components.Eyebrow
import app.lipovka.ui.components.Kind
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.components.TopBar
import app.lipovka.ui.components.pixelBox
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import app.lipovka.work.HealthSteps
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

/**
 * A search for a town whose weather the village should share. The field starts with the town already
 * chosen, so coming back to it doesn't look as if the choice was forgotten.
 */
@Composable
fun PlacePicker(ru: Boolean, current: String = "", onPicked: (Place) -> Unit) {
    val scope = rememberCoroutineScope()
    var q by remember(current) { mutableStateOf(current) }
    var results by remember { mutableStateOf<List<Place>>(emptyList()) }
    var failed by remember { mutableStateOf(false) }
    fun search() {
        if (q.isBlank()) return
        scope.launch {
            val r = runCatching { withContext(Dispatchers.IO) { Weather.search(q, if (ru) "ru" else "en") } }
            failed = r.isFailure
            results = r.getOrDefault(emptyList())
        }
    }
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            // The field is the whole box, so a tap anywhere on it starts typing.
            BasicTextField(q, { q = it }, Modifier.weight(1f).pixelBox(C.light), textStyle = T.Body, singleLine = true, cursorBrush = SolidColor(C.ink),
                keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search), keyboardActions = KeyboardActions(onSearch = { search() }),
                decorationBox = { inner ->
                    Box(Modifier.padding(horizontal = 10.dp, vertical = 10.dp)) { if (q.isEmpty()) Text(stringResource(R.string.weather_search), style = T.Body.copy(color = C.faint)); inner() }
                })
            Spacer(Modifier.width(8.dp))
            PixelButton(stringResource(R.string.weather_find), { search() })
        }
        if (failed) Text(stringResource(R.string.weather_fail), style = T.Small.copy(color = C.red))
        for (p in results) Panel(Modifier.fillMaxWidth(), onClick = { results = emptyList(); q = p.name; onPicked(p) }, fill = C.paper2) {
            Text(p.name, style = T.Body)
            Text(p.region, style = T.Small)
        }
    }
}

/** Where the steps come from: the phone's own counter, or Health Connect. */
@Composable
private fun StepSource(health: Boolean) {
    val ctx = LocalContext.current
    val c = ctx.container
    // null while asking Health Connect whether reading is still allowed.
    var allowed by remember { mutableStateOf<Boolean?>(null) }
    LaunchedEffect(health) { allowed = c.health.allowed() }
    // Why tapping Health Connect didn't switch to it.
    var note by remember { mutableStateOf<Int?>(null) }
    fun useHealth() = c.write {
        settings.update { it.copy(healthFrom = java.time.LocalDate.now().toEpochDay()) }
        sync()
    }
    val ask = rememberLauncherForActivityResult(HealthSteps.requestContract()) { got ->
        allowed = HealthSteps.READ in got
        if (allowed == true) { note = null; useHealth() } else note = R.string.health_denied
    }
    fun pickHealth() {
        when {
            c.health.available -> ask.launch(c.health.permissions())
            c.health.installable -> { note = R.string.health_install; runCatching { ctx.startActivity(c.health.storeIntent()) } }
            else -> note = R.string.health_none
        }
    }
    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
        PixelButton(stringResource(R.string.source_phone), {
            note = null
            c.write { settings.update { it.copy(healthFrom = -1) }; sync() }
        }, Modifier.weight(1f), kind = if (!health) Kind.PRIMARY else Kind.GHOST)
        PixelButton(stringResource(R.string.source_health), { pickHealth() }, Modifier.weight(1f), kind = if (health) Kind.PRIMARY else Kind.GHOST)
    }
    val status = when {
        !health -> note ?: if (c.sensor.allowed && c.sensor.present) R.string.steps_ok else R.string.steps_off
        allowed == null -> null
        allowed == true -> R.string.health_ok
        c.health.available -> R.string.health_denied
        c.health.installable -> R.string.health_install
        else -> R.string.health_none
    }
    status?.let { Text(stringResource(it), style = T.Body) }
    if (health && allowed == false) {
        if (c.health.available) PixelButton(stringResource(R.string.health_allow), { pickHealth() }, Modifier.fillMaxWidth())
        else if (c.health.installable) PixelButton(stringResource(R.string.health_get), { pickHealth() }, Modifier.fillMaxWidth())
    }
    Text(stringResource(R.string.source_hint), style = T.Small)
}

@Composable
fun SettingsScreen(home: Home, onBack: () -> Unit) {
    val ctx = LocalContext.current
    val c = ctx.container
    val set = home.settings
    Column(Modifier.fillMaxSize().background(C.paper).clickable(remember { MutableInteractionSource() }, null) {}) {
        TopBar(stringResource(R.string.settings), onBack)
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(horizontal = 16.dp).navigationBarsPadding(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Eyebrow(stringResource(R.string.weather))
            val p = set.place
            val w = set.weather
            Text(
                if (p != null && w != null) stringResource(R.string.weather_now, p.name, Words.sky(w.sky, home.ru), Math.round(w.temp).toString())
                else if (p != null) p.name else stringResource(R.string.weather_off),
                style = T.Body,
            )
            Text(stringResource(R.string.weather_hint), style = T.Small)
            PlacePicker(home.ru, p?.name.orEmpty()) { picked -> c.write { settings.update { it.copy(place = picked, weather = null) }; refreshWeather(force = true) } }
            if (p != null) PixelButton(stringResource(R.string.weather_none), { c.write { settings.update { it.copy(place = null, weather = null) } } }, Modifier.fillMaxWidth(), kind = Kind.GHOST)

            Eyebrow(stringResource(R.string.steps_source))
            StepSource(set.healthFrom >= 0)

            Eyebrow(stringResource(R.string.notifications))
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(stringResource(R.string.notify_text), style = T.Body, modifier = Modifier.weight(1f))
                PixelButton(stringResource(if (set.notify) R.string.on else R.string.off), { c.write { settings.update { it.copy(notify = !it.notify) } } },
                    kind = if (set.notify) Kind.PRIMARY else Kind.GHOST)
            }
            if (set.notify) Row(verticalAlignment = Alignment.CenterVertically) {
                Text(stringResource(R.string.notify_delivered), style = T.Body, modifier = Modifier.weight(1f))
                PixelButton(stringResource(if (set.notifyDelivered) R.string.on else R.string.off), { c.write { settings.update { it.copy(notifyDelivered = !it.notifyDelivered) } } },
                    kind = if (set.notifyDelivered) Kind.PRIMARY else Kind.GHOST)
            }

            Eyebrow(stringResource(R.string.sounds))
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(stringResource(R.string.ambience_text), style = T.Body, modifier = Modifier.weight(1f))
                PixelButton(stringResource(if (set.ambience) R.string.on else R.string.off), { c.write { settings.update { it.copy(ambience = !it.ambience) } } },
                    kind = if (set.ambience) Kind.PRIMARY else Kind.GHOST)
            }
            Text(stringResource(R.string.ambience_hint), style = T.Small)

            Eyebrow(stringResource(R.string.language))
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                for ((tag, label) in listOf("" to stringResource(R.string.lang_system), "ru" to "Русский", "en" to "English")) {
                    val cur = AppCompatDelegate.getApplicationLocales().toLanguageTags().substringBefore('-').substringBefore(',')
                    PixelButton(label, {
                        AppCompatDelegate.setApplicationLocales(if (tag.isEmpty()) LocaleListCompat.getEmptyLocaleList() else LocaleListCompat.forLanguageTags(tag))
                    }, Modifier.weight(1f), kind = if (cur == tag) Kind.PRIMARY else Kind.GHOST)
                }
            }

            Eyebrow(stringResource(R.string.backup))
            BackupSection()

            Eyebrow(stringResource(R.string.community))
            CommunityLinks()

            Eyebrow(stringResource(R.string.about))
            Text(stringResource(R.string.credits), style = T.Small)
            Spacer(Modifier.height(16.dp))
        }
    }
}
