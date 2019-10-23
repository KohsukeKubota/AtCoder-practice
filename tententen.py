o, e = input(), input()
s = ''
o_idx = 0
e_idx = 0
i = 0
while o_idx < len(o) or e_idx < len(e):
    if i % 2 == 0:
        s += o[o_idx]
        o_idx += 1
    else:
        s += e[e_idx]
        e_idx += 1
    i += 1
print(s)
