# Guessing 2 - Reverse

I use the following command to get informations about executable:

`python3 -m ElfAnalyzer guessing`.

We can see the compiler in `.comment` section: `GCC: (Debian 12.2.0-14) 12.2.0` and the section `gcc_except_table`, this section is used by GCC for C++ *try ... catch* syntax, this is probably a C++ code.

I use Ghidra to get a pseudo C code but it's probably easiest to use a debugger (dynamic analysis) instead of reverse tool (static analysis) to solve this challenge.

```c
undefined4 FUN_08049803(void)

{
  ushort uVar1;
  undefined4 uVar2;
  int iVar3;
  undefined4 **ppuVar4;
  undefined4 *puStack_40;
  uint *puStack_3c;
  undefined4 uStack_38;
  undefined4 uStack_34;
  undefined auStack_30 [4];
  undefined4 local_2c;
  uint local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  int local_18;
  undefined4 *local_14;
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  uStack_34 = 0x804981a;
  uStack_38 = 0;
  puStack_3c = (uint *)0x1;
  puStack_40 = (undefined4 *)0x2;
  local_14 = (undefined4 *)FUN_08080360();
  if (local_14 == (undefined4 *)0x0) {
    puStack_40 = (undefined4 *)0x80d6008;
    FUN_08053350();
    uVar2 = 0xffffffff;
  }
  else {
    local_24 = 0;
    local_20 = 0;
    local_1c = 0;
    local_28 = 2;
    puStack_40 = (undefined4 *)0x0;
    local_24 = FUN_08080750();
    puStack_40 = (undefined4 *)0x2329;
    uVar1 = FUN_08080760();
    local_28 = local_28 & 0xffff | (uint)uVar1 << 0x10;
    local_2c = 0x10;
    uStack_38 = 0x10;
    puStack_3c = &local_28;
    puStack_40 = local_14;
    iVar3 = FUN_08080240();
    if (iVar3 < 0) {
      puStack_40 = (undefined4 *)0x80d6022;
      FUN_08053350();
      puStack_40 = &DAT_0810f460;
      FUN_08060590();
      uVar2 = 0xffffffff;
    }
    else {
      puStack_3c = (uint *)0x1e;
      puStack_40 = local_14;
      iVar3 = FUN_080802e0();
      ppuVar4 = (undefined4 **)auStack_30;
      if (iVar3 < 0) {
        puStack_40 = (undefined4 *)0x80d603b;
        FUN_08053350();
        puStack_40 = &DAT_0810f460;
        FUN_08060590();
        puStack_40 = (undefined4 *)0x1;
        FUN_08051650();
        ppuVar4 = &puStack_40;
      }
      *(undefined4 *)((int)ppuVar4 + -0xc) = 0x2329;
      *(char **)((int)ppuVar4 + -0x10) = "Server listen on port %d\n";
      *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049947;
      FUN_08053420();
      *(undefined4 **)((int)ppuVar4 + -0x10) = &DAT_0810f5a0;
      *(undefined4 *)((int)ppuVar4 + -0x14) = 0x804995b;
      FUN_08060590();
      do {
        *(undefined4 **)((int)ppuVar4 + -8) = &local_2c;
        *(uint **)((int)ppuVar4 + -0xc) = &local_28;
        *(undefined4 **)((int)ppuVar4 + -0x10) = local_14;
        *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049971;
        DAT_081106dc = FUN_080801a0();
        if (DAT_081106dc < 0) {
          *(char **)((int)ppuVar4 + -0x10) = "Connection failure\n";
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049993;
          FUN_08053350();
          *(undefined4 **)((int)ppuVar4 + -0x10) = &DAT_0810f460;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x80499a7;
          FUN_08060590();
        }
        *(undefined4 *)((int)ppuVar4 + -4) = 0x80499af;
        local_18 = FUN_0807bac0();
        if (local_18 == 0) {
          *(undefined4 **)((int)ppuVar4 + -0x10) = local_14;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x80499c7;
          FUN_0807daf0();
          *(code **)((int)ppuVar4 + -0xc) = FUN_080497d5;
          *(undefined4 *)((int)ppuVar4 + -0x10) = 2;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x80499db;
          FUN_08050e20();
          *(undefined4 *)((int)ppuVar4 + -0xc) = 0;
          *(int *)((int)ppuVar4 + -0x10) = DAT_081106dc;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x80499ef;
          FUN_0807dbc0();
          *(undefined4 *)((int)ppuVar4 + -0xc) = 1;
          *(int *)((int)ppuVar4 + -0x10) = DAT_081106dc;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a03;
          FUN_0807dbc0();
          *(undefined4 *)((int)ppuVar4 + -0xc) = 2;
          *(int *)((int)ppuVar4 + -0x10) = DAT_081106dc;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a17;
          FUN_0807dbc0();
          *(undefined4 *)((int)ppuVar4 + -0x10) = 0;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a24;
          uVar2 = FUN_0807b6e0();
          *(undefined4 *)((int)ppuVar4 + -0x10) = uVar2;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a30;
          FUN_080523b0();
          *(undefined4 *)((int)ppuVar4 + -4) = 0x8049a38;
          FUN_08049c8e();
          *(int *)((int)ppuVar4 + -0x10) = DAT_081106dc;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a47;
          FUN_0807daf0();
          *(undefined4 *)((int)ppuVar4 + -0x10) = 0;
          *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a54;
          FUN_08051650();
          ppuVar4 = (undefined4 **)((int)ppuVar4 + -0x10);
        }
        *(int *)((int)ppuVar4 + -0x10) = DAT_081106dc;
        *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a63;
        FUN_0807daf0();
        *(undefined4 *)((int)ppuVar4 + -4) = 0x8049a6b;
        iVar3 = FUN_0807bac0();
      } while (iVar3 != 0);
      *(undefined4 *)((int)ppuVar4 + -0x10) = 0x1e;
      *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a7d;
      FUN_0807b920();
      *(undefined4 *)((int)ppuVar4 + -0xc) = 2;
      *(int *)((int)ppuVar4 + -0x10) = local_18;
      *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a8d;
      FUN_08051110();
      *(undefined4 *)((int)ppuVar4 + -0x10) = 0;
      *(undefined4 *)((int)ppuVar4 + -0x14) = 0x8049a9a;
      uVar2 = FUN_08051650();
    }
  }
  return uVar2;
}

void FUN_0804b230(undefined4 param_1,int param_2,int param_3)

{
  undefined *puVar1;
  code **ppcVar2;
  undefined4 *puVar3;
  uint *puVar4;
  char cVar5;
  uint uVar6;
  code *pcVar7;
  undefined4 uVar8;
  byte bVar9;
  int iVar10;
  int extraout_ECX;
  int iVar11;
  int extraout_EDX;
  int *piVar12;
  undefined4 uVar13;
  uint uVar14;
  undefined *puVar15;
  undefined4 uVar16;
  uint uVar17;
  Elf32_Rel *pEVar18;
  int in_GS_OFFSET;
  undefined4 param_7;
  int *apiStackY_b0 [3];
  int aiStackY_a4 [2];
  int *apiStack_98 [3];
  undefined auStack_8c [8];
  int *local_84;
  uint local_80 [16];
  int local_40 [12];
  
  DAT_0811344c = (int *)(param_3 + 4 + param_2 * 4);
  DAT_0810ed10 = param_7;
  piVar12 = DAT_0811344c;
  do {
    iVar10 = *piVar12;
    piVar12 = piVar12 + 1;
  } while (iVar10 != 0);
  FUN_08082210(piVar12);
  FUN_08081620(DAT_0811344c);
  local_80[13] = 0;
  local_80[14] = 0;
  local_80[15] = 0;
  puVar3 = (undefined4 *)cpuid_basic_info(0);
  DAT_08113504 = *puVar3;
  piVar12 = (int *)puVar3[1];
  iVar11 = puVar3[2];
  iVar10 = puVar3[3];
  if ((piVar12 != (int *)0x756e6547) || (iVar10 != 0x6c65746e)) {
    puVar15 = auStack_8c;
    if (piVar12 != (int *)0x68747541) goto LAB_0804bac8;
    puVar15 = auStack_8c;
    if (iVar10 != 0x444d4163) goto LAB_0804bac8;
    puVar15 = auStack_8c;
    puVar1 = auStack_8c;
    if (iVar11 == 0x69746e65) goto LAB_0804baec;
    goto LAB_0804b389;
  }
  puVar15 = auStack_8c;
  if (iVar11 != 0x49656e69) goto LAB_0804b389;
  piVar12 = local_40 + 7;
  FUN_0804a3d0(local_80 + 0xf);
  FUN_0804a340();
  FUN_0804ad50();
  puVar15 = auStack_8c;
  if (local_80[13] != 6) goto LAB_0804b30e;
  local_80[14] = local_40[7] + local_80[14];
  cVar5 = (char)local_80[14];
  if (local_80[14] < 0x38) {
    if (local_80[14] < 0x1a) {
      if ((DAT_0811351f & 0x10) != 0) {
LAB_0804bfe5:
        _DAT_08113634 = _DAT_08113634 | 0x39;
      }
    }
    else {
      uVar14 = 1 << (cVar5 - 0x1aU & 0x1f);
      if ((uVar14 & 0x340831) != 0) goto LAB_0804bfe5;
      if ((uVar14 & 0x1004) == 0) {
        if (local_80[14] == 0x37) {
          _DAT_08113634 = _DAT_08113634 | 0x138;
        }
        else if ((DAT_0811351f & 0x10) != 0) {
LAB_0804c151:
          _DAT_08113634 = _DAT_08113634 | 0x39;
          if (local_80[14] < 0x5f) goto LAB_0804c02b;
          goto LAB_0804c089;
        }
      }
      else {
        _DAT_08113634 = _DAT_08113634 | 4;
      }
    }
    goto LAB_0804b30e;
  }
  if (local_80[14] < 0x9d) {
    if (0x85 < local_80[14]) {
      if ((0x410001U >> (cVar5 + 0x7aU & 0x1f) & 1) != 0) {
        _DAT_08113634 = _DAT_08113634 | 0x139;
        goto LAB_0804c089;
      }
      goto LAB_0804c078;
    }
    if (0x5a < local_80[14]) {
      if ((0x1e < local_80[14] - 0x5c) ||
         ((0x4200000bU >> ((byte)(local_80[14] - 0x5c) & 0x1f) & 1) == 0)) {
        if ((DAT_0811351f & 0x10) == 0) {
          if (0x5e < local_80[14]) goto LAB_0804b30e;
        }
        else {
          _DAT_08113634 = _DAT_08113634 | 0x39;
          if (0x5e < local_80[14]) goto LAB_0804c089;
        }
        goto LAB_0804c034;
      }
      _DAT_08113634 = _DAT_08113634 | 0x138;
      if (local_80[14] < 0x5f) goto LAB_0804c034;
      goto LAB_0804c089;
    }
    if (local_80[14] < 0x4a) {
      if ((DAT_0811351f & 0x10) != 0) {
        _DAT_08113634 = _DAT_08113634 | 0x39;
      }
LAB_0804c02b:
      if (local_80[14] < 0x3c) goto LAB_0804b30e;
    }
    else if ((0x1200dU >> (cVar5 + 0xb6U & 0x1f) & 1) == 0) {
      if ((DAT_0811351f & 0x10) != 0) goto LAB_0804c151;
    }
    else {
      _DAT_08113634 = _DAT_08113634 | 0x138;
    }
LAB_0804c034:
    switch(local_80[14]) {
    case 0x3c:
    case 0x45:
    case 0x46:
code_r0x0804c054:
      _DAT_08113548 = _DAT_08113548 & 0xfffff7ff;
      break;
    case 0x3f:
      if (local_80[15] < 4) goto code_r0x0804c054;
      break;
    case 0x4e:
    case 0x5e:
      goto code_r0x0804c0a1;
    case 0x55:
      if (local_80[15] < 6) goto code_r0x0804c0a1;
    }
  }
  else {
LAB_0804c078:
    if ((DAT_0811351f & 0x10) != 0) {
      _DAT_08113634 = _DAT_08113634 | 0x39;
    }
LAB_0804c089:
    if (((local_80[14] & 0xffffffef) == 0x8e) && (local_80[15] < 0xd)) {
code_r0x0804c0a1:
      _DAT_08113548 = _DAT_08113548 & 0xfffff7ef;
      _DAT_08113550 = _DAT_08113550 | 0x800;
    }
  }
LAB_0804b30e:
  if ((DAT_0811353b & 8) == 0) {
    if ((DAT_081135d4 & 0x10) == 0) {
      _DAT_08113634 = _DAT_08113634 | 0x1000;
    }
    if ((_DAT_08113548 & 0x800) == 0) goto LAB_0804b33b;
  }
  _DAT_08113634 = _DAT_08113634 | 0x400;
LAB_0804b33b:
  if ((DAT_08113540 & 0x10) != 0) {
    _DAT_08113634 = _DAT_08113634 | 0x8000;
  }
  DAT_08113500 = 1;
  local_84 = local_40 + 5;
  DAT_08113510 = local_80[15];
  DAT_0811350c = local_80[14];
  uVar14 = local_80[13];
LAB_0804b3be:
  do {
    if ((DAT_08113520 & 0x100) != 0) {
      _DAT_08113634 = _DAT_08113634 | 0x40;
    }
    if ((DAT_08113520 & 0x8000) != 0) {
      _DAT_08113634 = _DAT_08113634 | 0x80;
    }
    *(undefined4 *)(puVar15 + 0x4c) = 0xffffffff;
    *(undefined4 *)(puVar15 + 0x50) = 0xffffffff;
    *(undefined4 *)(puVar15 + 0x54) = 0;
    DAT_08113508 = uVar14;
    if (DAT_08113500 == 1) {
      *(undefined4 *)(puVar15 + -4) = 0x804bb61;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0xc) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bb6f;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + -4) = 0x804bb7b;
      uVar16 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x4c) = uVar16;
      *(undefined4 *)(puVar15 + 0x50) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804bb8f;
      uVar8 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x14) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bb9d;
      uVar8 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x1c) = uVar8;
      *(undefined4 *)(puVar15 + 0x20) = *(undefined4 *)(puVar15 + 0xc);
      *(undefined4 *)(puVar15 + -4) = 0x804bbb3;
      uVar8 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x24) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bbc1;
      uVar8 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x18) = uVar13;
      *(undefined4 *)(puVar15 + 0x28) = uVar8;
      *(undefined4 *)(puVar15 + 0x2c) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bbd7;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x30) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bbe5;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x10) = uVar16;
      *(undefined4 *)(puVar15 + 0x34) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bbf7;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + 0x38) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bc05;
      uVar13 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + -4) = 0x804bc11;
      uVar16 = FUN_0804ac40();
      *(undefined4 *)(puVar15 + -0x10) = *(undefined4 *)(puVar15 + 0x18);
      *(undefined4 *)(puVar15 + -0x14) = 0x804bc2b;
      FUN_0804a580();
    }
    else if (DAT_08113500 == 3) {
      *(undefined4 *)(puVar15 + -4) = 0x804bcf3;
      uVar13 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0xc) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bd01;
      uVar16 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x18) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804bd11;
      uVar13 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x4c) = uVar13;
      *(undefined4 *)(puVar15 + 0x50) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bd25;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x14) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bd33;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x1c) = uVar8;
      *(undefined4 *)(puVar15 + 0x20) = *(undefined4 *)(puVar15 + 0xc);
      *(undefined4 *)(puVar15 + -4) = 0x804bd49;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x24) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bd57;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x2c) = uVar16;
      *(undefined4 *)(puVar15 + 0x28) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bd69;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x30) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bd77;
      uVar8 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x10) = uVar13;
      *(undefined4 *)(puVar15 + 0x34) = uVar8;
      *(undefined4 *)(puVar15 + -4) = 0x804bd89;
      uVar13 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + 0x38) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bd97;
      uVar13 = FUN_08049fe0();
      *(undefined4 *)(puVar15 + -0x10) = uVar16;
      uVar16 = 0xffffffff;
      *(undefined4 *)(puVar15 + -0x14) = 0x804bdb1;
      FUN_0804a580();
    }
    else if (DAT_08113500 == 2) {
      *(undefined4 *)(puVar15 + -4) = 0x804bdc3;
      uVar13 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0xc) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bdd1;
      uVar13 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x18) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bddf;
      uVar13 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x14) = uVar13;
      *(undefined4 *)(puVar15 + 0x4c) = uVar13;
      *(undefined4 *)(puVar15 + 0x50) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804bdf7;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x1c) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be05;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x20) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be13;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x24) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be21;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x28) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be2f;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x30) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be3d;
      uVar16 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x10) = uVar13;
      *(undefined4 *)(puVar15 + 0x34) = uVar16;
      *(undefined4 *)(puVar15 + -4) = 0x804be4f;
      uVar13 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x38) = uVar13;
      *(undefined4 *)(puVar15 + -4) = 0x804be5d;
      uVar13 = FUN_0804a120();
      *(undefined4 *)(puVar15 + 0x3c) = uVar13;
      puVar4 = (uint *)cpuid(0x80000000);
      if (*(int *)(puVar15 + 0x10) < 1) {
        iVar10 = *(int *)(puVar15 + 0x18);
        *(int *)(puVar15 + 0x4c) = iVar10;
      }
      else {
        if (*puVar4 < 0x80000008) {
LAB_0804beba:
          iVar10 = cpuid_Version_info(1);
          if ((*(uint *)(iVar10 + 8) & 0x10000000) != 0) {
            *(uint *)(puVar15 + 0x54) = *(uint *)(iVar10 + 4) >> 0x10 & 0xff;
          }
          if (*(uint *)(puVar15 + 0x54) != 0) {
            *(uint *)(puVar15 + 0x50) = *(uint *)(puVar15 + 0x14) / *(uint *)(puVar15 + 0x54);
          }
          *(undefined4 *)(puVar15 + 0x2c) = *(undefined4 *)(puVar15 + 0x50);
          if (0x16 < uVar14) {
            puVar4 = (uint *)cpuid(0x8000001d);
            iVar10 = ((*puVar4 >> 0xe & 0xfff) + 1) * *(int *)(puVar15 + 0x2c);
            goto LAB_0804bf56;
          }
        }
        else {
          iVar10 = cpuid(0x80000008);
          bVar9 = (byte)(*(uint *)(iVar10 + 0xc) >> 0xc) & 0xf;
          *(int *)(puVar15 + 0x54) = 1 << bVar9;
          if (0x16 < uVar14) goto LAB_0804beba;
          *(uint *)(puVar15 + 0x2c) = *(uint *)(puVar15 + 0x14) >> bVar9;
        }
        *(int *)(puVar15 + 0x4c) = *(int *)(puVar15 + 0x14) + *(int *)(puVar15 + 0x18);
        iVar10 = *(int *)(puVar15 + 0x2c) + *(int *)(puVar15 + 0x18);
      }
LAB_0804bf56:
      uVar13 = *(undefined4 *)(puVar15 + 0x3c);
      *(int *)(puVar15 + 0x50) = iVar10;
      uVar16 = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x14) = *(undefined4 *)(puVar15 + 0x1c);
      *(undefined4 *)(puVar15 + 0x1c) = *(undefined4 *)(puVar15 + 0x20);
      *(undefined4 *)(puVar15 + 0x20) = *(undefined4 *)(puVar15 + 0xc);
      *(undefined4 *)(puVar15 + 0x2c) = *(undefined4 *)(puVar15 + 0x18);
    }
    else {
      *(undefined4 *)(puVar15 + 0x38) = 0xffffffff;
      uVar16 = 0xffffffff;
      uVar13 = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x10) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x34) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x30) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x2c) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x28) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x24) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x20) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x1c) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x14) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0x18) = 0xffffffff;
      *(undefined4 *)(puVar15 + 0xc) = 0xffffffff;
    }
    DAT_0811365c = *(undefined4 *)(puVar15 + 0x14);
    DAT_08113660 = *(undefined4 *)(puVar15 + 0x1c);
    iVar10 = *(int *)(puVar15 + 0x50) * 3;
    DAT_08113664 = *(undefined4 *)(puVar15 + 0x20);
    iVar11 = iVar10 + 3;
    if (-1 < iVar10) {
      iVar11 = iVar10;
    }
    DAT_08113668 = *(undefined4 *)(puVar15 + 0x24);
    uVar14 = iVar11 >> 2;
    DAT_0811366c = *(undefined4 *)(puVar15 + 0x28);
    DAT_08113670 = *(undefined4 *)(puVar15 + 0x2c);
    DAT_08113674 = *(undefined4 *)(puVar15 + 0x30);
    DAT_08113678 = *(undefined4 *)(puVar15 + 0x34);
    DAT_0811367c = *(undefined4 *)(puVar15 + 0x10);
    DAT_08113680 = *(undefined4 *)(puVar15 + 0x38);
    if (((_DAT_08113548 & 0x200) != 0) && (uVar14 < (uint)(*(int *)(puVar15 + 0x4c) / 4))) {
      uVar14 = *(int *)(puVar15 + 0x4c) / 4;
    }
    if (((_DAT_08113548 & 0x10000) == 0) || ((_DAT_08113634 & 0x1000) != 0)) {
      uVar17 = (-(uint)((_DAT_08113634 & 0x200) == 0) & 0xffffe800) + 0x2000;
      *(uint *)(puVar15 + 0x14) = (-(uint)((_DAT_08113634 & 0x200) == 0) & 0xffffff80) + 0x100;
    }
    else {
      *(undefined4 *)(puVar15 + 0x14) = 0x200;
      uVar17 = 0x4000;
    }
    if ((_DAT_08113550 & 0x10) != 0) {
      uVar17 = 0x840;
    }
    *(undefined4 *)(puVar15 + -8) = 0;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 0x1d;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b572;
    DAT_08113684 = uVar13;
    DAT_08113688 = uVar16;
    FUN_08081d50();
    iVar10 = *(int *)(puVar15 + 0x68);
    if (iVar10 == 0) {
      iVar10 = *(int *)(puVar15 + 0xc);
    }
    *(int *)(puVar15 + 0xc) = iVar10;
    *(undefined4 *)(puVar15 + -8) = 0;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 4;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b58e;
    FUN_08081d50();
    if (*(int *)(puVar15 + 0x68) != 0) {
      *(int *)(puVar15 + 0x4c) = *(int *)(puVar15 + 0x68);
    }
    *(undefined4 *)(puVar15 + -8) = 0;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 0x10;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b5aa;
    FUN_08081d50();
    uVar6 = *(uint *)(puVar15 + 0x68);
    if (0xfffbfbe < uVar6 - 0x4041) {
      uVar6 = 0xfffffff;
      if (uVar14 < 0x10000000) {
        uVar6 = uVar14;
      }
      if (uVar6 < 0x4040) {
        uVar6 = 0x4040;
      }
    }
    *(uint *)(puVar15 + 0x1c) = uVar6;
    *(undefined4 *)(puVar15 + -8) = 0;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 10;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b5e4;
    FUN_08081d50();
    *(undefined4 *)(puVar15 + -8) = 0;
    *(int **)(puVar15 + -0xc) = piVar12;
    if (*(uint *)(puVar15 + 0x14) < *(uint *)(puVar15 + 0x68)) {
      uVar17 = *(uint *)(puVar15 + 0x68);
    }
    *(undefined4 *)(puVar15 + -0x10) = 0xf;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b5fc;
    FUN_08081d50();
    uVar13 = *(undefined4 *)(puVar15 + 0x68);
    *(undefined4 *)(puVar15 + 0x60) = 0xffffffff;
    *(undefined4 *)(puVar15 + 100) = 0;
    *(int *)(puVar15 + 0x68) = *(int *)(puVar15 + 0xc);
    *(undefined4 *)(puVar15 + 0x10) = uVar13;
    *(int *)(puVar15 + 0x6c) = *(int *)(puVar15 + 0xc) >> 0x1f;
    *(undefined4 *)(puVar15 + 0x58) = 0;
    *(undefined4 *)(puVar15 + 0x5c) = 0;
    *(undefined4 *)(puVar15 + -0x14) = *(undefined4 *)(puVar15 + 8);
    puVar1 = puVar15 + 0x58;
    *(undefined **)(puVar15 + -0x18) = puVar1;
    *(int **)(puVar15 + -0x1c) = piVar12;
    *(undefined4 *)(puVar15 + -0x20) = 0x1d;
    *(undefined4 *)(puVar15 + -0x24) = 0x804b644;
    FUN_080815f0();
    iVar10 = *(int *)(puVar15 + 0x4c);
    *(undefined4 *)(puVar15 + 0x60) = 0xffffffff;
    *(undefined4 *)(puVar15 + 100) = 0;
    *(int *)(puVar15 + 0x68) = iVar10;
    *(int *)(puVar15 + 0x20) = iVar10;
    *(int *)(puVar15 + 0x6c) = iVar10 >> 0x1f;
    *(undefined4 *)(puVar15 + 0x58) = 0;
    *(undefined4 *)(puVar15 + 0x5c) = 0;
    *(undefined4 *)(puVar15 + -4) = *(undefined4 *)(puVar15 + 8);
    *(undefined **)(puVar15 + -8) = puVar1;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 4;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b695;
    FUN_080815f0();
    *(undefined4 *)(puVar15 + 0x60) = 0xfffffff;
    *(undefined4 *)(puVar15 + 100) = 0;
    *(undefined4 *)(puVar15 + 0x68) = *(undefined4 *)(puVar15 + 0x1c);
    *(undefined4 *)(puVar15 + 0x58) = 0x4040;
    *(undefined4 *)(puVar15 + 0x5c) = 0;
    *(undefined4 *)(puVar15 + 0x6c) = 0;
    *(undefined4 *)(puVar15 + -0x14) = *(undefined4 *)(puVar15 + 8);
    *(undefined **)(puVar15 + -0x18) = puVar1;
    *(int **)(puVar15 + -0x1c) = piVar12;
    *(undefined4 *)(puVar15 + -0x20) = 0x10;
    *(undefined4 *)(puVar15 + -0x24) = 0x804b6d2;
    FUN_080815f0();
    *(undefined4 *)(puVar15 + 0x60) = 0xffffffff;
    *(undefined4 *)(puVar15 + 100) = 0;
    *(undefined4 *)(puVar15 + 0x58) = *(undefined4 *)(puVar15 + 0x14);
    *(undefined4 *)(puVar15 + 0x5c) = 0;
    *(uint *)(puVar15 + 0x68) = uVar17;
    *(undefined4 *)(puVar15 + 0x6c) = 0;
    *(undefined4 *)(puVar15 + -4) = *(undefined4 *)(puVar15 + 8);
    *(undefined **)(puVar15 + -8) = puVar1;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 10;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b71a;
    FUN_080815f0();
    *(undefined4 *)(puVar15 + 0x60) = 0xffffffff;
    *(undefined4 *)(puVar15 + 100) = 0;
    *(undefined4 *)(puVar15 + 0x58) = 1;
    *(undefined4 *)(puVar15 + 0x5c) = 0;
    *(undefined4 *)(puVar15 + 0x68) = *(undefined4 *)(puVar15 + 0x10);
    *(undefined4 *)(puVar15 + 0x6c) = 0;
    *(undefined4 *)(puVar15 + -0x14) = *(undefined4 *)(puVar15 + 8);
    *(undefined **)(puVar15 + -0x18) = puVar1;
    *(int **)(puVar15 + -0x1c) = piVar12;
    *(undefined4 *)(puVar15 + -0x20) = 0xf;
    *(undefined4 *)(puVar15 + -0x24) = 0x804b757;
    FUN_080815f0();
    DAT_0811364c = *(undefined4 *)(puVar15 + 0x1c);
    DAT_08113648 = *(uint *)(puVar15 + 0x20);
    DAT_08113644 = *(uint *)(puVar15 + 0xc);
    DAT_08113654 = *(undefined4 *)(puVar15 + 0x18);
    if (DAT_08113500 != 2) {
      DAT_08113654 = DAT_0811364c;
    }
    DAT_08113658 = *(undefined4 *)(puVar15 + 0x10);
    *(code **)(puVar15 + -8) = FUN_08082e90;
    *(int **)(puVar15 + -0xc) = piVar12;
    *(undefined4 *)(puVar15 + -0x10) = 0x19;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b7ab;
    DAT_08113650 = uVar17;
    FUN_08081d50();
    if ((_DAT_0811352c & 0x8000000) == 0) {
      _DAT_0811352c = _DAT_0811352c & 0xfbffffff;
      DAT_08113584 = DAT_08113584 & 0xffffffe8;
LAB_0804b7d4:
      _DAT_0811352c = _DAT_0811352c & 0xcfffefff;
      _DAT_08113548 = _DAT_08113548 & 0x23dcffdf;
      DAT_0811354c = DAT_0811354c & 0xffffa1bd;
      DAT_081135e4 = DAT_081135e4 & 0xffffffcf;
      _DAT_08113550 = _DAT_08113550 & 0xfc3ffef3;
      DAT_0811356c = DAT_0811356c & 0xfffef7ff;
      DAT_0811363c = 0;
    }
    else if ((DAT_08113584 & 2 | _DAT_0811352c & 0x4000000) == 0) goto LAB_0804b7d4;
    DAT_081134cc = 0;
    DAT_081134c8 = (uint)((DAT_08113533 & 4) != 0);
    if ((_DAT_08113634 & 0x80) == 0) {
      if ((_DAT_08113634 & 0x40) != 0) {
        DAT_081136c0 = &DAT_080d646f;
      }
    }
    else {
      DAT_081136c0 = &DAT_080d646a;
    }
    uVar14 = DAT_08113644 & 0xffffff00;
    if (0 < (int)uVar14) {
      DAT_0810f394 = (int)uVar14 >> 1;
      DAT_0810f390 = uVar14;
    }
    uVar14 = DAT_08113648 & 0xffffff00;
    if (0 < (int)uVar14) {
      DAT_0810f38c = (int)uVar14 >> 1;
      DAT_0810f388 = uVar14;
    }
    DAT_081106e8 = DAT_0811364c;
    DAT_0810f384 = DAT_08113650;
    DAT_0810f380 = DAT_08113658;
    DAT_081106e4 = DAT_08113654;
    if ((_DAT_08113634 & 0x8000) != 0) {
      DAT_081106e0 = DAT_081106e0 | 1;
    }
    *(undefined4 *)(puVar15 + -4) = 0x804b8db;
    FUN_080496a0();
    pEVar18 = Elf32_Rel_ARRAY_08048178;
    do {
      ppcVar2 = (code **)pEVar18->r_offset;
      if (*(char *)&pEVar18->r_info != '*') {
        *(char **)(puVar15 + -0x10) = "Unexpected reloc type in static binary.\n";
                    /* WARNING: Subroutine does not return */
        *(undefined **)(puVar15 + -0x14) = &UNK_0804b914;
        FUN_08063160();
      }
      pcVar7 = *ppcVar2;
      *(undefined4 *)(puVar15 + -4) = 0x804b8f3;
      pcVar7 = (code *)(*pcVar7)();
      pEVar18 = pEVar18 + 1;
      *ppcVar2 = pcVar7;
    } while (pEVar18 < (Elf32_Rel *)0x80481f0);
    *(undefined4 *)(puVar15 + -4) = 0x804b97a;
    FUN_0804c330();
    puVar4 = DAT_0810ed08;
    *(uint *)(in_GS_OFFSET + 0x14) = *DAT_0810ed08 & 0xffffff00;
    *(uint *)(in_GS_OFFSET + 0x18) = puVar4[1];
    if (*(int *)(puVar15 + 0xa4) != 0) {
      *(uint **)(puVar15 + -4) = puVar4;
      *(undefined4 *)(puVar15 + -8) = 0;
      *(undefined4 *)(puVar15 + -0xc) = 0;
      *(undefined4 *)(puVar15 + -0x10) = *(undefined4 *)(puVar15 + 0xa4);
      *(undefined4 *)(puVar15 + -0x14) = 0x804b9c4;
      FUN_08051330();
    }
    *(undefined4 *)(puVar15 + -0x10) = 1;
    *(undefined4 *)(puVar15 + -0x14) = 0x804b9d1;
    FUN_080839f0();
    *(int **)(puVar15 + -8) = DAT_0811344c;
    *(undefined4 *)(puVar15 + -0xc) = *(undefined4 *)(puVar15 + 0x98);
    *(undefined4 *)(puVar15 + -0x10) = *(undefined4 *)(puVar15 + 0x94);
    *(undefined4 *)(puVar15 + -0x14) = 0x804b9ed;
    FUN_08083ac0();
    *(undefined4 *)(puVar15 + -8) = 0;
    *(undefined4 *)(puVar15 + -0xc) = 0;
    *(code **)(puVar15 + -0x10) = FUN_08049fa0;
    *(undefined4 *)(puVar15 + -0x14) = 0x804ba00;
    FUN_08051330();
    if (DAT_0811008c != 0) {
      *(undefined4 *)(puVar15 + -4) = 0x804bfb9;
      FUN_0804c300();
    }
    piVar12 = DAT_0811344c;
    *(undefined4 *)(puVar15 + -4) = 0x804ba60;
    FUN_08049000();
    iVar10 = 0;
    do {
      *(int **)(puVar15 + -8) = piVar12;
      *(undefined4 *)(puVar15 + -0xc) = *(undefined4 *)(puVar15 + 0x98);
      *(undefined4 *)(puVar15 + -0x10) = *(undefined4 *)(puVar15 + 0x94);
      pcVar7 = (code *)(&PTR_FUN_0810cbd8)[iVar10];
      *(undefined4 *)(puVar15 + -0x14) = 0x804ba99;
      uVar13 = (*pcVar7)();
      iVar10 = iVar10 + 1;
    } while (iVar10 == 0);
    *(undefined4 *)(puVar15 + -4) = uVar13;
    *(undefined4 *)(puVar15 + -8) = uVar13;
    *(undefined4 *)(puVar15 + -0xc) = 0;
    *(undefined4 *)(puVar15 + -0x10) = 0;
    *(undefined4 *)(puVar15 + -0x14) = 0x804baae;
    FUN_080807c0();
    *(undefined4 *)(puVar15 + -0x14) = 0x804bac8;
    FUN_0804a2a0();
    iVar10 = extraout_ECX;
    iVar11 = extraout_EDX;
    puVar15 = puVar15 + -0x10;
LAB_0804bac8:
    if ((piVar12 != (int *)0x6f677948) || (iVar10 != 0x656e6975)) {
      if ((piVar12 == (int *)0x746e6543) && (iVar10 == 0x736c7561)) {
        if (iVar11 != 0x48727561) {
LAB_0804b389:
          *(undefined4 *)(puVar15 + -0x10) = 0;
          *(undefined4 *)(puVar15 + -0x14) = 0x804b399;
          FUN_0804a3d0();
          *(undefined4 *)(puVar15 + -0x14) = 0x804b39e;
          FUN_0804ad50();
          DAT_0811350c = *(uint *)(puVar15 + 0x44);
          DAT_08113510 = *(uint *)(puVar15 + 0x48);
          uVar14 = *(uint *)(puVar15 + 0x40);
          DAT_08113500 = 4;
          piVar12 = (int *)(puVar15 + 0x68);
          *(undefined **)(puVar15 + 8) = puVar15 + 0x60;
          goto LAB_0804b3be;
        }
      }
      else if ((piVar12 != (int *)0x68532020 || iVar10 != 0x20206961) || (iVar11 != 0x68676e61))
      goto LAB_0804b389;
      *(undefined **)(puVar15 + 8) = puVar15 + 0x60;
      piVar12 = (int *)(puVar15 + 0x68);
      *(int **)(puVar15 + -0x10) = piVar12;
      *(undefined4 *)(puVar15 + -0x14) = 0x804bca8;
      FUN_0804a3d0();
      *(undefined4 *)(puVar15 + -0x14) = 0x804bcad;
      FUN_0804a340();
      *(undefined4 *)(puVar15 + -0x14) = 0x804bcb2;
      FUN_0804ad50();
      uVar14 = *(uint *)(puVar15 + 0x40);
      iVar10 = *(int *)(puVar15 + 0x60) + *(int *)(puVar15 + 0x44);
      *(int *)(puVar15 + 0x44) = iVar10;
      if (uVar14 == 6) {
        if ((iVar10 == 0xf) || (iVar10 == 0x19)) {
LAB_0804bf26:
          _DAT_08113548 = _DAT_08113548 & 0xffffffdf;
          _DAT_0811352c = _DAT_0811352c & 0xefffffff;
          _DAT_08113634 = _DAT_08113634 & 0xfffffdff | 0x100;
        }
      }
      else if (uVar14 == 7) {
        if (iVar10 == 0x1b) goto LAB_0804bf26;
        if (iVar10 == 0x3b) {
          _DAT_0811352c = _DAT_0811352c & 0xefffffff;
          _DAT_08113548 = _DAT_08113548 & 0xffffffdf;
          _DAT_08113634 = _DAT_08113634 & 0xfffffdff;
        }
      }
      DAT_0811350c = *(uint *)(puVar15 + 0x44);
      DAT_08113510 = *(uint *)(puVar15 + 0x48);
      DAT_08113500 = 3;
      goto LAB_0804b3be;
    }
    puVar1 = puVar15;
    if (iVar11 != 0x6e65476e) goto LAB_0804b389;
LAB_0804baec:
    puVar15 = puVar1;
    piVar12 = (int *)(puVar15 + 0x68);
    *(undefined **)(puVar15 + -0x10) = puVar15 + 0x48;
    *(undefined4 *)(puVar15 + -0x14) = 0x804bb07;
    FUN_0804a3d0();
    *(undefined4 *)(puVar15 + -0x14) = 0x804bb0c;
    FUN_0804a340();
    *(undefined4 *)(puVar15 + -0x14) = 0x804bb11;
    FUN_0804ad50();
    if ((_DAT_0811352c & 0x10000000) != 0) {
      DAT_0811356c = DAT_0811356c | DAT_0811355c & 0x10000;
    }
    DAT_0811350c = *(uint *)(puVar15 + 0x44);
    if ((*(int *)(puVar15 + 0x40) == 0x15) && (DAT_0811350c - 0x60 < 0x20)) {
      _DAT_08113634 = _DAT_08113634 & 0xfffffdff | 10;
    }
    DAT_08113510 = *(uint *)(puVar15 + 0x48);
    uVar14 = *(uint *)(puVar15 + 0x40);
    DAT_08113500 = 2;
    *(undefined **)(puVar15 + 8) = puVar15 + 0x60;
  } while( true );
}

void FUN_08049670(void)

{
  FUN_0804b230(FUN_08049803);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

Start the script, create a dump file and laucnh strings on it, we can see: 

```
Looser ! (The game is closed)
Your win ! Congratulation
```

In Ida free search `Congratulation`:

```
.text:080C0E27
.text:080C0EFC
.text:080C13A3
.text:080C13E9
.text:080C1698
.text:080C1AE7
.text:080C2523
.text:080C256F
.text:080C57C5
.data:0810F254
```

In Ida free search `Looser`:

```
.data:0810F2B8
```

and search references to the precedent address:

```
.text:08049F74
```

In graph view we can see:

```
.text:08049F3B
jmp     edx             ; switch jump
```

 - Case 0: `.text:08049F3D`
 - Case 1: `.text:08049F48`
 - Case 2: `.text:08049F53`
 - Case 4: `.text:08049F5E`
 - Case 5: `.text:08049F69`
 - Case 6: `.text:08049F74`
 - Case 3: `.text:08049F7F`

In all cases:
 - move an address in `eax` (different for each cases)
 - move `eax` address to `ebp-4`
 - go to `.text:08049F89`

In `.text:08049F89`:
 - move `ebp-4` address to `eax`
 - return (address in `eax`)

Return to the function start, we can see:
 - call a function (`8049F8E`)
 - the switch condition on global variable value

```
.text:08049F0D ; =============== S U B R O U T I N E =======================================
.text:08049F0D
.text:08049F0D ; Attributes: bp-based frame
.text:08049F0D
.text:08049F0D sub_8049F0D     proc near               ; CODE XREF: sub_8049C8E+26↑p
.text:08049F0D                                         ; sub_8049C8E+5A↑p ...
.text:08049F0D
.text:08049F0D var_4           = dword ptr -4
.text:08049F0D arg_0           = dword ptr  8
.text:08049F0D
.text:08049F0D ; __unwind {
.text:08049F0D                 push    ebp
.text:08049F0E                 mov     ebp, esp
.text:08049F10                 sub     esp, 10h
.text:08049F13                 call    sub_8049F8E
.text:08049F18                 add     eax, (offset tbyte_810EFF4 - $)
.text:08049F1D                 lea     edx, [eax+6Ch]  ; "GH{R3v3rs3_1s_s1mpl3}"
.text:08049F23                 mov     [ebp-4], edx
.text:08049F26                 cmp     dword ptr [ebp+8], 6 ; switch 7 cases
.text:08049F2A                 ja      short def_8049F3B ; jumptable 08049F3B default case
.text:08049F2C                 mov     edx, [ebp+8]
.text:08049F2F                 shl     edx, 2
.text:08049F32                 mov     edx, ds:(jpt_8049F3B - 810EFF4h)[edx+eax]
.text:08049F39                 add     edx, eax
.text:08049F3B                 jmp     edx             ; switch jump
.text:08049F3D ; ---------------------------------------------------------------------------
.text:08049F3D
.text:08049F3D loc_8049F3D:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F3D                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F3D                 lea     eax, [eax+0D0h] ; jumptable 08049F3B case 0
.text:08049F43                 mov     [ebp-4], eax
.text:08049F46                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F48 ; ---------------------------------------------------------------------------
.text:08049F48
.text:08049F48 loc_8049F48:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F48                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F48                 lea     eax, [eax+134h] ; jumptable 08049F3B case 1
.text:08049F4E                 mov     [ebp-4], eax
.text:08049F51                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F53 ; ---------------------------------------------------------------------------
.text:08049F53
.text:08049F53 loc_8049F53:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F53                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F53                 lea     eax, [eax+198h] ; jumptable 08049F3B case 2
.text:08049F59                 mov     [ebp-4], eax
.text:08049F5C                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F5E ; ---------------------------------------------------------------------------
.text:08049F5E
.text:08049F5E loc_8049F5E:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F5E                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F5E                 lea     eax, [eax+1FCh] ; jumptable 08049F3B case 4
.text:08049F64                 mov     [ebp-4], eax
.text:08049F67                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F69 ; ---------------------------------------------------------------------------
.text:08049F69
.text:08049F69 loc_8049F69:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F69                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F69                 lea     eax, [eax+260h] ; jumptable 08049F3B case 5
.text:08049F6F                 mov     [ebp-4], eax
.text:08049F72                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F74 ; ---------------------------------------------------------------------------
.text:08049F74
.text:08049F74 loc_8049F74:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F74                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F74                 lea     eax, [eax+2C4h] ; jumptable 08049F3B case 6
.text:08049F7A                 mov     [ebp-4], eax
.text:08049F7D                 jmp     short def_8049F3B ; jumptable 08049F3B default case
.text:08049F7F ; ---------------------------------------------------------------------------
.text:08049F7F
.text:08049F7F loc_8049F7F:                            ; CODE XREF: sub_8049F0D+2E↑j
.text:08049F7F                                         ; DATA XREF: .rodata:jpt_8049F3B↓o
.text:08049F7F                 lea     eax, [eax+328h] ; jumptable 08049F3B case 3
.text:08049F85                 mov     [ebp-4], eax
.text:08049F88                 nop
.text:08049F89
.text:08049F89 def_8049F3B:                            ; CODE XREF: sub_8049F0D+1D↑j
.text:08049F89                                         ; sub_8049F0D+39↑j ...
.text:08049F89                 mov     eax, [ebp-4]    ; jumptable 08049F3B default case
.text:08049F8C                 leave
.text:08049F8D                 retn
.text:08049F8D ; } // starts at 8049F0D
.text:08049F8D sub_8049F0D     endp
```