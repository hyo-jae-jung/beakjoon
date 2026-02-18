from sys import stdin  
from heapq import heappop,heappush

N = int(stdin.readline().strip())
lactures = []
for _ in range(N):
    lactures.append(tuple(map(int,stdin.readline().strip().split())))

lactures.sort(key=lambda x:x[1])

q = []
ans = 0
for i in range(N):
    _,s,e = lactures[i]
    while len(q) > 0 and q[0] <= s:
        heappop(q)
    heappush(q,e)
    ans = max(ans,len(q))
    
print(ans)
