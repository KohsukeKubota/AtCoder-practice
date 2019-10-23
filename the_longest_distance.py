from math import sqrt


N = int(input())
coordinate = [list(map(int, input().split())) for i in range(N)]

res = -1

for i in range(N):
    for j in range(N):
        a = coordinate[i]
        b = coordinate[j]
        dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        if res < dist:
            res = dist

print('{:.6f}'.format(res))
