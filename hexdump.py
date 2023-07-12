def hexdump(buf):
    buf = bytearray(buf)
    alphabet = b"0123456789abcdef"
    ln = len(buf)
    # print("Len of buf: "+str(ln))
    print("   +------------------------------------------------+ +----------------+")
    print("   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |")
    i = 0
    while i < ln:
        if i % 128 == 0:
            print(
                "   +------------------------------------------------+ +----------------+"
            )
        s = b"|                                                | |................|"
        s0 = list(s)
        ix = 1
        iy = 52
        j = 0
        while j < 16:
            if (i + j) < ln:
                c = buf[i + j]
                s0[ix] = alphabet[(c >> 4) & 0x0F]
                ix += 1
                s0[ix] = alphabet[c & 0x0F]
                ix += 2
                if c > 31 and c < 127:
                    s0[iy] = c
                iy += 1
            j += 1
        index = int(i / 16)
        hd = ("00" + hex(index)[2:])[-2:] + "."
        s = bytearray(s0)
        s = hd + s.decode()
        print(s)
        i += 16
    print("   +------------------------------------------------+ +----------------+")
