SE = [list(map(int, input().split())) for _ in range(3)]
res = 0
for i, se in enumerate(SE):
    res += SE[i][0] * SE[i][1]/10
print(int(res))
