from socket import socket
from sys import stdout

s = socket()
s.connect(('palindrome.misc.midnightflag.fr', 17002))
data = s.recv(65535)
stdout.buffer.write(data)

while True:
    is_pal = True
    data = s.recv(65535)
    stdout.buffer.write(data)
    word = data.split(b'Voici le mot : ')[-1].strip().lower().split()[0]
    for i in range(len(word)):
        if word[i] != word[-(i + 1)]: is_pal = False
    if is_pal: s.send(b'oui\n'); stdout.buffer.write(b'oui\n')
    else: s.send(b'non\n'); stdout.buffer.write(b'non\n')
    stdout.flush()
