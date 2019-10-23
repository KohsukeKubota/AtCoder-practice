S = input()

res = 0

for s in S:
    if s == '+':
        res += 1
    else:
        res -= 1
print(res)
