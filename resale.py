N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

profit = [x - y for (x, y) in zip(V, C)]

res = 0

for i in range(N):
    if profit[i] > 0:
        res += profit[i]

print(res)
