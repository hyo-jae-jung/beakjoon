from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
A = [0] + list(map(int,stdin.readline().strip().split()))

dp = [[0]*(N+1) for _ in range(M+1)]
dp[0][0] = 1
for i in range(M):
    for j in range(N):
        if dp[i][j] > 0:
            dp[i+1][j+1] = dp[i][j] + A[j+1]

    for k in range(N):
        if dp[i][k] > 0 and k+2 <= N:
            dp[i+1][k+2] = max(dp[i+1][k+2],dp[i][k]//2 + A[k+2])

ans = 0
for l in dp:
    ans = max(ans,max(l))

print(ans)
