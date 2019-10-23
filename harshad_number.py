N = int(input())

res = 0
num = N

while num > 0:
    q, mod = divmod(num, 10)
    res += mod
    num = q

if (N % res == 0):
    print('Yes')
else:
    print('No')
