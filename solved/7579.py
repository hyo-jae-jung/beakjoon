from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
Am = list(map(int,stdin.readline().strip().split()))
Ac = list(map(int,stdin.readline().strip().split()))

sumAc = sum(Ac)
dp = [0]*(sumAc+1)
for i in range(N):
    for j in range(sumAc,Ac[i]-1,-1):
        dp[j] = max(dp[j-Ac[i]]+Am[i],dp[j])
        
for i,j in enumerate(dp):
    if j >= M:
        print(i)
        break
