from sys import stdin  

V,N = map(int,stdin.readline().strip().split())
coins = [int(stdin.readline().strip()) for _ in range(V)]

dp = [1] + [0]*N
for c in coins:
    for i in range(c,N+1):
        dp[i]+=dp[i-c]

print(dp[N])
