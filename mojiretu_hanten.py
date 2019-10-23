S = input()
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
for l, r in LR:
    l -= 1
    r -= 1
    forward = S[:l]
    part_str = S[l:r+1]
    backward = S[r+1:]
    S = forward + part_str[::-1] + backward
print(S)
