N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
res = 0
for s in set(S):
    score = S.count(s) - T.count(s)
    if score > res:
        res = score
print(res)
