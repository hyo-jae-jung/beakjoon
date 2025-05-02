from sys import stdin 

n,k = map(int,stdin.readline().strip().split())
nums = [int(stdin.readline().strip()) for _ in range(n)]
dp = [1] + [0]*k
for num in nums:
    for i in range(num,k+1):
        dp[i]+=dp[i-num]

print(dp[k])
