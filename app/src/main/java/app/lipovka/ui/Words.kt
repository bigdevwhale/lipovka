package app.lipovka.ui

import android.content.Context
import app.lipovka.R
import app.lipovka.data.Content
import app.lipovka.data.Kind
import app.lipovka.data.Mail
import app.lipovka.data.Tx
import app.lipovka.domain.Sky
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.Locale

/** The words of a piece of mail, resolved for the reader's language. */
data class MailText(val from: String, val brief: String, val news: String, val kind: Kind, val title: String)

object Words {
    private val houses = mapOf(
        "shop" to Tx("Магазин", "The shop"), "club" to Tx("Клуб и библиотека", "The club and library"),
        "kuznetsovy" to Tx("Дом Кузнецовых", "The Kuznetsovs' house"), "vetrovy" to Tx("Дом Ветровых", "The Vetrovs' house"),
        "sorokina" to Tx("Дом Сорокиной", "Agafya Sorokina's house"), "ryabininy" to Tx("Дом Рябининых", "The Ryabinins' house"),
        "lebedev" to Tx("Дом учителя", "The teacher's house"), "sokolovy" to Tx("Дом Соколовых", "The Sokolovs' house"),
        "apiary" to Tx("Пасека", "The apiary"), "mill" to Tx("Мельница", "The mill"), "farmstead" to Tx("Хутор", "The farmstead"),
        "forester" to Tx("Лесничество", "The forester's lodge"), "workshop" to Tx("Мастерская", "The workshop"),
        "lastochkiny" to Tx("Дом Ласточкиных", "The Lastochkins' house"), "halt" to Tx("Разъезд 118 км", "Halt 118 km"),
        "stationhouse" to Tx("Дом машиниста", "The train driver's house"), "boatshed" to Tx("Лодочный сарай", "The boat shed"),
        "painter" to Tx("Домик художницы", "The painter's cottage"), "meteo" to Tx("Метеостанция", "The weather station"),
        "belkiny" to Tx("Дом Белкиных", "The Belkins' house"), "newspaper" to Tx("Редакция", "The newspaper office"),
        "museum" to Tx("Музей", "The museum"), "post" to Tx("Почта", "The post office"),
    )
    private val districts = listOf(
        Tx("Липовка", "Lipovka"), Tx("Заречье", "Zarechye"), Tx("Разъезд", "the Halt"),
        Tx("Озёрки", "Ozyorki"), Tx("Сосновый кордон", "the Pine Cordon"), Tx("Городок", "Gorodok"),
    )

    fun house(id: String, ru: Boolean) = houses[id]?.invoke(ru) ?: id
    fun district(d: Int, ru: Boolean) = districts.getOrNull(d)?.invoke(ru) ?: ""

    fun sky(s: Sky, ru: Boolean): String = when (s) {
        Sky.CLEAR -> if (ru) "ясно" else "clear"
        Sky.CLOUDY -> if (ru) "облачно" else "cloudy"
        Sky.OVERCAST -> if (ru) "пасмурно" else "overcast"
        Sky.FOG -> if (ru) "туман" else "fog"
        Sky.DRIZZLE -> if (ru) "морось" else "drizzle"
        Sky.RAIN -> if (ru) "дождь" else "rain"
        Sky.STORM -> if (ru) "гроза" else "thunderstorm"
        Sky.SNOW -> if (ru) "снег" else "snow"
        Sky.SLEET -> if (ru) "мокрый снег" else "sleet"
    }

    fun kind(c: Context, k: Kind): String = c.getString(
        when (k) {
            Kind.LETTER -> R.string.k_letter
            Kind.POSTCARD -> R.string.k_postcard
            Kind.PARCEL -> R.string.k_parcel
            Kind.TELEGRAM -> R.string.k_telegram
            Kind.REGISTERED -> R.string.k_registered
            Kind.NEWSPAPER -> R.string.k_newspaper
            Kind.NOTICE -> R.string.k_notice
        },
    )

    /** "1 240" with a thin non-breaking space. */
    fun num(n: Number): String = String.format(Locale.US, "%,d", n.toLong()).replace(',', ' ')

    fun km(steps: Long): String = String.format(Locale.US, "%.1f", steps * 0.72 / 1000).let { it.replace('.', ',') }

    fun date(c: Context, day: Long, today: LocalDate = LocalDate.now()): String {
        val d = LocalDate.ofEpochDay(day)
        val l = c.resources.configuration.locales[0]
        return d.format(DateTimeFormatter.ofPattern(if (d.year == today.year) "d MMMM" else "d MMMM yyyy", l))
    }

    fun ago(c: Context, day: Long, today: LocalDate = LocalDate.now()): String {
        val n = (today.toEpochDay() - day).toInt()
        return when {
            n <= 0 -> c.getString(R.string.today)
            n == 1 -> c.getString(R.string.yesterday)
            n < 14 -> c.resources.getQuantityString(R.plurals.days_ago, n, n)
            else -> date(c, day, today)
        }
    }

    private fun fill(s: String, name: String, year: Int) = s.replace("{name}", name).replace("{year}", year.toString())

    /** What a piece of mail says: the envelope, the evening line and the news at the gate. */
    fun mail(c: Context, content: Content, m: Mail, ru: Boolean, year: Int): MailText {
        val kind = Kind.of(m.kind)
        val to = content.resident(m.to)
        val name = to?.name?.invoke(ru) ?: ""
        val src = m.src
        return when {
            src.startsWith("arc:") -> {
                val b = content.beat(src.removePrefix("arc:"))
                MailText(b?.from?.invoke(ru) ?: "", fill(b?.brief?.invoke(ru) ?: "", name, year), fill(b?.news?.invoke(ru) ?: "", name, year), kind, name)
            }
            src.startsWith("tpl:") -> {
                val t = content.templateByKey[src.removePrefix("tpl:")]
                val v = t?.variants?.getOrNull(m.variant)?.invoke(ru) ?: ""
                MailText(t?.from?.invoke(ru) ?: "", fill(t?.brief?.invoke(ru) ?: "", name, year), fill(v, name, year), kind, name)
            }
            src.startsWith("fill:") -> {
                val f = content.fillers.getOrNull(src.removePrefix("fill:").toIntOrNull() ?: -1)
                MailText(f?.from?.invoke(ru) ?: "", fill(f?.brief?.invoke(ru) ?: "", name, year), fill(f?.news?.invoke(ru) ?: "", name, year), kind, name)
            }
            src.startsWith("evt:") -> {
                val e = content.eventByKey[src.removePrefix("evt:")]
                MailText(e?.name?.invoke(ru) ?: "", e?.brief?.invoke(ru) ?: "", e?.notice?.invoke(ru) ?: "", kind, name)
            }
            src.startsWith("reply:") -> {
                val from = content.resident(m.from)?.name?.invoke(ru) ?: c.getString(R.string.unknown_sender)
                val pick = listOf(R.string.reply_1, R.string.reply_2, R.string.reply_3)[Math.floorMod(m.id.toInt(), 3)]
                MailText(c.getString(R.string.from_reply, from), c.getString(R.string.reply_1, name, from), c.getString(pick, name, from), kind, name)
            }
            else -> MailText("", "", "", kind, name)
        }
    }
}
