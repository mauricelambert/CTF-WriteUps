# Snakee

## Executable analysis

```
C:\Users\MauriceLambert\Downloads>ElfAnalyzer snakee

ElfAnalyzer  Copyright (C) 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


EntropyAnalysis  Copyright (C) 2023, 2024  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


*********************************************************** ELF identification ************************************************************

Magic bytes              00000000-00000004   7f454c46                                .ELF                Elf Magic Bytes
ELF class                00000004-00000005   02                                      .                   Object 64 Bits (2)
ELF data                 00000005-00000006   01                                      .                   Little Endian (1)
ELF version              00000006-00000007   01                                      .                   Current (1)
ELF operating system     00000007-00000008   00                                      .                   SYSV (0)
ELF defined OS           00000008-00000009   00                                      .                   Os Unspecified (0)

*************************************************************** ELF headers ***************************************************************

ELF type                 00000010-00000012   0200                                    ..                  Executable (2)
ELF machine              00000012-00000014   3e00                                    >.                  AMD_X86_64 (62)
ELF version              00000014-00000018   01000000                                ....                Current (1)
ELF entry point          00000018-00000020   e624400000000000                        .$@.....            Entry Point (4203750)
ELF processor specific   00000030-00000034   00000000                                ....                Processor Specific Flags (0)
ELF header's size        00000034-00000036   4000                                    @.                  ELF header's size (64)
ELF entry header size    00000036-00000038   3800                                    8.                  Entry Header Table Size (56)
ELF header entry length  00000038-0000003a   0b00                                    ..                  Header Table Entry Number (11)
ELF entry section size   0000003a-0000003c   4000                                    @.                  Entry Section Header'S Size (64)
ELF section entry length 0000003c-0000003e   1c00                                    ..                  Section Header Entry Number (28)
Section header table     0000003e-00000040   1b00                                    ..                  Section Header Table Address (27)

************************************************************ ELF header table *************************************************************

Program header type      00000000-00000004   06000000                                ....                PT_PHDR (6)
Program header address   00000008-00000010   4000000000000000                        @.......            Program Header File Position (64)
Segment length file      00000020-00000028   6802000000000000                        h.......            Segment Size In Bytes In File Image (616)
Segment length memory    00000028-00000030   6802000000000000                        h.......            Segment Size In Bytes In Memory Image (616)
Segment alignment        00000030-00000038   0800000000000000                        ........            Segment Alignment (8)
Program header type      00000000-00000004   03000000                                ....                PT_INTERP (3)
Program header address   00000008-00000010   a802000000000000                        ........            Program Header File Position (680)
Segment length file      00000020-00000028   1c00000000000000                        ........            Segment Size In Bytes In File Image (28)
Segment length memory    00000028-00000030   1c00000000000000                        ........            Segment Size In Bytes In Memory Image (28)
Segment alignment        00000030-00000038   0100000000000000                        ........            No Segment Alignment (1)
Program header type      00000000-00000004   01000000                                ....                PT_LOAD (1)
Program header address   00000008-00000010   0000000000000000                        ........            Program Header File Position (0)
Segment length file      00000020-00000028   d015000000000000                        ........            Segment Size In Bytes In File Image (5584)
Segment length memory    00000028-00000030   d015000000000000                        ........            Segment Size In Bytes In Memory Image (5584)
Segment alignment        00000030-00000038   0010000000000000                        ........            Segment Alignment (4096)
Program header type      00000000-00000004   01000000                                ....                PT_LOAD (1)
Program header flags     00000004-00000008   05000000                                ....                PF_EXECUTE (5)
Program header flags     00000004-00000008   05000000                                ....                PF_READ (5)
Program header address   00000008-00000010   0020000000000000                        . ......            Program Header File Position (8192)
Segment length file      00000020-00000028   bd66000000000000                        .f......            Segment Size In Bytes In File Image (26301)
Segment length memory    00000028-00000030   bd66000000000000                        .f......            Segment Size In Bytes In Memory Image (26301)
Segment alignment        00000030-00000038   0010000000000000                        ........            Segment Alignment (4096)
Program header type      00000000-00000004   01000000                                ....                PT_LOAD (1)
Program header address   00000008-00000010   0090000000000000                        ........            Program Header File Position (36864)
Segment length file      00000020-00000028   1842000000000000                        .B......            Segment Size In Bytes In File Image (16920)
Segment length memory    00000028-00000030   1842000000000000                        .B......            Segment Size In Bytes In Memory Image (16920)
Segment alignment        00000030-00000038   0010000000000000                        ........            Segment Alignment (4096)
Program header type      00000000-00000004   01000000                                ....                PT_LOAD (1)
Program header flags     00000004-00000008   06000000                                ....                PF_WRITE (6)
Program header flags     00000004-00000008   06000000                                ....                PF_READ (6)
Program header address   00000008-00000010   e8dd000000000000                        ........            Program Header File Position (56808)
Segment length file      00000020-00000028   9004000000000000                        ........            Segment Size In Bytes In File Image (1168)
Segment length memory    00000028-00000030   8047000000000000                        .G......            Segment Size In Bytes In Memory Image (18304)
Segment alignment        00000030-00000038   0010000000000000                        ........            Segment Alignment (4096)
Program header type      00000000-00000004   02000000                                ....                PT_DYNAMIC (2)
Program header flags     00000004-00000008   06000000                                ....                PF_WRITE (6)
Program header flags     00000004-00000008   06000000                                ....                PF_READ (6)
Program header address   00000008-00000010   f8dd000000000000                        ........            Program Header File Position (56824)
Segment length file      00000020-00000028   0002000000000000                        ........            Segment Size In Bytes In File Image (512)
Segment length memory    00000028-00000030   0002000000000000                        ........            Segment Size In Bytes In Memory Image (512)
Segment alignment        00000030-00000038   0800000000000000                        ........            Segment Alignment (8)
Program header type      00000000-00000004   04000000                                ....                PT_NOTE (4)
Program header address   00000008-00000010   c402000000000000                        ........            Program Header File Position (708)
Segment length file      00000020-00000028   4400000000000000                        D.......            Segment Size In Bytes In File Image (68)
Segment length memory    00000028-00000030   4400000000000000                        D.......            Segment Size In Bytes In Memory Image (68)
Segment alignment        00000030-00000038   0400000000000000                        ........            Segment Alignment (4)
Program header type      00000000-00000004   50e57464                                P.td                PT_GNU_EH_FRAME (1685382480)
Program header address   00000008-00000010   d8bb000000000000                        ........            Program Header File Position (48088)
Segment length file      00000020-00000028   d402000000000000                        ........            Segment Size In Bytes In File Image (724)
Segment length memory    00000028-00000030   d402000000000000                        ........            Segment Size In Bytes In Memory Image (724)
Segment alignment        00000030-00000038   0400000000000000                        ........            Segment Alignment (4)
Program header type      00000000-00000004   51e57464                                Q.td                PT_GNU_STACK (1685382481)
Program header flags     00000004-00000008   06000000                                ....                PF_WRITE (6)
Program header flags     00000004-00000008   06000000                                ....                PF_READ (6)
Program header address   00000008-00000010   0000000000000000                        ........            Program Header File Position (0)
Segment length file      00000020-00000028   0000000000000000                        ........            Segment Size In Bytes In File Image (0)
Segment length memory    00000028-00000030   0000000000000000                        ........            Segment Size In Bytes In Memory Image (0)
Segment alignment        00000030-00000038   1000000000000000                        ........            Segment Alignment (16)
Program header type      00000000-00000004   52e57464                                R.td                PT_GNU_RELRO (1685382482)
Program header address   00000008-00000010   e8dd000000000000                        ........            Program Header File Position (56808)
Segment length file      00000020-00000028   1802000000000000                        ........            Segment Size In Bytes In File Image (536)
Segment length memory    00000028-00000030   1802000000000000                        ........            Segment Size In Bytes In Memory Image (536)
Segment alignment        00000030-00000038   0100000000000000                        ........            No Segment Alignment (1)

************************************************************ ELF section table ************************************************************

Name:                    0014a868-0014a869   00                                      .                   Undefined section role.
Section type             00000004-00000008   00000000                                ....                SHT_NULL (0)
Section offset           00000018-00000020   0000000000000000                        ........            Section File Offset (0)
Section size             00000020-00000028   0000000000000000                        ........            Section Size In Bytes (0)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .interp            0014a873-0014a87b   2e696e7465727000                        .interp.            Program interpreter
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   a802000000000000                        ........            Section File Offset (680)
Section size             00000020-00000028   1c00000000000000                        ........            Section Size In Bytes (28)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .note.gnu.build-id 0014a87b-0014a88e   2e6e6f74652e676e752e6275696c642d696400  .note.gnu.build-id. Specific vendor information
Section type             00000004-00000008   07000000                                ....                SHT_NOTE (7)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   c402000000000000                        ........            Section File Offset (708)
Section size             00000020-00000028   2400000000000000                        $.......            Section Size In Bytes (36)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .note.ABI-tag      0014a88e-0014a89c   2e6e6f74652e4142492d74616700            .note.ABI-tag.      Specific vendor information
Section type             00000004-00000008   07000000                                ....                SHT_NOTE (7)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   e802000000000000                        ........            Section File Offset (744)
Section size             00000020-00000028   2000000000000000                         .......            Section Size In Bytes (32)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .gnu.hash          0014a89c-0014a8a6   2e676e752e6861736800                    .gnu.hash.          Undefined section role.
Section type             00000004-00000008   f6ffff6f                                ...o                SHT_GNU_HASH (1879048182)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   0803000000000000                        ........            Section File Offset (776)
Section size             00000020-00000028   2800000000000000                        (.......            Section Size In Bytes (40)
Section link             00000028-0000002c   05000000                                ....                Section Link (5)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .dynsym            0014a8a6-0014a8ae   2e64796e73796d00                        .dynsym.            Dynamic linking symbol table
Section type             00000004-00000008   0b000000                                ....                SHT_DYNSYM (11)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   3003000000000000                        0.......            Section File Offset (816)
Section size             00000020-00000028   3807000000000000                        8.......            Section Size In Bytes (1848)
Section link             00000028-0000002c   06000000                                ....                Section Link (6)
Section info             0000002c-00000030   01000000                                ....                Section Info (1)
Symbol table entry size  00000038-00000040   1800000000000000                        ........            Symbol Table Entry Size (24)
Name: .dynstr            0014a8ae-0014a8b6   2e64796e73747200                        .dynstr.            Dynamic linking strings
Section type             00000004-00000008   03000000                                ....                SHT_STRTAB (3)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   680a000000000000                        h.......            Section File Offset (2664)
Section size             00000020-00000028   e502000000000000                        ........            Section Size In Bytes (741)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .gnu.version       0014a8b6-0014a8c3   2e676e752e76657273696f6e00              .gnu.version.       Undefined section role.
Section type             00000004-00000008   ffffff6f                                ...o                SHT_HIOS (1879048191)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   4e0d000000000000                        N.......            Section File Offset (3406)
Section size             00000020-00000028   9a00000000000000                        ........            Section Size In Bytes (154)
Section link             00000028-0000002c   05000000                                ....                Section Link (5)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0200000000000000                        ........            Symbol Table Entry Size (2)
Name: .gnu.version_r     0014a8c3-0014a8d2   2e676e752e76657273696f6e5f7200          .gnu.version_r.     Undefined section role.
Section type             00000004-00000008   feffff6f                                ...o                SHT_VERNEED (1879048190)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   e80d000000000000                        ........            Section File Offset (3560)
Section size             00000020-00000028   b000000000000000                        ........            Section Size In Bytes (176)
Section link             00000028-0000002c   06000000                                ....                Section Link (6)
Section info             0000002c-00000030   03000000                                ....                Section Info (3)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .rela.dyn          0014a8d2-0014a8dc   2e72656c612e64796e00                    .rela.dyn.          Undefined section role.
Section type             00000004-00000008   04000000                                ....                SHT_RELA (4)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   980e000000000000                        ........            Section File Offset (3736)
Section size             00000020-00000028   4800000000000000                        H.......            Section Size In Bytes (72)
Section link             00000028-0000002c   05000000                                ....                Section Link (5)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   1800000000000000                        ........            Symbol Table Entry Size (24)
Name: .rela.plt          0014a8dc-0014a8e6   2e72656c612e706c7400                    .rela.plt.          Undefined section role.
Section type             00000004-00000008   04000000                                ....                SHT_RELA (4)
Section flags            00000008-00000010   4200000000000000                        B.......            SHF_ALLOC (66)
Section flags            00000008-00000010   4200000000000000                        B.......            SHF_INFO_LINK (66)
Section offset           00000018-00000020   e00e000000000000                        ........            Section File Offset (3808)
Section size             00000020-00000028   f006000000000000                        ........            Section Size In Bytes (1776)
Section link             00000028-0000002c   05000000                                ....                Section Link (5)
Section info             0000002c-00000030   16000000                                ....                Section Info (22)
Symbol table entry size  00000038-00000040   1800000000000000                        ........            Symbol Table Entry Size (24)
Name: .init              0014a8e6-0014a8ec   2e696e697400                            .init.              Process initialization code
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_ALLOC (6)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_EXECINSTR (6)
Section offset           00000018-00000020   0020000000000000                        . ......            Section File Offset (8192)
Section size             00000020-00000028   1a00000000000000                        ........            Section Size In Bytes (26)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .plt               0014a8e1-0014a8e6   2e706c7400                              .plt.               Procedure linkage table
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_ALLOC (6)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_EXECINSTR (6)
Section offset           00000018-00000020   2020000000000000                          ......            Section File Offset (8224)
Section size             00000020-00000028   b004000000000000                        ........            Section Size In Bytes (1200)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   1000000000000000                        ........            Symbol Table Entry Size (16)
Name: .text              0014a8ec-0014a8f2   2e7465787400                            .text.              Executable instruction
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_ALLOC (6)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_EXECINSTR (6)
Section offset           00000018-00000020   d024000000000000                        .$......            Section File Offset (9424)
Section size             00000020-00000028   e261000000000000                        .a......            Section Size In Bytes (25058)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .fini              0014a8f2-0014a8f8   2e66696e6900                            .fini.              Process termination code
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_ALLOC (6)
Section flags            00000008-00000010   0600000000000000                        ........            SHF_EXECINSTR (6)
Section offset           00000018-00000020   b486000000000000                        ........            Section File Offset (34484)
Section size             00000020-00000028   0900000000000000                        ........            Section Size In Bytes (9)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .rodata            0014a8f8-0014a900   2e726f6461746100                        .rodata.            Read-only data
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   0090000000000000                        ........            Section File Offset (36864)
Section size             00000020-00000028   d82b000000000000                        .+......            Section Size In Bytes (11224)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .eh_frame_hdr      0014a900-0014a90e   2e65685f6672616d655f68647200            .eh_frame_hdr.      Undefined section role.
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   d8bb000000000000                        ........            Section File Offset (48088)
Section size             00000020-00000028   d402000000000000                        ........            Section Size In Bytes (724)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .eh_frame          0014a90e-0014a918   2e65685f6672616d6500                    .eh_frame.          Undefined section role.
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0200000000000000                        ........            SHF_ALLOC (2)
Section offset           00000018-00000020   b0be000000000000                        ........            Section File Offset (48816)
Section size             00000020-00000028   6813000000000000                        h.......            Section Size In Bytes (4968)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .init_array        0014a918-0014a924   2e696e69745f617272617900                .init_array.        Initialization function pointers
Section type             00000004-00000008   0e000000                                ....                SHT_INIT_ARRAY (14)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   e8dd000000000000                        ........            Section File Offset (56808)
Section size             00000020-00000028   0800000000000000                        ........            Section Size In Bytes (8)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0800000000000000                        ........            Symbol Table Entry Size (8)
Name: .fini_array        0014a924-0014a930   2e66696e695f617272617900                .fini_array.        Termination function pointers
Section type             00000004-00000008   0f000000                                ....                SHT_FINI_ARRAY (15)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   f0dd000000000000                        ........            Section File Offset (56816)
Section size             00000020-00000028   0800000000000000                        ........            Section Size In Bytes (8)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0800000000000000                        ........            Symbol Table Entry Size (8)
Name: .dynamic           0014a930-0014a939   2e64796e616d696300                      .dynamic.           Dynamic linking information
Section type             00000004-00000008   06000000                                ....                SHT_DYNAMIC (6)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   f8dd000000000000                        ........            Section File Offset (56824)
Section size             00000020-00000028   0002000000000000                        ........            Section Size In Bytes (512)
Section link             00000028-0000002c   06000000                                ....                Section Link (6)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   1000000000000000                        ........            Symbol Table Entry Size (16)
Name: .got               0014a939-0014a93e   2e676f7400                              .got.               Global offset table
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   f8df000000000000                        ........            Section File Offset (57336)
Section size             00000020-00000028   0800000000000000                        ........            Section Size In Bytes (8)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0800000000000000                        ........            Symbol Table Entry Size (8)
Name: .got.plt           0014a93e-0014a947   2e676f742e706c7400                      .got.plt.           Global offset table
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   00e0000000000000                        ........            Section File Offset (57344)
Section size             00000020-00000028   6802000000000000                        h.......            Section Size In Bytes (616)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0800000000000000                        ........            Symbol Table Entry Size (8)
Name: .data              0014a947-0014a94d   2e6461746100                            .data.              Initialized data
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   68e2000000000000                        h.......            Section File Offset (57960)
Section size             00000020-00000028   1000000000000000                        ........            Section Size In Bytes (16)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .bss               0014a94d-0014a952   2e62737300                              .bss.               Uninitialized data
Section type             00000004-00000008   08000000                                ....                SHT_NOBITS (8)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_WRITE (3)
Section flags            00000008-00000010   0300000000000000                        ........            SHF_ALLOC (3)
Section offset           00000018-00000020   78e2000000000000                        x.......            Section File Offset (57976)
Section size             00000020-00000028   e842000000000000                        .B......            Section Size In Bytes (17128)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .comment           0014a952-0014a95b   2e636f6d6d656e7400                      .comment.           Version control information
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section flags            00000008-00000010   3000000000000000                        0.......            SHF_MERGE (48)
Section flags            00000008-00000010   3000000000000000                        0.......            SHF_STRINGS (48)
Section offset           00000018-00000020   78e2000000000000                        x.......            Section File Offset (57976)
Section size             00000020-00000028   5c00000000000000                        \.......            Section Size In Bytes (92)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0100000000000000                        ........            Symbol Table Entry Size (1)
Name: pydata             0014a95b-0014a962   70796461746100                          pydata.             Undefined section role.
Section type             00000004-00000008   01000000                                ....                SHT_PROGBITS (1)
Section offset           00000018-00000020   d4e2000000000000                        ........            Section File Offset (58068)
Section size             00000020-00000028   94c5130000000000                        ........            Section Size In Bytes (1295764)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)
Name: .shstrtab          0014a869-0014a873   2e736873747274616200                    .shstrtab.          Section names
Section type             00000004-00000008   03000000                                ....                SHT_STRTAB (3)
Section offset           00000018-00000020   68a8140000000000                        h.......            Section File Offset (1353832)
Section size             00000020-00000028   fa00000000000000                        ........            Section Size In Bytes (250)
Section link             00000028-0000002c   00000000                                ....                Section Link (0)
Section info             0000002c-00000030   00000000                                ....                Section Info (0)
Symbol table entry size  00000038-00000040   0000000000000000                        ........            No Section Symbal Table (0)

************************************************************* Comment section *************************************************************

Version control info     0000e278-0000e2a6   GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44).GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44)
Version control info     0000e2a6-0000e2d6   GCC: (GNU) 10.2.1 20210130 (Red Hat 10.2.1-11).GCC: (GNU) 10.2.1 20210130 (Red Hat 10.2.1-11)

************************************************************** Note sections **************************************************************

Note name size           00000000-00000004   04000000                                ....                Note name size (4)
Descriptor size          00000004-00000008   14000000                                ....                Note descriptor size (20)
Note type                00000008-0000000c   03000000                                ....                Note type (3)
Note name                000002d0-000002d4   474e5500                                GNU.                GNU
Note descriptor          000002d4-000002e8   8485f6953c06d12b9865185ba3466fdbf9b4a65c....<..+.e.[.Fo....\
Note name size           00000000-00000004   04000000                                ....                Note name size (4)
Descriptor size          00000004-00000008   10000000                                ....                Note descriptor size (16)
Note type                00000008-0000000c   01000000                                ....                Note type (1)
Note name                000002f4-000002f8   474e5500                                GNU.                GNU
Note descriptor          000002f8-00000308   00000000020000000600000020000000        ............ ...

************************************************************* Dynamic section *************************************************************

Tag DT_NEEDED            0000ddf8-0000de00   0100000000000000                        ........            Needed library name offset
Value                    0000de00-0000de08   7502000000000000                        u.......            629
Tag DT_NEEDED            0000de08-0000de10   0100000000000000                        ........            Needed library name offset
Value                    0000de10-0000de18   8002000000000000                        ........            640
Tag DT_NEEDED            0000de18-0000de20   0100000000000000                        ........            Needed library name offset
Value                    0000de20-0000de28   8a02000000000000                        ........            650
Tag DT_NEEDED            0000de28-0000de30   0100000000000000                        ........            Needed library name offset
Value                    0000de30-0000de38   9a02000000000000                        ........            666
Tag DT_INIT              0000de38-0000de40   0c00000000000000                        ........            Initialization function address
Address                  0000de40-0000de48   0020400000000000                        . @.....            4202496
Tag DT_FINI              0000de48-0000de50   0d00000000000000                        ........            Termination function address
Address                  0000de50-0000de58   b486400000000000                        ..@.....            4228788
Tag DT_INIT_ARRAY        0000de58-0000de60   1900000000000000                        ........            Initialization functions pointers
Address                  0000de60-0000de68   e8ed400000000000                        ..@.....            4255208
Tag DT_INIT_ARRAYSZ      0000de68-0000de70   1b00000000000000                        ........            Initialization functions number
Value                    0000de70-0000de78   0800000000000000                        ........            8
Tag DT_FINI_ARRAY        0000de78-0000de80   1a00000000000000                        ........            Termination functions pointers
Address                  0000de80-0000de88   f0ed400000000000                        ..@.....            4255216
Tag DT_FINI_ARRAYSZ      0000de88-0000de90   1c00000000000000                        ........            Termination functions number
Value                    0000de90-0000de98   0800000000000000                        ........            8
Tag UNDEFINED            0000de98-0000dea0   f5feff6f00000000                        ...o....            None
Value                    0000dea0-0000dea8   0803400000000000                        ..@.....            4195080
Tag DT_STRTAB            0000dea8-0000deb0   0500000000000000                        ........            Address string table (.dynstr)
Address                  0000deb0-0000deb8   680a400000000000                        h.@.....            4196968
Tag DT_SYMTAB            0000deb8-0000dec0   0600000000000000                        ........            Address symbol table (.dynsym)
Address                  0000dec0-0000dec8   3003400000000000                        0.@.....            4195120
Tag DT_STRSZ             0000dec8-0000ded0   0a00000000000000                        ........            String table size
Value                    0000ded0-0000ded8   e502000000000000                        ........            741
Tag DT_SYMENT            0000ded8-0000dee0   0b00000000000000                        ........            Symbol table entry size
Value                    0000dee0-0000dee8   1800000000000000                        ........            24
Tag DT_DEBUG             0000dee8-0000def0   1500000000000000                        ........            Used for debugging
Address                  0000def0-0000def8   0000000000000000                        ........            0
Tag DT_PLTGOT            0000def8-0000df00   0300000000000000                        ........            Address procedure linkage table
Address                  0000df00-0000df08   00f0400000000000                        ..@.....            4255744
Tag DT_PLTRELSZ          0000df08-0000df10   0200000000000000                        ........            Relocation entries size
Value                    0000df10-0000df18   f006000000000000                        ........            1776
Tag DT_PLTREL            0000df18-0000df20   1400000000000000                        ........            Relocation entry type
Value                    0000df20-0000df28   0700000000000000                        ........            7
Tag DT_JMPREL            0000df28-0000df30   1700000000000000                        ........            Procedure linkage table
Address                  0000df30-0000df38   e00e400000000000                        ..@.....            4198112
Tag DT_RELA              0000df38-0000df40   0700000000000000                        ........            Address relocation table
Address                  0000df40-0000df48   980e400000000000                        ..@.....            4198040
Tag DT_RELASZ            0000df48-0000df50   0800000000000000                        ........            Relocation table size
Value                    0000df50-0000df58   4800000000000000                        H.......            72
Tag DT_RELAENT           0000df58-0000df60   0900000000000000                        ........            Relocation entry size
Value                    0000df60-0000df68   1800000000000000                        ........            24
Tag UNDEFINED            0000df68-0000df70   feffff6f00000000                        ...o....            None
Value                    0000df70-0000df78   e80d400000000000                        ..@.....            4197864
Tag UNDEFINED            0000df78-0000df80   ffffff6f00000000                        ...o....            None
Value                    0000df80-0000df88   0300000000000000                        ........            3
Tag UNDEFINED            0000df88-0000df90   f0ffff6f00000000                        ...o....            None
Value                    0000df90-0000df98   4e0d400000000000                        N.@.....            4197710
Tag DT_NULL              0000df98-0000dfa0   0000000000000000                        ........            End of dynamic array
Value                    0000dfa0-0000dfa8   0000000000000000                        ........            0

C:\Users\MauriceLambert\Downloads>EntropyAnalysis --force-cli snakee

EntropyAnalysis  Copyright (C) 2023, 2024  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

'snakee' full file entropy analysis:
000000000000-00000014b068    7.974048651279646
'snakee' detailed entropy analysis:
000000000000-000000000800    1.7472787783436623
0000000034f7-000000003cf7    5.823145190258419
0000000069ee-0000000071ee    5.823609726488164
000000009ee5-00000000a6e5    4.789256768427682
00000000d3dc-00000000dbdc    0.0
0000000108d3-0000000110d3    7.911106689548471
000000013dca-0000000145ca    7.879889274321314
0000000172c1-000000017ac1    7.906113361634997
00000001a7b8-00000001afb8    7.900925397454753
00000001dcaf-00000001e4af    7.890675637726793
0000000211a6-0000000219a6    7.918690713891865
00000002469d-000000024e9d    7.898181472785146
000000027b94-000000028394    7.886851070089209
00000002b08b-00000002b88b    7.889883665868806
00000002e582-00000002ed82    7.895551718088976
000000031a79-000000032279    7.901284613248958
000000034f70-000000035770    7.901903576704937
000000038467-000000038c67    7.89517580872105
00000003b95e-00000003c15e    7.876341174932382
00000003ee55-00000003f655    7.887327407075621
00000004234c-000000042b4c    7.877724852853946
000000045843-000000046043    7.889780291776485
000000048d3a-00000004953a    7.917798207315291
00000004c231-00000004ca31    7.893108439643887
00000004f728-00000004ff28    7.890932907416214
000000052c1f-00000005341f    7.904369914066222
000000056116-000000056916    7.893596174920915
00000005960d-000000059e0d    7.909751582382103
00000005cb04-00000005d304    7.902911314845479
00000005fffb-0000000607fb    7.8969175143143255
0000000634f2-000000063cf2    7.886148216167873
0000000669e9-0000000671e9    7.898647924606975
000000069ee0-00000006a6e0    7.8841964534884035
00000006d3d7-00000006dbd7    7.8652007556356285
0000000708ce-0000000710ce    7.897975506071168
000000073dc5-0000000745c5    7.892624836608385
0000000772bc-000000077abc    7.909483242863818
00000007a7b3-00000007afb3    7.899203907474413
00000007dcaa-00000007e4aa    7.89387603891092
0000000811a1-0000000819a1    7.907858763766763
000000084698-000000084e98    7.914111130370655
000000087b8f-00000008838f    7.886421012702603
00000008b086-00000008b886    7.896601132650018
00000008e57d-00000008ed7d    7.904733122276754
000000091a74-000000092274    7.898938833427435
000000094f6b-00000009576b    7.890630636900905
000000098462-000000098c62    7.896142245581862
00000009b959-00000009c159    7.899573391940083
00000009ee50-00000009f650    7.900627969894859
0000000a2347-0000000a2b47    7.903695868162017
0000000a583e-0000000a603e    7.892517568601851
0000000a8d35-0000000a9535    7.896574158270218
0000000ac22c-0000000aca2c    7.90389802342191
0000000af723-0000000aff23    7.9038396715013555
0000000b2c1a-0000000b341a    7.876526766828024
0000000b6111-0000000b6911    7.888193716256806
0000000b9608-0000000b9e08    7.905714658308207
0000000bcaff-0000000bd2ff    7.892117926563442
0000000bfff6-0000000c07f6    7.889192585479193
0000000c34ed-0000000c3ced    7.907084110571385
0000000c69e4-0000000c71e4    7.908276622543106
0000000c9edb-0000000ca6db    7.886235968502467
0000000cd3d2-0000000cdbd2    7.914477630225644
0000000d08c9-0000000d10c9    7.8997848496859
0000000d3dc0-0000000d45c0    7.896187829101619
0000000d72b7-0000000d7ab7    7.908348436052269
0000000da7ae-0000000dafae    7.909029719438384
0000000ddca5-0000000de4a5    7.904801717422534
0000000e119c-0000000e199c    7.896612503801657
0000000e4693-0000000e4e93    7.902649247111639
0000000e7b8a-0000000e838a    7.882374251143718
0000000eb081-0000000eb881    7.908252907762553
0000000ee578-0000000eed78    7.890907377435041
0000000f1a6f-0000000f226f    7.883371554909998
0000000f4f66-0000000f5766    7.905090316312959
0000000f845d-0000000f8c5d    7.885235279193688
0000000fb954-0000000fc154    7.909627229931848
0000000fee4b-0000000ff64b    7.905482830986626
000000102342-000000102b42    7.717803211840877
000000105839-000000106039    7.892386711393946
000000108d30-000000109530    7.91040580351733
00000010c227-00000010ca27    7.885248051335043
00000010f71e-00000010ff1e    7.902164163136813
000000112c15-000000113415    7.8954555033825935
00000011610c-00000011690c    7.892024890595279
000000119603-000000119e03    7.884893747186394
00000011cafa-00000011d2fa    7.888093939340367
00000011fff1-0000001207f1    7.9001904407850105
0000001234e8-000000123ce8    7.877117906478292
0000001269df-0000001271df    7.904171602624994
000000129ed6-00000012a6d6    7.818344093495476
00000012d3cd-00000012dbcd    7.892378473007123
0000001308c4-0000001310c4    7.882515598585604
000000133dbb-0000001345bb    7.91447162742756
0000001372b2-000000137ab2    7.879507179932182
00000013a7a9-00000013afa9    7.9121312497223455
00000013dca0-00000013e4a0    7.8926488430057145
000000141197-000000141997    7.892749056022091
00000014468e-000000144e8e    7.890241831714852
000000147b85-000000148385    7.895806705827556
00000014b07c-00000014b87c    2.313854329609176


C:\Users\MauriceLambert\Downloads>
```

