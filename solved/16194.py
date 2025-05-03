from sys import stdin  

N = int(stdin.readline().strip())
P = list(map(int,stdin.readline().strip().split()))

dp = [0] + [10000]*N
for i,p in enumerate(P,1):
    for j in range(i,N+1):
        dp[j] = min(dp[j],dp[j-i]+p)

print(dp[-1])
