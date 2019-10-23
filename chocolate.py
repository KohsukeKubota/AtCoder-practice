N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
res = 0
for a in A:
    n = 1 + int((D-1)/a)
    res += n

print(res + X)
