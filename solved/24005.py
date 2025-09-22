dp = list(range(10001))

for i in range(2,101):
    dp[i**2] = 1

for i in range(2,10001):
    for j in range(i):
        dp[i] = min(dp[i],dp[j]+dp[i-j])

from sys import stdin  

T = int(stdin.readline().strip())

ans = []
for i in range(1,T+1):
    N = int(stdin.readline().strip())
    ans.append(f"Case #{i}: {dp[N]}")

print(*ans,sep='\n')
