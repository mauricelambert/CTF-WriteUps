# There are lot of directories, sub-directories and files and the flag is in one of them.
# To find it i write this script

from urllib.request import urlopen
from re import compile as regex

hrefs = regex(b'HREF=[^>]+')

def myiter(url1: str) -> None:
    print('.', end='', flush=True)
    response = urlopen(url1)
    data = response.read()
    if data.startswith(b'<H1>'):
        for url in hrefs.finditer(data):
            url = url.group()[5:]
            if url == b'.' or url == b'..':
                continue
            # print('URL:', url)
            myiter(url1 + url.decode())
    else:
        if b'ugra_' in data:
            print('Found:', data)
        # else:
            # print(data)

myiter('https://depth.q.2023.ugractf.ru/tvd25ezj30tn5c5d/')
