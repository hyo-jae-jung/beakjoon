from sys import stdin  

N,D = map(int,stdin.readline().strip().split())
dp = list(range(D+1))
items = []
for _ in range(N):
    start,end,dist = map(int,stdin.readline().strip().split())
    if end <= D:
        items.append((start,end,dist))
    
for i in range(1,D+1):
    dp[i] = dp[i-1] + 1
    for start,end,dist in items:
        if i == end:
            dp[i] = min(dp[i],dp[start] + dist)

print(dp[D])
    