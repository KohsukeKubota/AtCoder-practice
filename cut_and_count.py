N = int(input())
S = input()
cnt = 0

for i in range(1, N):
    dup_cnt = set(S[:i]) & set(S[i:])
    if cnt < len(dup_cnt):
        cnt = len(dup_cnt)
print(cnt)
