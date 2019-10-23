N = int(input())
XU = [input().split() for _ in range(N)]

res = 0

for xu in XU:
    if xu[1] == 'BTC':
        res += float(xu[0])* 380000
    else:
        res += int(xu[0])

print(res)
