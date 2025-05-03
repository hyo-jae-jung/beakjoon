from sys import stdin

N = int(stdin.readline().strip())
P = [int(i) for i in stdin.readline().strip().split()]

dp = [0]*(N+1)
for i,p in enumerate(P,1):
    for j in range(i,N+1):
        dp[j] = max(dp[j],dp[j-i]+p)

print(dp[-1])
