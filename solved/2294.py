from sys import stdin  

n,k = map(int,stdin.readline().strip().split())
coins = [int(stdin.readline().strip()) for _ in range(n)]

dp = [0] + [10001]*k
for coin in coins:
    for i in range(coin,k+1):
        dp[i]=min(dp[i-coin]+1,dp[i])

print(dp[k] if dp[k] != 10001 else -1)
