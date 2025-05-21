from sys import stdin  

S = list(map(int,stdin.readline().strip().split()))

dp = [0]*(sum(S)+1)
for i in range(1,S[0]+1):
    for j in range(1,S[1]+1):
        for k in range(1,S[2]+1):
            dp[i+j+k]+=1

print(dp.index(max(dp)))
