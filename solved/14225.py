from sys import stdin  

N = int(stdin.readline().strip())
S = list(map(int,stdin.readline().strip().split()))
max_S = sum(S)
dp = [True] + [False]*(max_S+1)
for s in S:
    for i in range(max_S+1,-1,-1):
        if dp[i]:
            dp[i+s] = True

for i,j in enumerate(dp):
    if not j:
        print(i)
        break

