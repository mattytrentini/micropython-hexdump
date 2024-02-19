# micropython-hexdump

A simple implementation of hexdump (`hd` and `xxd`) tools for MicroPython.

## Installation

Use `mip` from the command line using `mpremote`:

```bash
> mpremote mip install github:mattytrentini/micropython-hexdump
```

or from within a running instance of MicroPython that has an established
internet connection.

```python
>>> import mip
>>> mip.install("github:mattytrentini/micropython-hexdump")
```

## Example usage

```text
>>> from os import urandom
>>> from hexdump import hd, xxd
>>> data = urandom(100)
>>> hd(data)
00000000  4d 9a 16 3d 4c 87 c4 31  9e 95 36 e3 f8 49 4b 4b  |M..=L..1..6..IKK|
00000010  98 12 6b b6 a6 a3 fd 1b  91 a5 21 95 73 ac 35 6f  |..k.......!.s.5o|
00000020  dc b4 4d 0b 43 fb bb 36  d6 17 52 4d 40 b4 04 ed  |..M.C..6..RM@...|
00000030  2b 7c 8b 30 84 a3 96 9a  71 e4 e5 69 d1 62 b7 06  |+|.0....q..i.b..|
00000040  fd 89 3a f7 b3 06 04 39  f9 70 62 33 d2 56 35 e2  |..:....9.pb3.V5.|
00000050  fc 7e 16 46 5f 35 1d 62  63 d4 5c 18 f3 de 6d 3c  |.~.F_5.bc.\...m<|
00000060  a1 1f fa ed                                       |....|
00000061
>>> xxd(data)
00000000: 4d 9a 16 3d 4c 87 c4 31 9e 95 36 e3 f8 49 4b 4b  M..=L..1..6..IKK
00000010: 98 12 6b b6 a6 a3 fd 1b 91 a5 21 95 73 ac 35 6f  ..k.......!.s.5o
00000020: dc b4 4d 0b 43 fb bb 36 d6 17 52 4d 40 b4 04 ed  ..M.C..6..RM@...
00000030: 2b 7c 8b 30 84 a3 96 9a 71 e4 e5 69 d1 62 b7 06  +|.0....q..i.b..
00000040: fd 89 3a f7 b3 06 04 39 f9 70 62 33 d2 56 35 e2  ..:....9.pb3.V5.
00000050: fc 7e 16 46 5f 35 1d 62 63 d4 5c 18 f3 de 6d 3c  .~.F_5.bc.\...m<
00000060: a1 1f fa ed                                      ....
```
