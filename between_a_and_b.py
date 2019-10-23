a, b, x = map(int, input().split())
fb = b//x + 1
if a == 0:
    fa = 0
else:
    fa = (a-1)//x + 1
print(fb-fa)
