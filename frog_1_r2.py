def chmin(a, b):
    if a > b:
        return b
    else:
        return a
N = int(input())
h = list(map(int, input().split()))
dp = [float('INF')] * (10**5+10)
dp[0] = 0
for i in range(0, N-1):
    dp[i+1] = chmin(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    if i < N-2:
        dp[i+2] = chmin(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
print(dp[N-1])
