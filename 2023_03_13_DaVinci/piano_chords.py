# Accord mineur 3, 7
# Accord majeur 4, 7

from itertools import permutations
from socket import socket
from sys import stdout

keyboard_ref = b"""
_________________________________________________________
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |c| |d|  |  |f| |g| |a|  |  |c| |d|  |  |f| |g| |a|  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| C | D | E | F | G | A | B | C | D | E | F | G | A | B |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
""".strip()

octave = b'CcDdEFfGgAaB' * 2

s = socket()
s.connect(("prog.dvc.tf", 7752))

data = s.recv(65535)
stdout.buffer.write(data)

while b'_________________________________________________________' in data:
    data = data[data.index(b'_________________________________________________________'):]
    permut = []

    start = 0
    for i in range(3):
        index = data.index(b'X', start)
        start = index + 1
        permut.append(keyboard_ref[index:start])

    for _1, _2, _3 in permutations(permut):
        mineur = octave.index(_1) + 3
        mineur = octave[mineur:mineur+1]
        majeur = octave.index(_1) + 4
        majeur = octave[majeur:majeur+1]
        quinte = octave.index(_1) + 7
        quinte = octave[quinte:quinte+1]
        if mineur in (_2, _3) and quinte in (_2, _3):
            type_ = b'm'
            break
        elif majeur in (_2, _3) and quinte in (_2, _3):
            type_ = b''
            break

    if _1.upper() != _1:
        type_ = b'#' + type_

    chord = _1.upper() + type_

    s.send(chord + b'\n')

    data = s.recv(65535)
    stdout.buffer.write(data)