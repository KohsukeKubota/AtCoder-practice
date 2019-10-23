from bisect import bisect_left
N = int(input())
l = list(map(int, input().split()))
l.sort()
res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        t = l[i] + l[j]
        idx = bisect_left(l, t)
        res += idx-j-1
print(res)
