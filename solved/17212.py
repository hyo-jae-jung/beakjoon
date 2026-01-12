from sys import stdin 

N = int(stdin.readline().strip())
dp = list(range(N+1))

for i in [2,5,7]:
    for j in range(N+1-i):
        dp[j+i] = min(dp[j+i],dp[j]+1)

print(dp[N])
