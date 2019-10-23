from sys import exit


N, Y = map(int, input().split())

res = 0

for i in range(N+1):
    for j in range(N+1):
        k = N - i - j
        if k >= 0:
            amm = 10000 * i + 5000 * j + 1000 * k
            if amm == Y:
                res += 1
                print('{} {} {}'.format(i, j, k))
                exit()

if res == 0:
    print('{} {} {}'. format(-1, -1, -1))
