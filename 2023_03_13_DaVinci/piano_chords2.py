# Accord mineur 3, 7
# Accord majeur 4, 7

from itertools import permutations
from socket import socket
from sys import stdout

ref_lines = b"""
____________________________
  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |
  |c| |d|  |  |f| |g| |a|  |
  |_| |_|  |  |_| |_| |_|  |
   |   |   |   |   |   |   |
 C | D | E | F | G | A | B |
___|___|___|___|___|___|___|
""".strip().splitlines()

keyboard_ref = b"""
_____________________________
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |c| |d|  |  |f| |g| |a|  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
| C | D | E | F | G | A | B |
|___|___|___|___|___|___|___|
""".strip().splitlines()

octave = b'CcDdEFfGgAaB' * 2

s = socket()
s.connect(("prog.dvc.tf", 7753))

data = s.recv(65535)
stdout.buffer.write(data)

while b'_________________________________________________________' in data:
    data = data[data.index(b'_________________________________________________________'):]
    keyboard_ref_temp = b''
    number = (len(data.split(maxsplit=1)[0]) // 28) - 1
    for i, line in enumerate(keyboard_ref):
        keyboard_ref_temp += line + ref_lines[i] * number + b'\n'
    permut = []

    start = 0
    for i in range(3):
        index = data.index(b'X', start)
        start = index + 1
        permut.append(keyboard_ref_temp[index:start])

    chords = []
    for _1, _2, _3 in permutations(permut):
        mineur = octave.index(_1) + 3
        mineur = octave[mineur:mineur+1]
        majeur = octave.index(_1) + 4
        majeur = octave[majeur:majeur+1]
        quinte = octave.index(_1) + 7
        quinte_plus = quinte + 1
        quinte_less = octave[quinte-1:quinte]
        quinte = octave[quinte:quinte_plus]
        quinte_plus = octave[quinte_plus:quinte_plus+1]
        if _1.upper() != _1:
            type_ = '#'
        else:
            type_ = ''
        if mineur in (_2, _3) and quinte in (_2, _3):
            type_ += 'm'
        elif majeur in (_2, _3) and quinte in (_2, _3):
            type_ += ''
        elif mineur in (_2, _3) and quinte_plus in (_2, _3):
            type_ += 'm+'
        elif mineur in (_2, _3) and quinte_less in (_2, _3):
            type_ += '-'
        elif majeur in (_2, _3) and quinte_plus in (_2, _3):
            type_ += '+'
        # elif majeur in (_2, _3) and quinte_less in (_2, _3):
        #     type_ += '-'
        else:
            continue

        chord = _1.upper().decode() + type_
        if chord not in chords:
            chords.append(chord)

    to_send = repr(chords).encode() + b'\n'
    stdout.buffer.write(to_send)
    s.send(to_send)

    stdout.buffer.write(keyboard_ref_temp)

    data = s.recv(65535)
    stdout.buffer.write(data)