N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
res = 0
for lr in LR:
    res += lr[1]-lr[0]+1
print(res)
