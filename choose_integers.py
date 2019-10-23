import sys
a, b, c = map(int, input().split())
for n in range(a, a*b+1, a):
    if n % b == c:
        print('YES')
        sys.exit()
print('NO')
