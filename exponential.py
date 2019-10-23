import math
X = int(input())
res = 0
for b in range(1, int(math.sqrt(X))+1):
    for p in range(2, int(math.sqrt(X))+2):
        val = b**p
        if (val <= X) and (val > res):
            res = val
print(res)
