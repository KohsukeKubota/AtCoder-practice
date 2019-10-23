import math
N = int(input())
res = 0
for i in range(int(math.sqrt(N))+1):
    val = i**2
    if val > res:
        res = val
print(res)
