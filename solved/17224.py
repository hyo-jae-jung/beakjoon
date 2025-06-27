from sys import stdin  
from heapq import heappop,heappush

N,L,K = map(int,stdin.readline().strip().split())
ans = 0
items = []
for _ in range(N):
    sub1,sub2 = map(int,stdin.readline().strip().split())
    if sub2 <= L:
        heappush(items,-140)
    elif sub1 <= L:
        heappush(items,-100)
    else:
        heappush(items,0)

for _ in range(K):
    ans-=heappop(items)

print(ans)
