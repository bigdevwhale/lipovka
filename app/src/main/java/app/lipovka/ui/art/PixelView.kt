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
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import app.lipovka.ui.Toys
import java.time.LocalTime
import java.util.EnumMap
import kotlin.math.roundToInt
import kotlin.math.sin

/** Global switches for the art. */
object Art {
    /** Screenshots and renders want a still frame: no loop, a fixed moment. */
    @Volatile var still = false

    /** Art pixels advance about this often. */
    const val FRAME_MS = 110L
}

/** Things in a picture that answer a tap: the cat purrs, the kettle boils, the clock strikes the hour. */
enum class Toy { CAT, KETTLE, CLOCK }

/**
 * A picture painted into a [Buf]: [base] once (cached while [key] stays the same), then [anim] on
 * top for every frame with a growing tick.
 */
abstract class Scene(val w: Int, val h: Int) {
    abstract val key: Any
    abstract fun base(b: Buf)
    open fun anim(b: Buf, t: Int) = Unit

    /** Where each toy was drawn, as x, y, w, h in scene pixels; a toy not drawn here isn't in it. */
    private val spots = EnumMap<Toy, IntArray>(Toy::class.java)

    /** For a toy at play: the tick it started and the tick it stops. */
    private val play = EnumMap<Toy, IntArray>(Toy::class.java)

    /** The clock's strikes for its current hour, set when it's tapped. */
    var strikes = 0
        private set

    /** Marks where [toy] sits, so a tap there finds it. */
    protected fun spot(toy: Toy, x: Int, y: Int, w: Int, h: Int) {
        spots[toy] = intArrayOf(x, y, w, h)
    }

    /** The toy at ([x], [y]) in scene pixels, if any; the cat first, as it lies on top of things. */
    fun toyAt(x: Int, y: Int): Toy? = spots.entries.firstOrNull { (_, r) -> x in r[0] until r[0] + r[2] && y in r[1] until r[1] + r[3] }?.key

    /** Starts [toy] playing at tick [t]; false if it's still busy with the last tap. */
    fun start(toy: Toy, t: Int): Boolean {
        if (age(toy, t) >= 0) return false
        val ticks = when (toy) {
            Toy.CAT -> PURR_TICKS
            Toy.KETTLE -> KETTLE_TICKS
            Toy.CLOCK -> {
                strikes = (LocalTime.now().hour % 12).let { if (it == 0) 12 else it }
                strikes * STRIKE_TICKS + 20
            }
        }
        play[toy] = intArrayOf(t, t + ticks)
        return true
    }

    /** How many ticks [toy] has been playing at tick [t], or -1 if it isn't. */
    protected fun age(toy: Toy, t: Int): Int = play[toy]?.let { (from, to) -> if (t in from until to) t - from else -1 } ?: -1

    /** How many ticks [toy] has left to play at tick [t], or 0. */
    protected fun left(toy: Toy, t: Int): Int = play[toy]?.let { (from, to) -> if (t in from until to) to - t else 0 } ?: 0

    private var catX = -1
    private var catY = -1

    /** The sleeping cat, which lifts its head and breathes quick and deep while it purrs. */
    protected fun cat(b: Buf, x: Int, y: Int, t: Int) {
        catX = x; catY = y
        spot(Toy.CAT, x + 1, y + 3, 46, 25)
        val age = age(Toy.CAT, t)
        val purring = age >= 0
        // the head comes up a pixel a tick, stays up while it purrs, and settles back down at the end
        val lift = if (purring) minOf(age + 1, left(Toy.CAT, t), HEAD_LIFT) else 0
        Props.cat(b, x, y, if (purring) (sin(t * .75) + 1) / 2 else (sin(t * .18) + 1) / 2, lift = lift)
    }

    /** Little hearts rising from the cat while it purrs; drawn last, so nothing covers them. */
    protected fun purrHearts(b: Buf, t: Int) {
        val age = age(Toy.CAT, t)
        if (catX < 0 || age < 0) return
        for (i in 0 until 5) {
            val h = (age - i * 7).takeIf { it in 0 until 18 } ?: continue
            val hx = catX + 8 + i % 3 * 6 + (sin((t + i * 3) * .5) * 1.5).roundToInt()
            val a = (1f - h / 18f).coerceIn(0f, 1f)
            for ((u, v) in HEART) b.p(hx + u, catY - 2 - h + v, rgb(0xe0607a), a)
        }
    }

    /**
     * The steam of the kettle at ([x], [y]) drawn at scale [s] (as [Props.kettle]), and marks it as a toy. Simmering,
     * a thin wisp rises from the spout, as [Props.steam] at ([sx], [sy]) with [n] puffs, [len] and [a]; boiling, the wisp
     * gives way to a thick jet from the spout. Call after the kettle is painted.
     */
    protected fun kettleSteam(b: Buf, x: Int, y: Int, s: Double, t: Int, sx: Int, sy: Int, n: Int, len: Int, a: Float) {
        spot(Toy.KETTLE, x, y, (36 * s).roundToInt(), (30 * s).roundToInt())
        val age = age(Toy.KETTLE, t)
        // the boil builds like the whistle does, and dies away at the end
        val power = if (age < 0) 0.0 else minOf(age / 14.0, 1.0) * minOf(left(Toy.KETTLE, t) / 6.0, 1.0)
        if (power < 1) Props.steam(b, sx, sy, t, n, len, (a * (1 - power)).toFloat())
        if (age < 0) return
        Props.steamJet(b, x + (33 * s).roundToInt(), y + (11 * s).roundToInt(), t, power)
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

/** How long the kettle boils and whistles, in art ticks. */
const val KETTLE_TICKS = 40

/** Art ticks between the clock's strikes (the sound's own spacing). */
const val STRIKE_TICKS = 8

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
    // A tap on a toy plays it; any other tap passes on to whatever the picture sits in.
    val taps = Modifier.pointerInput(scene) {
        awaitEachGesture {
            val down = awaitFirstDown(requireUnconsumed = false)
            val k = scene.w / size.width.toFloat()
            val toy = scene.toyAt((down.position.x * k).toInt(), (down.position.y * k).toInt()) ?: return@awaitEachGesture
            val up = waitForUpOrCancellation() ?: return@awaitEachGesture
            up.consume()
            if (scene.start(toy, tick)) Toys.play(ctx, toy, scene.strikes)
        }
    }
    Canvas(modifier.aspectRatio(scene.w.toFloat() / scene.h).then(taps)) {
        val t = tick
        frame.copyFrom(base)
        scene.anim(frame, t)
        bitmap.setPixels(frame.d, 0, frame.w, 0, 0, frame.w, frame.h)
        val scale = size.width / scene.w
        drawImage(image, srcOffset = IntOffset.Zero, srcSize = IntSize(scene.w, scene.h),
            dstOffset = IntOffset.Zero, dstSize = IntSize(size.width.roundToInt(), (scene.h * scale).roundToInt()), filterQuality = FilterQuality.None)
    }
}
