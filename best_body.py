N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for _ in range(N-1)]

cnt = 0
cur_w = W
if S<= cur_w <= T:
    cnt += 1
for a in A:
    cur_w += a 
    if S <= cur_w <= T:
        cnt += 1
print(cnt)
