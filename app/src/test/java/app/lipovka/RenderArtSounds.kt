package app.lipovka

import app.lipovka.ui.Ambience
import app.lipovka.ui.Ambience.Layer
import org.junit.Test
import java.io.File
import java.nio.ByteBuffer
import java.nio.ByteOrder

/**
 * Puts every post office sound in app/build/art/sounds to listen to (run with `-Prender`): the made-up clock and
 * stove as WAVs, and the recordings copied as they are.
 */
class RenderArtSounds {
    private val out = File(System.getProperty("render.out") ?: "build/art", "sounds").apply { deleteRecursively(); mkdirs() }

    private fun wav(name: String, pcm: ShortArray) {
        val b = ByteBuffer.allocate(44 + pcm.size * 2).order(ByteOrder.LITTLE_ENDIAN)
        b.put("RIFF".toByteArray()).putInt(36 + pcm.size * 2).put("WAVEfmt ".toByteArray()).putInt(16).putShort(1).putShort(1)
            .putInt(Ambience.SAMPLE_RATE).putInt(Ambience.SAMPLE_RATE * 2).putShort(2).putShort(16).put("data".toByteArray()).putInt(pcm.size * 2)
        for (v in pcm) b.putShort(v)
        File(out, "$name.wav").writeBytes(b.array())
    }

    @Test fun sounds() {
        wav("clock", Ambience.synth(Layer.CLOCK, 12))
        wav("stove", Ambience.synth(Layer.STOVE, 30))
        for (l in Layer.entries) {
            val f = File("src/main/assets/ambience/${l.file}.ogg")
            if (f.exists()) f.copyTo(File(out, "${l.name.lowercase()}.ogg"), overwrite = true)
        }
    }
}
