from sys import stdin  

N = int(stdin.readline().strip())
foods = [0] + [int(stdin.readline().strip()) for _ in range(N)]

dp = [[0]*2 for _ in range(N+1)]
dp[1][0] = foods[1]
ans = foods[1]

tmp = 0
for i in range(2,N+1):
    dp[i][1] = dp[i-1][0] + foods[i]//2
    tmp = max(tmp,max(dp[i-2]))
    dp[i][0] = tmp + foods[i]
    ans = max(ans,max(dp[i]))

print(ans)
