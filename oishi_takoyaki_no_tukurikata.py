x, y = map(int, input().split())
cnt = 0
while y >= x:
    y -= x
    cnt += 1
print(cnt)
