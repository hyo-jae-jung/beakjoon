from sys import stdin  

N,T = map(int,stdin.readline().strip().split())
question_list = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]

dp = [0]*(T+1)
for t,v in question_list:
    for i in range(T,t-1,-1):
        dp[i] = max(dp[i],dp[i-t]+v)
        
print(max(dp))
