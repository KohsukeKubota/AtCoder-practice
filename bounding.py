import numpy as np


N, X = map(int, input().split())
L_list = list(map(int, input().split()))

initial_val = 0
res = 0

if initial_val <= X:
    res += 1

for i in range(N):
    cd = initial_val + L_list[i]
    if cd <= X:
        res += 1
    initial_val = cd
    i += 1

print(res)
