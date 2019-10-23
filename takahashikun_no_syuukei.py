N = int(input())
A = list(map(int, input().split()))
cnt = 0
sum_ = 0
for a in A:
    if a != 0:
        cnt += 1
        sum_ += a
print(-(-sum_//cnt))

