N = int(input())
P = [int(input()) for _ in range(N)]
P.sort()
print(int(sum(P[:-1]) + P[-1]/2))
