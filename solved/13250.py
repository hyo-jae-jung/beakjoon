from sys import stdin 

N = int(stdin.readline().strip())

dp = [0.0]*(N+6)
for i in range(N-1,-1,-1):
    p = 0
    for j in range(i+1,i+7):
        p+=dp[j]
    p/=6
    dp[i] = 1 + p

print(dp[0])
