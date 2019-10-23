import math
a, b = input().split()
sqrt_ab = math.sqrt(int(a + b))
if sqrt_ab.is_integer():
    print('Yes')
else:
    print('No')
