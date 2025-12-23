from sys import stdin   

dp = [0]*31
dp[0] = 1
dp[1] = 1

for i in range(2,31):
    for j in range(i):
        dp[i]+=dp[j]*dp[i-j-1]

ans = []
while (n:=int(stdin.readline().strip())) != 0:
    ans.append(dp[n])

print(*ans,sep='\n')
