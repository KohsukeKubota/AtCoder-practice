from statistics import mean
N = int(input())
A = list(map(int, input().split()))
mean_ = mean(A)
if mean_.is_integer():
    target, res = 0, 0
    for i in range(len(A)):
        target += A[i]
        if target != mean_ * (i+1):
            res += 1
    print(res)
else:
    print(-1)
