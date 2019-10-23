S, N = list(input()), int(input())
S.sort()

candidates = [s + t for s in S for t in S]
print(candidates[N-1])
