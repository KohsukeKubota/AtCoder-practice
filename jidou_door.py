N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
res = T
open_time = A[0]+T
for a in A[1:]:
    if a >= open_time:
        res += T
    else:
        res += (T - (open_time - a))
    open_time = a + T
print(res)
