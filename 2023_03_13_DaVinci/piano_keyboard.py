from socket import socket
from sys import stdout

keyboard = bytearray(b"""
_____________________________
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|
""".strip())

keyboard_ref = b"""
_____________________________
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |c| |d|  |  |f| |g| |a|  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
| C | D | E | F | G | A | B |
|___|___|___|___|___|___|___|
""".strip()

s = socket()
s.connect(("prog.dvc.tf", 7751))

data = s.recv(65535)
stdout.buffer.write(data)

data = data.splitlines()[-1]

keyboard_lines = keyboard.splitlines()

while data.startswith(b"Give me the "):
	index = data[12] - 48
	letter = data.split()[4]
	if b'#' in letter:
		letter = letter[:-1].lower()
	position = keyboard_ref.index(letter)
	last_keyboad = keyboard.copy()
	last_keyboad[position] = b'X'[0]
	last_keyboad_lines = last_keyboad.splitlines()
	to_send = b''
	for i, line in enumerate(keyboard_lines):
		to_send += line[:-1] * (index - 1) + last_keyboad_lines[i] + b'\n'
	stdout.buffer.write(to_send)
	s.send(to_send)
	data = s.recv(65535)
	stdout.buffer.write(data)
	data = data.splitlines()[-1]

s.close()