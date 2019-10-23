W, H, N = map(int, input().split())
XYA = [list(map(int, input().split())) for _ in range(N)]
x1, x2, y1, y2 = 0, W, 0, H
for x, y, a in XYA:
    if a == 1:
        x1 = max(x1, x)
    elif a == 2: 
        x2 = min(x2, x)
    elif a == 3:
        y1 = max(y1, y)
    elif a == 4:
        y2 = min(y2, y)
if x2 > x1 and y2 > y1:
    print((x2-x1)*(y2-y1))
else:
    print(0)
