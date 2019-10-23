N = int(input())
cnt = 0
while N > 1:
    cnt += 1
    N -= 2
else:
    cnt += 1
    print(cnt)
    for i in range(cnt):
        if i == 0:
            print(1)
        else:
            print(2)
