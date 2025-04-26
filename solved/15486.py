from sys import stdin  

N = int(stdin.readline().strip())
schedule = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]
dp = [0]*(N+1)

for i in range(N):
    if i+schedule[i][0] <= N:
        dp[i+schedule[i][0]] = max(dp[i]+schedule[i][1],dp[i+schedule[i][0]])
    dp[i+1] = max(dp[i+1],dp[i])

print(max(dp))
