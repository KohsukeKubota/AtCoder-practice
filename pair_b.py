n = int(input())
res = n % 10**9
if res % 2 == 0:
    print(n-1)
else:
    print(n+1)
