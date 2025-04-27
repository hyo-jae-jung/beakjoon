from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
items = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]

dp = [0]*(M+1)
for w,d in items:
    for i in range(M,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+d)

print(max(dp))
