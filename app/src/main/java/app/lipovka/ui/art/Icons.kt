package app.lipovka.ui.art

import app.lipovka.data.Kind

/** Small pixel icons for envelopes in lists, the widget and the settings. */
object Icons {
    fun kind(k: Kind): Buf {
        val b = Buf(18, 15)
        when (k) {
            Kind.TELEGRAM -> {
                b.r(0, 0, 18, 15, R.INK); b.r(1, 1, 16, 13, rgb(0xfbf3dc))
                for (i in 1 until 17 step 2) { b.p(i, 0, rgb(0xfbf3dc)); b.p(i, 14, rgb(0xfbf3dc)) }
                b.vgrad(3, 3, 12, 9, R.red.copyOfRange(1, 5))
                b.line(10, 3, 6, 7, rgb(0xf8d070)); b.line(6, 7, 11, 7, rgb(0xf8d070)); b.line(11, 7, 7, 11, rgb(0xf8d070)); b.line(9, 3, 5, 7, rgb(0xfff0b0))
            }
            Kind.POSTCARD -> {
                b.r(0, 1, 18, 13, R.INK); b.r(1, 2, 16, 11, rgb(0xfbf3dc)); b.vgrad(2, 3, 8, 9, R.morning)
                b.r(2, 9, 8, 3, rgb(0x426442)); b.r(12, 4, 4, 5, rgb(0xa33a2c)); b.r(11, 10, 5, 1, rgb(0x8a7a62))
            }
            Kind.PARCEL -> {
                b.vol(1, 2, 16, 12, { _, _ -> true }, { u, v -> .7 - u * .02 - v * .03 }, R.paper, R.INK)
                b.line(9, 2, 9, 13, rgb(0x7a4a2a)); b.line(1, 7, 16, 7, rgb(0x7a4a2a)); b.r(11, 9, 4, 3, rgb(0xa33a2c))
            }
            Kind.NEWSPAPER -> {
                b.r(1, 1, 16, 13, R.INK); b.r(2, 2, 14, 11, rgb(0xe8e2d4)); b.r(3, 3, 12, 2, rgb(0x2a2a30))
                for (y in 6 until 12 step 2) { b.r(3, y, 5, 1, rgb(0x8a8a92)); b.r(10, y, 5, 1, rgb(0x8a8a92)) }
            }
            Kind.NOTICE -> {
                b.r(2, 0, 14, 15, R.INK); b.r(3, 1, 12, 13, rgb(0xf6dc84)); b.r(4, 3, 10, 2, rgb(0xa33a2c))
                for (y in 7 until 13 step 2) b.r(5, y, 8, 1, rgb(0x55331e)); b.p(8, 0, rgb(0xa33a2c))
            }
            Kind.REGISTERED, Kind.LETTER -> {
                Props.envelope(b, 0, 1, 18, 13, if (k == Kind.REGISTERED) rgb(0xdce8f0) else rgb(0xf8eed4))
                b.r(12, 3, 4, 4, rgb(0x5a74aa)); b.r(13, 4, 2, 2, rgb(0xfbf3dc))
            }
        }
        return b
    }

    fun gear(): Buf {
        val b = Buf(12, 12)
        b.disc(6, 6, 4, R.INK); b.disc(6, 6, 2, rgb(0xf2e2bb))
        for ((x, y) in listOf(6 to 0, 6 to 11, 0 to 6, 11 to 6, 2 to 2, 10 to 2, 2 to 10, 10 to 10)) b.r(x - 1, y - 1, 2, 2, R.INK)
        return b
    }

    fun bag(): Buf {
        val b = Buf(20, 18)
        Props.envelope(b, 4, 0, 10, 6)
        b.vol(1, 5, 18, 13, { _, _ -> true }, { u, v -> .62 - u * .01 - v * .01 }, R.leather, rgb(0x140a06))
        b.vol(1, 5, 18, 6, { u, v -> v < 5 - if (kotlin.math.abs(u - 9) > 7) 1 else 0 }, { _, v -> .78 - v * .03 }, R.leather, rgb(0x140a06))
        b.r(8, 9, 4, 3, rgb(0xe8bf58))
        return b
    }
}
