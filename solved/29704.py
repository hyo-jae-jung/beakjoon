from sys import stdin  

N,T = map(int,stdin.readline().strip().split())

items = []
ans = 0
for _ in range(N):
    d,f = map(int,stdin.readline().strip().split())
    ans+=f
    items.append((d,f))

dp = [0]*(T+1)

for d, f in items:
    for w in range(T, d - 1, -1):
        dp[w] = max(dp[w], dp[w - d] + f)

print(ans - max(dp))
