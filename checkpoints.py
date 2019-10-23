N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    res = 1000000000
    tidx = 0
    for j in range(M):
        dist = abs(AB[i][0]-CD[j][0]) + abs(AB[i][1]-CD[j][1])
        if res > dist:
            res = dist
            tidx = j+1
    print(tidx)
