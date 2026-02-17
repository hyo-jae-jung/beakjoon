from sys import stdin  

n = int(stdin.readline().strip())

items = []
dp = [0]*10001
for _ in range(n):
    items.append(tuple(map(int,stdin.readline().strip().split())))

items.sort(key=lambda x:(-x[0],-x[1]))

for p,d in items:
    for i in range(d,0,-1):
        if dp[i] < p:
            dp[i] = p
            break

print(sum(dp))
