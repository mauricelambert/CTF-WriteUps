from socket import socket
from sys import stdout

s = socket()
s.connect(("mc.ax", 31493))

data = '\0'

for i in range(256):
    stdout.buffer.write(s.recv(2048) + b'1\n')
    s.send(b'1\n')
    stdout.buffer.write(s.recv(2048) + b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\n')
    s.send(b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\n')
    stdout.buffer.write(s.recv(2048) + b'00000000000000000000000000000000\n')
    s.send(b'00000000000000000000000000000000\n')
    data = s.recv(2048)
    stdout.buffer.write(data + b'2\n')
    s.send(b'2\n')
    data = data.splitlines()[0]
    stdout.buffer.write(s.recv(2048) + data)
    s.send(data + b"\n")
    data = s.recv(2048)
    stdout.buffer.write(data + b'0\n')
    s.send(b'0\n')
    stdout.buffer.write(s.recv(2048))
    if b'00000000000000000000000000000000' in data:
        s.send(b'1\n')
        stdout.buffer.write(b'1\n')
    elif b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'.upper() in data.upper():
        s.send(b'0\n')
        stdout.buffer.write(b'0\n')
    stdout.flush()

s.close()

# Flag: dice{yeah_I_lost_like_10_points_on_that_proof_lmao}