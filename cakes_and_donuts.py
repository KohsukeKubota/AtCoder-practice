N = int(input())

cnum = 25
dnum = 14

res = 0

for i in range(cnum):
    for j in range(dnum):
        amm = 4 * i + 7 * j
        if amm == N:
            res += 1

if res > 0:
    print('Yes')
else:
    print('No')
