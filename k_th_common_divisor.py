import sys


A, B, K = map(int, input().split())

cnt = 0

for i in reversed(range(1, 101)):
    if (A % i == 0) and (B % i == 0):
        cnt += 1
        if cnt == K:
            print(i)
            sys.exit()
