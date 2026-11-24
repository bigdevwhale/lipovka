package app.lipovka.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.Immutable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp
import app.lipovka.R

/** The colours of the post office: parchment, ink, the green of the kettle, the red of sealing wax. */
@Immutable
object C {
    val bg = Color(0xFF2A1A12)
    val paper = Color(0xFFF2E2BB)
    val paper2 = Color(0xFFE1CB9B)
    val light = Color(0xFFFBF3DC)
    val ink = Color(0xFF22160F)
    val muted = Color(0xFF7A5A3E)
    val faint = Color(0xFFA88A68)
    val green = Color(0xFF3D5E43)
    val greenDeep = Color(0xFF1B2B22)
    val greenLight = Color(0xFF5A7F4F)
    val red = Color(0xFFA33A2C)
    val redDeep = Color(0xFF6E1F1F)
    val ochre = Color(0xFFD9973A)
    val ochreDeep = Color(0xFFA86E22)
    val lamp = Color(0xFFF4CC5A)
    val lampDeep = Color(0xFFB87A1A)
    val blue = Color(0xFF26375E)
    val telegram = Color(0xFFF6DC84)
    val night = Color(0xFF151D34)
}

/**
 * Every text in the app: m6x11 by Daniel Linssen with Cyrillic by Natto Games (free with attribution),
 * the font Hearthspell uses. One family; sizes set the hierarchy.
 */
val Pixel = FontFamily(Font(R.font.m6x11, FontWeight.Normal))

/**
 * The text styles. m6x11 is drawn on a grid of 16 font units to the em, so it is only crisp when a font pixel
 * is a whole number of screen pixels: every size here is snapped to the nearest multiple of 16 px on this
 * screen (and the line heights to whole font pixels), or strokes come out one and two pixels thick by turns.
 */
object T {
    /** Screen pixels to an sp, with the person's own text size. */
    private val spPx: Float = android.content.res.Resources.getSystem().let { r -> r.displayMetrics.density * r.configuration.fontScale }.coerceAtLeast(.5f)

    /** The crisp size nearest to [sp]: a whole number of screen pixels per font pixel. */
    private fun crisp(sp: Float): Int = kotlin.math.max(1, kotlin.math.round(sp * spPx / 16f).toInt())

    /** A text style at the crisp size nearest [sp], its lines [lead] font pixels apart beyond the 16 of the font. */
    private fun style(sp: Float, lead: Int, color: androidx.compose.ui.graphics.Color = androidx.compose.ui.graphics.Color.Unspecified, spacing: Float = 0f): TextStyle {
        val k = crisp(sp)
        return TextStyle(fontFamily = Pixel, fontSize = (16 * k / spPx).sp, lineHeight = ((16 + lead) * k / spPx).sp, color = color, letterSpacing = spacing.em)
    }

    val Display = style(27f, 0, C.ink)
    val Title = style(23f, 1, C.ink)
    val Heading = style(23f, 1, C.ink)
    val Eyebrow = style(16f, 1, C.muted, .04f)
    val Body = style(20f, 2, C.ink)
    val Letter = style(21f, 4, C.ink)
    val Sub = style(18f, 1, C.muted)
    val Small = style(16f, 1, C.muted)

    /** For the names on the map: the smallest crisp size, two screen pixels to a font pixel on most phones. */
    val Tiny = style(12f, 1, C.ink)
    val Number = style(28f, 0, C.ink)
    val Button = style(19f, 0)
    val Hand = style(21f, 2, C.blue)
}

@Composable
fun LipovkaTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = lightColorScheme(
            primary = C.green, onPrimary = C.light, background = C.paper, surface = C.paper, onSurface = C.ink,
            onBackground = C.ink, surfaceContainer = C.paper, surfaceContainerHigh = C.paper, surfaceContainerHighest = C.paper2,
            outline = C.ink, error = C.red,
        ),
        typography = MaterialTheme.typography.copy(bodyLarge = T.Body, bodyMedium = T.Body, bodySmall = T.Small, labelLarge = T.Button, titleLarge = T.Title),
        content = content,
    )
}
