package app.lipovka.ui.art

import android.graphics.Bitmap
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.gestures.awaitEachGesture
import androidx.compose.foundation.gestures.awaitFirstDown
import androidx.compose.foundation.gestures.waitForUpOrCancellation
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.runtime.withFrameMillis
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import app.lipovka.ui.Purr
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlin.math.roundToInt
import kotlin.math.sin

/** Global switches for the art. */
object Art {
    /** Screenshots and renders want a still frame: no loop, a fixed moment. */
    @Volatile var still = false

    /** Art pixels advance about this often. */
    const val FRAME_MS = 110L
}

/**
 * A picture painted into a [Buf]: [base] once (cached while [key] stays the same), then [anim] on
 * top for every frame with a growing tick.
 */
abstract class Scene(val w: Int, val h: Int) {
    abstract val key: Any
    abstract fun base(b: Buf)
    open fun anim(b: Buf, t: Int) = Unit

    /** Where the cat was last drawn (its 48×28 sprite), or -1 while this scene has no cat. */
    private var catX = -1
    private var catY = -1

    /** The tick the cat purrs until, after being stroked. */
    @Volatile var purrUntil = 0

    /** Is ([x], [y]) in scene pixels on the cat? */
    fun onCat(x: Int, y: Int) = catX >= 0 && x in catX + 1..catX + 46 && y in catY + 3..catY + 27

    /** The sleeping cat, which breathes quick and deep while it purrs. */
    protected fun cat(b: Buf, x: Int, y: Int, t: Int) {
        catX = x; catY = y
        val left = purrUntil - t
        val purring = left > 0
        // the head comes up a pixel a tick, stays up while it purrs, and settles back down at the end
        val lift = if (purring) minOf(PURR_TICKS - left + 1, left, HEAD_LIFT) else 0
        Props.cat(b, x, y, if (purring) (sin(t * .75) + 1) / 2 else (sin(t * .18) + 1) / 2, lift = lift)
    }

    /** Little hearts rising from the cat while it purrs; drawn last, so nothing covers them. */
    protected fun purrHearts(b: Buf, t: Int) {
        if (catX < 0 || t >= purrUntil) return
        val left = purrUntil - t
        for (i in 0 until 5) {
            val age = (PURR_TICKS - left - i * 7).takeIf { it in 0 until 18 } ?: continue
            val hx = catX + 8 + i % 3 * 6 + (sin((t + i * 3) * .5) * 1.5).roundToInt()
            val hy = catY - 2 - age
            val a = (1f - age / 18f).coerceIn(0f, 1f)
            for ((u, v) in HEART) b.p(hx + u, hy + v, rgb(0xe0607a), a)
        }
    }

    /** A single finished frame, for widgets and renders. */
    fun frame(t: Int = 7): Buf {
        val b = Buf(w, h)
        base(b)
        anim(b, t)
        return b
    }
}

/** How long a stroke keeps the cat purring, in art ticks (about the length of the sound). */
const val PURR_TICKS = 37

/** How many pixels the cat raises its head when stroked. */
private const val HEAD_LIFT = 3

private val HEART = listOf(0 to 0, 2 to 0, 0 to 1, 1 to 1, 2 to 1, 1 to 2)

fun Buf.toBitmap(): Bitmap = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888).also { it.setPixels(d, 0, w, 0, 0, w, h) }

/** Shows a scene scaled up with hard pixels, animating while on screen. Width fills, height follows. */
@Composable
fun PixelView(scene: Scene, modifier: Modifier = Modifier) {
    val base = remember(scene.key, scene.w, scene.h) { Buf(scene.w, scene.h).also { scene.base(it) } }
    val frame = remember(scene.w, scene.h) { Buf(scene.w, scene.h) }
    val bitmap = remember(scene.w, scene.h) { Bitmap.createBitmap(scene.w, scene.h, Bitmap.Config.ARGB_8888) }
    val image = remember(bitmap) { bitmap.asImageBitmap() }
    var tick by remember { mutableIntStateOf(if (Art.still) 7 else 0) }
    if (!Art.still) {
        LaunchedEffect(scene.key) {
            var last = 0L
            while (true) {
                withFrameMillis { ms ->
                    if (ms - last >= Art.FRAME_MS) { last = ms; tick++ }
                }
            }
        }
    }
    val ctx = LocalContext.current
    // A tap on the cat strokes it; any other tap passes on to whatever the picture sits in.
    val stroke = Modifier.pointerInput(scene) {
        awaitEachGesture {
            val down = awaitFirstDown(requireUnconsumed = false)
            val k = scene.w / size.width.toFloat()
            if (!scene.onCat((down.position.x * k).toInt(), (down.position.y * k).toInt())) return@awaitEachGesture
            val up = waitForUpOrCancellation() ?: return@awaitEachGesture
            up.consume()
            if (tick >= scene.purrUntil) {
                scene.purrUntil = tick + PURR_TICKS
                Purr.play(ctx)
            }
        }
    }
    Canvas(modifier.aspectRatio(scene.w.toFloat() / scene.h).then(stroke)) {
        val t = tick
        frame.copyFrom(base)
        scene.anim(frame, t)
        bitmap.setPixels(frame.d, 0, frame.w, 0, 0, frame.w, frame.h)
        val scale = size.width / scene.w
        drawImage(image, srcOffset = IntOffset.Zero, srcSize = IntSize(scene.w, scene.h),
            dstOffset = IntOffset.Zero, dstSize = IntSize(size.width.roundToInt(), (scene.h * scale).roundToInt()), filterQuality = FilterQuality.None)
    }
}
