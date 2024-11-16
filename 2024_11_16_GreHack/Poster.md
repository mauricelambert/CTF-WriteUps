# Poster

First i check the firsts bytes to identify the type of the file:

```python
>>> open("posterv2.odg", "rb").read(5)
b'PK\x03\x04\n'
>>>
```

I use python to list files, extract the flag and decode it:

```
C:\Users\MauriceLambert\Downloads>python -m zipfile -l posterv2.odg
File Name                                             Modified             Size
meta.xml                                       2024-08-05 18:17:24         1172
mimetype                                       2024-08-05 18:17:24           43
META-INF/                                      2024-11-07 15:08:28            0
META-INF/manifest.xml                          2024-11-07 15:08:28         1168
Thumbnails/                                    2024-11-07 15:08:28            0
Thumbnails/thumbnail.png                       2024-08-05 18:17:24        18238
Pictures/                                      2024-11-07 15:08:28            0
Pictures/10000001000007D0000007D0968D462C.png  2024-08-05 18:17:24       427620
settings.xml                                   2024-08-05 18:17:24        10849
content.xml                                    2024-08-05 18:17:24        12341
styles.xml                                     2024-08-05 18:17:24        19971
Configurations2/                               2024-11-07 15:08:28            0
Configurations2/toolbar/                       2024-08-05 18:17:24            0
Configurations2/floater/                       2024-08-05 18:17:24            0
Configurations2/menubar/                       2024-08-05 18:17:24            0
Configurations2/statusbar/                     2024-08-05 18:17:24            0
Configurations2/accelerator/                   2024-08-05 18:17:24            0
Configurations2/toolpanel/                     2024-08-05 18:17:24            0
Configurations2/images/                        2024-11-07 15:08:28            0
Configurations2/images/Bitmaps/                2024-08-05 18:17:24            0
Configurations2/progressbar/                   2024-08-05 18:17:24            0
Configurations2/popupmenu/                     2024-08-05 18:17:24            0
flag.txt                                       2024-11-07 15:06:46           55

C:\Users\MauriceLambert\Downloads>python -m zipfile -e posterv2.odg ewf

C:\Users\MauriceLambert\Downloads>type ewf\flag.txt
Base64 :
R0h7MHAzbmRvY3VtM243X0BuZF93MHJkX0ByM196MXB9

C:\Users\MauriceLambert\Downloads>python
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from base64 import b64decode
>>> b64decode(b"R0h7MHAzbmRvY3VtM243X0BuZF93MHJkX0ByM196MXB9")
b'GH{0p3ndocum3n7_@nd_w0rd_@r3_z1p}'
>>>
```