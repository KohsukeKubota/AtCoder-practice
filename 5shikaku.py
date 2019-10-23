n = int(input())
res = 10000
for h in range(1, n+1):
    w = n // h
    val = abs(h-w)+(n-h*w)
    if res > val:
        res = val
print(res)
