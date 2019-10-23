N = int(input())
res = 1
for i in range(1, N+1):
    if res >= (10**9+7):
        res %= (10**9+7)
        res *= i
    else:
        res *= i
print(res % (10**9+7))
