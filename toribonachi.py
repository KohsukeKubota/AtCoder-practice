import sys
n = int(input())
a1, a2, a3 = 0, 0, 1
if n == 1: print(a1); sys.exit()
elif n == 2: print(a2); sys.exit()
elif n == 3: print(a3); sys.exit()
res = 0
for i in range(4, n+1):
    res =  a1 + a2 + a3
    if res > 10007: res %= 10007
    a1 = a2
    a2 = a3
    a3 = res
print(res % 10007)
