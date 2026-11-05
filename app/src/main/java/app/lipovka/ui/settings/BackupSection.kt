package app.lipovka.ui.settings

import android.net.Uri
import android.util.Log
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import app.lipovka.R
import app.lipovka.container
import app.lipovka.data.Backup
import app.lipovka.ui.components.Kind
import app.lipovka.ui.components.Panel
import app.lipovka.ui.components.PixelButton
import app.lipovka.ui.theme.C
import app.lipovka.ui.theme.T
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import java.time.LocalDate

/**
 * Saving the post office to a file and restoring it from one. With [save] off (the first onboarding page,
 * where there is nothing to save or lose yet) only restoring shows, and it doesn't ask before replacing.
 */
@Composable
fun BackupSection(save: Boolean = true) {
    val c = LocalContext.current.container
    // A string resource saying how the last save or restore went.
    var note by remember { mutableStateOf<Int?>(null) }
    var failed by remember { mutableStateOf(false) }
    // A file picked for restoring, waiting for the "replace" confirmation.
    var pending by remember { mutableStateOf<Uri?>(null) }

    // The work runs in the app's scope, so leaving the screen (or onboarding ending on success) doesn't cut it short.
    fun run(ok: Int, work: suspend () -> Unit) = c.scope.launch(Dispatchers.Main) {
        val r = runCatching { work() }
        r.exceptionOrNull()?.let { Log.w("Backup", "failed", it) }
        failed = r.isFailure
        note = if (r.isSuccess) ok else R.string.backup_failed
    }

    val create = rememberLauncherForActivityResult(ActivityResultContracts.CreateDocument(Backup.mime())) { uri ->
        if (uri != null) run(R.string.backup_saved) { c.backupTo(uri) }
    }
    val open = rememberLauncherForActivityResult(ActivityResultContracts.OpenDocument()) { uri ->
        if (uri == null) return@rememberLauncherForActivityResult
        if (save) pending = uri else run(R.string.backup_restored) { c.restoreFrom(uri) }
    }

    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        if (save) {
            Text(stringResource(R.string.backup_text), style = T.Small)
            PixelButton(stringResource(R.string.backup_save), { note = null; create.launch(Backup.fileName(LocalDate.now())) }, Modifier.fillMaxWidth())
        }
        // Backups are JSON, but file managers and chats often hand them over as plain or unknown files.
        PixelButton(stringResource(R.string.backup_restore), { note = null; open.launch(arrayOf("application/json", "text/plain", "application/octet-stream")) },
            Modifier.fillMaxWidth(), kind = Kind.GHOST)
        pending?.let { uri ->
            Panel(Modifier.fillMaxWidth(), fill = C.paper2) {
                Text(stringResource(R.string.backup_confirm), style = T.Body)
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    PixelButton(stringResource(R.string.backup_cancel), { pending = null }, Modifier.weight(1f), kind = Kind.GHOST)
                    PixelButton(stringResource(R.string.backup_yes), { pending = null; run(R.string.backup_restored) { c.restoreFrom(uri) } }, Modifier.weight(1f))
                }
            }
        }
        note?.let { Text(stringResource(it), style = T.Body.copy(color = if (failed) C.red else C.green)) }
    }
}
