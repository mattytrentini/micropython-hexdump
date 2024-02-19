def hd(buf):
    m = memoryview(buf)
    for i in range(0, len(m), 16):
        line = m[i:i+16]
        print("{:08x}  ".format(i),
            line[:8].hex(" "), "  ",
            line[8:].hex(" ") if len(line) > 8 else "  ",
            " " * 3 * (16-len(line)-1),
            "  |",
            "".join(chr(x) if 31 < x < 127 else "." for x in line),
            "|", sep="")
    print("{:08x}  ".format(i+1))

def xxd(buf):
    m = memoryview(buf)
    for i in range(0, len(m), 16):
        line = m[i:i+16]
        print("{:08x}: {}{}  {}".format(i,
            line.hex(" "),
            " " * 3 * (16-len(line)),
            "".join(chr(x) if 31 < x < 127 else "." for x in line)))
