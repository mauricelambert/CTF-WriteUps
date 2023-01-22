# Cartoons
# There are lot of ANSI escope code in this file https://en.wikipedia.org/wiki/ANSI_escape_code
# We can `cat` it but the flag is printed to fast and we can't read it
# So i write i little script to solve it
# flag: ugra_weve_got_terminals_pdwetksbjbrf

from sys import stdout
[stdout.buffer.write(b"\x1b" + x) and stdout.flush() or sleep(0.1) for x in open('cartoons.txt', 'rb').split(b'\x1b')]
