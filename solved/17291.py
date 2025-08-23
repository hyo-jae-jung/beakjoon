from sys import stdin   

N = int(stdin.readline().strip())
dp = [0]*(N+1)
for i in range(1,4):
    if i <= N:
        dp[i] = 1

for i in range(2,N+1):
    j = 0
    while i+j <= N and (j < (3 + (1 if i%2==0 else 0))):
        dp[i+j]+=dp[i-1]
        j+=1
        
print(dp[N])
