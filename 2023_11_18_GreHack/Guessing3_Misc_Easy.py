from socket import socket
from sys import stdout

max = 2147483647
min = 1

s = socket()
s.connect(("10.0.201.101", 20003))

data = s.recv(65535)
stdout.buffer.write(data)
stdout.flush()

while True:
    # data = s.recv(65535)
    # stdout.buffer.write(data)
    # stdout.flush()
    test = int((max - min) / 2 + min)
    data = str(test).encode()
    stdout.buffer.write(data)
    stdout.flush()
    s.sendall(data + b"\n")
    data = s.recv(65535)
    stdout.buffer.write(data)
    stdout.flush()
    if b" low." in data:
        min = test
    else:
        max = test

s.close()

# GH{R3v3rs3_1s_s1mpl3}
# 
# GH{Y0u_Kn0w_scr1pt1ng}

from socket import socket
from sys import stdout

max = 2147483647
min = 1

s = socket()
# s.connect(("10.0.201.101", 20003))
s.connect(("127.0.0.1", 9001))

data = s.recv(65535)
stdout.buffer.write(data)
stdout.flush()

while True:
    # data = s.recv(65535)
    # stdout.buffer.write(data)
    # stdout.flush()
    test = int((max - min) / 2 + min)
    data = str(test).encode() + b"\n"
    stdout.buffer.write(data)
    s.sendall(data)
    data = s.recv(65535)
    stdout.buffer.write(data)
    while True:
        if b" low." in data:
            min = test
            break
        elif b" high." in data:
            max = test
            break
        elif b"GH{" in data:
            break
        else:
            data = s.recv(65535)
            stdout.buffer.write(data)
    if b"GH{" in data:
        break
    print("Debug:", min, max)

s.close()
