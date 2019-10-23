N, Q = map(int, input().split())
a = [0 for _ in range(N)]
LRT = [list(map(int, input().split())) for _ in range(Q)]
for l, r, t in LRT:
    a[l-1:r] = [t for _ in range(len(a[l-1:r]))]
for i in a:
    print(i)
