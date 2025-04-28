from sys import stdin  

C,N = map(int,stdin.readline().strip().split())

items = []
max_pcnt = 0
for _ in range(N):
    cost,people = map(int,stdin.readline().strip().split())
    max_pcnt = max(max_pcnt,(C//people+1)*people)
    items.append(tuple([cost,people]))

dp = [0] + [max_pcnt*100]*max_pcnt

for i,c in items:
    for j in range(c,max_pcnt+1):
        dp[j] = min(dp[j],dp[j-c]+i)

print(min(dp[C:]))
