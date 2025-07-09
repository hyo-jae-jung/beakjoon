from sys import stdin  
from collections import deque  

N,M = map(int,stdin.readline().strip().split())
P = []
if N > 0:
    P += list(map(int,stdin.readline().strip().split()))

T = 10000
dp = [0]*(2*T+1)
q = deque([(T,0)])

ans = -1
while q:
    idx,cnt = q.popleft()
    if T+M == idx:
        ans = cnt
        break

    for i in P:
        if 0 <= idx+i <= 2*T:
            if dp[idx+i] == 0 or dp[idx+i] > cnt+1:
                q.append((idx+i,cnt+1))
                dp[idx+i] = cnt+1

print(ans)
