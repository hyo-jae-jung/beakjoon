from sys import stdin  

N,x = map(int,stdin.readline().strip().split())
items = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]

dp = [1] + [0]*x
for l,c in items:
    for i in range(x,-1,-1):
        for j in range(c,0,-1):
            if 0 <= i+l*j <= x:
                dp[i+l*j]+=dp[i]

print(dp[x])
