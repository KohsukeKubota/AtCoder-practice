def chmin(a, b):
    if a > b:
        return b
    else:
        return a
N = int(input())
H = list(map(int, input().split()))
dp = [float('INF')] * (10**5+10)
dp[0] = 0
for i in range(1, N):
    dp[i] = chmin(dp[i], dp[i-1] + abs(H[i] - H[i-1]))
    if i > 1:
        dp[i] = chmin(dp[i], dp[i-2] + abs(H[i] - H[i-2]))
print(dp[N-1])
