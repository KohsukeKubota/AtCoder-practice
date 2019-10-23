N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    sum_t = sum(T)
    idx = PX[i][0] - 1
    if T[idx] >= PX[i][1]:
        sum_t -= (T[idx] - PX[i][1])
    else:
        sum_t += PX[i][1] - T[idx]
    print(sum_t)
