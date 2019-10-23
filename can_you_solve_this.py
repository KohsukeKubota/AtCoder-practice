N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

res = 0

for i in range(N):
    target_num = sum([a*b for a, b in zip(A[i], B)]) + C
    if target_num > 0:
        res += 1

print(res)
