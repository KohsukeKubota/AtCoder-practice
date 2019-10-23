N = int(input())
SP = [input().split() for _ in range(N)]
sum_, max_ = 0, 0
for s, p in SP:
    sum_ += int(p)
    if max_ < int(p):
        max_ = int(p)
        max_name = s
if max_ > sum_/2:
    print(max_name)
else:
    print('atcoder')
