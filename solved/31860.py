from sys import stdin  
from heapq import heappop,heappush

N,M,K = map(int,stdin.readline().strip().split())
h = []
for _ in range(N):
    heappush(h,-int(stdin.readline().strip()))

ans = [0]
while h:
    p_work = -heappop(h)
    ans.append(ans[-1]//2 + p_work)
    if (n_work:=p_work-M) > K:
        heappush(h,-n_work)
    
print(len(ans[1:]))
print(*ans[1:],sep='\n')
