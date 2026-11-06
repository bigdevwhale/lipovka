package app.lipovka.ui

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import android.os.VibrationEffect
import android.os.Vibrator
import android.util.Log
import androidx.core.content.getSystemService
import app.lipovka.R
import app.lipovka.ui.art.Toy
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.sqrt

/**
 * What the toys in the pictures sound and feel like when tapped. All are real recordings, kept short in res/raw:
 * - the cat's purr: "Misha purrs" by AstronautDown (freesound.org/s/376378), CC0;
 * - the kettle's whistle: "Whistling kettle" by Work With Sounds / Konrad Gutkowski (Wikimedia Commons), CC BY 4.0;
 * - the clock's strike: "clock chime" by gsb1039 (freesound.org/s/415061), CC0.
 * The calendar's sheet tearing off is made up here: a short crackle of noise, fibre by fibre.
 */
object Toys {
    private const val TAG = "Toys"

    /** Seconds between the clock's strikes; matches the art's strike ticks. */
    private const val STRIKE_GAP = 0.88

    /** A recording as it sits in res/raw: 16-bit mono PCM. */
    private class Clip(val rate: Int, val pcm: ShortArray)

    private val clips = HashMap<Int, Clip>()

    /** One player per toy; the clock's is remade when the hour (its number of strikes) changes. */
    private val tracks = HashMap<Toy, AudioTrack>()
    private var trackStrikes = 0

    fun play(context: Context, toy: Toy, strikes: Int = 0, tear: Boolean = true) {
        val app = context.applicationContext
        when (toy) {
            Toy.CAT -> clip(app, R.raw.purr)?.let { sound(toy, it); buzz(app, follow(it)) }
            Toy.KETTLE -> clip(app, R.raw.kettle)?.let { sound(toy, it); buzz(app, follow(it, 45)) }
            Toy.CLOCK -> clip(app, R.raw.chime)?.let { strike ->
                if (trackStrikes != strikes) { tracks.remove(toy)?.release(); trackStrikes = strikes }
                sound(toy, strikes(strike, strikes))
                buzz(app, knocks(strikes))
            }
            Toy.CALENDAR -> if (tear) rip.let { sound(toy, it); buzz(app, follow(it, 70)) } else buzz(app, intArrayOf(30))
        }
    }

    /** Reads a WAV's format and samples; each is small enough to keep in memory whole. */
    private fun clip(context: Context, res: Int): Clip? = clips[res] ?: runCatching {
        val bytes = context.resources.openRawResource(res).use { it.readBytes() }
        val b = ByteBuffer.wrap(bytes).order(ByteOrder.LITTLE_ENDIAN)
        var rate = 0
        var at = 12
        while (at + 8 <= bytes.size) {
            val id = String(bytes, at, 4, Charsets.US_ASCII)
            val size = b.getInt(at + 4)
            if (id == "fmt ") rate = b.getInt(at + 12)
            if (id == "data") {
                val n = minOf(size, bytes.size - at - 8) / 2
                return@runCatching Clip(rate, ShortArray(n) { b.getShort(at + 8 + it * 2) })
            }
            at += 8 + size + (size and 1)
        }
        error("no data in raw $res")
    }.onFailure { Log.w(TAG, "load", it) }.getOrNull()?.also { clips[res] = it }

    /** Paper tearing along the perforation: a burst of fine noise, its loudness jumping as each fibre gives. */
    private val rip: Clip by lazy {
        val rate = 22050
        val n = (rate * .34).toInt()
        val r = java.util.Random(7)
        var last = 0.0
        var fibre = 0.0
        Clip(rate, ShortArray(n) { i ->
            val t = i.toDouble() / n
            if (i % (rate / 90) == 0) fibre = .3 + r.nextDouble() * .7
            val noise = r.nextGaussian()
            // the difference of white noise leans it towards the hiss of paper rather than a rumble
            val hiss = noise - last
            last = noise
            val shape = minOf(t * 30, 1.0) * (1 - t) * (1 - t)
            (hiss * fibre * shape * 9000).coerceIn(-32767.0, 32767.0).toInt().toShort()
        })
    }

    /** The clock's strike rung [n] times, each ringing on under the next. */
    private fun strikes(one: Clip, n: Int): Clip {
        val gap = (one.rate * STRIKE_GAP).toInt()
        val mix = FloatArray(gap * (n - 1) + one.pcm.size)
        for (k in 0 until n) for (i in one.pcm.indices) mix[k * gap + i] += one.pcm[i].toFloat()
        val top = mix.maxOf { kotlin.math.abs(it) }.coerceAtLeast(Short.MAX_VALUE.toFloat())
        return Clip(one.rate, ShortArray(mix.size) { (mix[it] / top * Short.MAX_VALUE).toInt().toShort() })
    }

    /** Plays [clip] from the start on [toy]'s own player. */
    private fun sound(toy: Toy, clip: Clip) {
        runCatching {
            val t = tracks[toy] ?: AudioTrack.Builder()
                .setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_GAME).setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build())
                .setAudioFormat(AudioFormat.Builder().setSampleRate(clip.rate).setEncoding(AudioFormat.ENCODING_PCM_16BIT).setChannelMask(AudioFormat.CHANNEL_OUT_MONO).build())
                .setTransferMode(AudioTrack.MODE_STATIC)
                .setBufferSizeInBytes(clip.pcm.size * 2)
                .build()
                .also { it.write(clip.pcm, 0, clip.pcm.size); tracks[toy] = it }
            if (t.playState == AudioTrack.PLAYSTATE_PLAYING) t.stop()
            t.reloadStaticData()
            t.play()
        }.onFailure { Log.w(TAG, "play $toy", it) }
    }

    /** A buzz pattern as steps of [STEP] ms: soft pulses as strong as [clip] is loud at that moment, up to [most]. */
    private fun follow(clip: Clip, most: Int = 100): IntArray {
        val win = (clip.rate * STEP / 1000).toInt()
        val loud = DoubleArray(clip.pcm.size / win) { w ->
            var sum = 0.0
            for (i in w * win until (w + 1) * win) sum += clip.pcm[i].toDouble() * clip.pcm[i]
            sqrt(sum / win)
        }
        val top = loud.maxOrNull()?.takeIf { it > 0 } ?: 1.0
        return IntArray(loud.size) { (loud[it] / top * most).toInt() }
    }

    /** One firm knock in the hand for each of the clock's [n] strikes. */
    private fun knocks(n: Int): IntArray {
        val gap = (STRIKE_GAP * 1000 / STEP).toInt()
        return IntArray(gap * n) { if (it % gap == 0) 160 else 0 }
    }

    /** Plays [levels] (one per [STEP] ms, 0..255) as short soft pulses, so it's felt as a texture, not a drone. */
    private fun buzz(context: Context, levels: IntArray) {
        val v = context.getSystemService<Vibrator>() ?: return
        if (!v.hasVibrator() || levels.isEmpty()) return
        val timings = LongArray(levels.size * 2) { STEP / 2 }
        val amps = IntArray(levels.size * 2) { if (it % 2 == 1) 0 else levels[it / 2].coerceIn(0, 255) }
        runCatching {
            if (v.hasAmplitudeControl()) v.vibrate(VibrationEffect.createWaveform(timings, amps, -1))
            // Without soft steps a phone only buzzes full strength, so just a single short tremble.
            else v.vibrate(VibrationEffect.createOneShot(30, VibrationEffect.DEFAULT_AMPLITUDE))
        }.onFailure { Log.w(TAG, "buzz", it) }
    }

    private const val STEP = 40L
}
