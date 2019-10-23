from itertools import combinations
from math import sqrt


N, D = map(int, input().split())
X_list = []
for i in range(N):
    X = list(map(int, input().split()))
    X_list.append(X)

comb_list = list(combinations(X_list, 2))
res = 0

for i in range(len(comb_list)):
    x1 = comb_list[i][0]
    x2 = comb_list[i][1]

    dst_elements = [(x1[i] - x2[i])**2 for i in range(len(x1))]
    dst = sqrt(sum(dst_elements))
    if dst.is_integer():
        res += 1

print(res)
