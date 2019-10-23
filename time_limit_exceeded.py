import sys


N, T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]
target_list = [[c, t] for c, t in CT if t <= T]

if len(target_list) == 0:
    print('TLE')
else:
    target_list = sorted(target_list, key=lambda t: t[0])
    print(target_list[0][0])
