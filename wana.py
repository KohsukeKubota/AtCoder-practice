W = input()
res = ''
for w in W:
    if w in set(['a', 'i', 'u', 'e', 'o']):
        pass
    else:
        res += w
print(res)
