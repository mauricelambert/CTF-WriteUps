# Poster Proposal

There are 16 colors in poster background, screenshot the poster, open it in pain, pick color and build the following matrix from 3 bytes colors:

```
71  72  123
67  48  108
111 114 95
104 48  108
100 115 95
49  110 102
48  114 109
97  55  105
49  110 95
102 48  114
95  99  111
109 112 117
55  101 114
95  101 121
51  115 95
40  58  125
```

Write the following python script:

```python
colors = """71  72  123
67  48  108
111 114 95
104 48  108
100 115 95
49  110 102
48  114 109
97  55  105
48  110 95
102 48  114
95  99  111
109 112 117
55  101 114
95  101 121
51  115 95
40  58  125"""
print(*(chr(int(x)) for x in colors.split()), sep="")
```

And get the flag: `GH{C0lor_h0lds_1nf0rma7i0n_f0r_compu7er_ey3s_(:}`