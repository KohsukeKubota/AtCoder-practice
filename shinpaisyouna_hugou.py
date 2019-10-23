N = int(input())
A = [int(input()) for _ in range(N)]
a_max = max(A)
res = 0
for a in A:
    if a > res and a < a_max:
        res = a
print(res)