So we have a very high entropy (7.8~7.9) and the last and greater section name is `pydata`... Probably a PyInstaller packaged ELF. I use the following web app: https://pyinstxtractor-web.netlify.app/, to obtain a ZIP file with all pyc (python compiled) files.

## PYC

To get the python code from pyc file, i use the following web app: https://www.pylingual.io/

## Decompiled code

```python
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: snakee.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from base64 import b64decode
FLAG = 'WH&J~H8V3aH#0FaGB##4H#0FaW;HP~Gcz(bG&46hGcz(aVmCN6H#7'

def main():
    flute()
    print('Tss, tsss, whatssss zee flag?')
    guess = input('🐍 ')
    if check(guess):
        print('Congratsss!')
    else:
        print('Tss, tsss, try again.')

def flute():
    tss = b'Cmdsb2JhbCBjaGVjawpkZWYgY2hlY2soZ3Vlc3M6IHN0cikgLT4gYm9vbDoKICAgIGZyb20gYmluYXNjaWkgaW1wb3J0IGhleGxpZnkKICAgIGZyb20gYmFzZTY0IGltcG9ydCBiODVlbmNvZGUKICAgIGd1ZXNzID0gaGV4bGlmeShndWVzcy5lbmNvZGUoInV0Zi04IikpWzo6LTFdCiAgICBndWVzcyA9IGI4NWVuY29kZShndWVzcykuZGVjb2RlKCJ1dGYtOCIpCiAgICByZXR1cm4gZ3Vlc3MgPT0gRkxBRwogICAg'
    exec(b64decode(tss))
if __name__ == '__main__':
    main()
```

## Decode the flag

```python
>>> from base64 import b85decode, b16decode
>>> b16decode(b85decode(b"WH&J~H8V3aH#0FaGB##4H#0FaW;HP~Gcz(bG&46hGcz(aVmCN6H#7").upper()[::-1])
b'GH{b3w4r3!_17_b1735!}'
>>>
```