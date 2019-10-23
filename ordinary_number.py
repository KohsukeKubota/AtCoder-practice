import numpy as  np


n = int(input())
p = np.array(input().split(), np.int32)

res =  0

for i in range(1, n-1):
    p_part = p[i-1:i+2]
    p_sorted = np.sort(p_part)
    if  p_part[1] == p_sorted[1]:
        res += 1

print(res)
