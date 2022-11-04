Responses:

1. Pajbot
2. Taher Elgamal
3. Vinton G. Cerf
4. Almon Strowger
5. NETBIOSRUNSSTILL

6. Question decode as base64:

```
syntax = "proto3";
message SomeMessage {
    string type = 1;
    string hexkey = 2;
    string ciphertext = 3;
}

.OTP.Z03dd47bb0e07d0bed85ac5ec519f437f1877f0f9fd9a1512f33305d1dc508efaa6ced1ce70ae39accabd0e427d.Z569904ef487cbe8dac2df59e3ac0214f6c28848bccec7c26cc6c6da4b40ff9c9caa28eba189a4ddf95d33d3500
```

Type: OTP
Key: 03dd47bb0e07d0bed85ac5ec519f437f1877f0f9fd9a1512f33305d1dc508efaa6ced1ce70ae39accabd0e427d
Cipher: 569904ef487cbe8dac2df59e3ac0214f6c28848bccec7c26cc6c6da4b40ff9c9caa28eba189a4ddf95d33d3500

Read this post: https://crypto.stackexchange.com/questions/10534/how-to-decode-an-otp-message

Decrypt with:

```python
from base64 import *

def strxor(s1,s2):
    return ''.join(chr(a ^ b) for a,b in zip(s1,s2))

strxor(b16decode(b'03dd47bb0e07d0bed85ac5ec519f437f1877f0f9fd9a1512f33305d1dc508efaa6ced1ce70ae39accabd0e427d'.upper()), b16decode(b'569904ef487cbe8dac2df59e3ac0214f6c28848bccec7c26cc6c6da4b40ff9c9caa28eba189a4ddf95d33d3500'.upper()))
```