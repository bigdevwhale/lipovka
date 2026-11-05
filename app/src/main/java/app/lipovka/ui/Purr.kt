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
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.sqrt

/**
 * The cat's purr when it's stroked: a real cat, two breaths of it ("Misha purrs" by AstronautDown,
 * freesound.org/s/376378, CC0), and a gentle buzz in the hand that follows the recording's own rise and fall.
 */
object Purr {
    private const val TAG = "Purr"

    /** The recording as it sits in res/raw/purr.wav: 16-bit mono PCM. */
    private class Sound(val rate: Int, val pcm: ShortArray)

    private var sound: Sound? = null
    private var track: AudioTrack? = null

    /** Reads the WAV's format and samples; small enough to keep in memory whole. */
    private fun load(context: Context): Sound? = sound ?: runCatching {
        val bytes = context.resources.openRawResource(R.raw.purr).use { it.readBytes() }
        val b = ByteBuffer.wrap(bytes).order(ByteOrder.LITTLE_ENDIAN)
        var rate = 0
        var at = 12
        while (at + 8 <= bytes.size) {
            val id = String(bytes, at, 4, Charsets.US_ASCII)
            val size = b.getInt(at + 4)
            if (id == "fmt ") rate = b.getInt(at + 12)
            if (id == "data") {
                val n = minOf(size, bytes.size - at - 8) / 2
                val pcm = ShortArray(n) { b.getShort(at + 8 + it * 2) }
                return@runCatching Sound(rate, pcm)
            }
            at += 8 + size + (size and 1)
        }
        error("no data in purr.wav")
    }.onFailure { Log.w(TAG, "load", it) }.getOrNull()?.also { sound = it }

    private fun made(s: Sound): AudioTrack? = track ?: runCatching {
        AudioTrack.Builder()
            .setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_GAME).setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build())
            .setAudioFormat(AudioFormat.Builder().setSampleRate(s.rate).setEncoding(AudioFormat.ENCODING_PCM_16BIT).setChannelMask(AudioFormat.CHANNEL_OUT_MONO).build())
            .setTransferMode(AudioTrack.MODE_STATIC)
            .setBufferSizeInBytes(s.pcm.size * 2)
            .build()
            .also { it.write(s.pcm, 0, s.pcm.size) }
    }.onFailure { Log.w(TAG, "track", it) }.getOrNull()?.also { track = it }

    /** Purrs once, from the start. */
    fun play(context: Context) {
        val s = load(context) ?: return
        runCatching {
            made(s)?.let { t ->
                if (t.playState == AudioTrack.PLAYSTATE_PLAYING) t.stop()
                t.reloadStaticData()
                t.play()
            }
        }.onFailure { Log.w(TAG, "play", it) }
        buzz(context, s)
    }

    /** The purr felt through the phone: short soft pulses, as strong as the recording is loud at that moment. */
    private fun buzz(context: Context, s: Sound) {
        val v = context.getSystemService<Vibrator>() ?: return
        if (!v.hasVibrator()) return
        val step = 40L
        val win = (s.rate * step / 1000).toInt()
        val loud = DoubleArray(s.pcm.size / win) { w ->
            var sum = 0.0
            for (i in w * win until (w + 1) * win) sum += s.pcm[i].toDouble() * s.pcm[i]
            sqrt(sum / win)
        }
        val top = loud.maxOrNull()?.takeIf { it > 0 } ?: return
        val timings = LongArray(loud.size * 2) { step / 2 }
        val amps = IntArray(loud.size * 2) { i -> if (i % 2 == 1) 0 else (loud[i / 2] / top * 100).toInt().coerceIn(0, 255) }
        runCatching {
            if (v.hasAmplitudeControl()) v.vibrate(VibrationEffect.createWaveform(timings, amps, -1))
            // Without soft steps a phone only buzzes full strength, so just a single short tremble.
            else v.vibrate(VibrationEffect.createOneShot(30, VibrationEffect.DEFAULT_AMPLITUDE))
        }.onFailure { Log.w(TAG, "buzz", it) }
    }
}
