# Hook

Open the downloaded file with wireshark, with fast analysis we can see lot of SMTP packets.
With scapy we can list packets and print data, but there are lot of data.
Data are random lower letters... but we can see a very long email data encoded in base64 (with upper letters and numbers).

So i do a script to extract all base64 data and save it in file, after that i call `file` command to know what is in these files. One of these files is a *text ASCII with very long line*, so i read it with `cat` and see a hexadecimal file. I decoded the file to get raw data, i use `file` command and i get a *png* file. I opened it and i get the flag.

Here a little script to get the flag:

```python
from base64 import b64decode, b16decode
from webbrowser import open as browser
from scapy.all import sniff, TCP, Raw
from re import compile as regex

datas = []
data = b''

for packet in sniff(offline="/media/kali/Downloads/capture.pcapng"):
	if packet[TCP].flags.flagrepr() == "S":
		datas.append(data)
		data = b''
	elif packet.haslayer(Raw):
		data += packet[Raw].load

regex1 = regex(r"\r\n\s*([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?\s*\r\n.\r\n".encode())
regex2 = regex(r"[0-9a-fA-F]+".encode())
counter = 0

for match in regex1.finditer(b'\n\n'.join(datas)):
	data = b64decode(match.group()[2:-5])
	if regex2.match(data):
		with open(f"{counter}.png", 'wb') as file:
			file.write(b16decode(data.upper()))
		counter += 1

browser("file:///home/kali/0.out")
```