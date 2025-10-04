from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

dp = [1]*N
g = {}

for i in range(1,N):
    u,c = 0,0
    for j in range(i):
        if A[i] > A[j] and dp[j] > c:
            u = j
            c = dp[j]
    if c > 0:
        dp[i]+=c
        if not g.get(i):
            g.update({i:u})
        g[i] = u

from collections import deque 

ans_len = max(dp)
ans = deque()
stack = [dp.index(ans_len)]
while stack:
    v = stack.pop()
    ans.appendleft(A[v])
    if g.get(v) is not None:
        stack.append(g[v])

print(ans_len)
print(*ans)
