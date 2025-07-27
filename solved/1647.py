def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent,parent[x])
    return parent[x]

def parent_union(parent,a,b):
    a = parent_find(parent,a)
    b = parent_find(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

from sys import stdin   
from  heapq import heapify,heappop,heappush

N,M = map(int,stdin.readline().strip().split())
parent = list(range(N+1))

h = []
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    heappush(h,(c,a,b))

i = 0
ans = 0
while i < N-2:
    c,a,b = heappop(h)
    if (a:=parent_find(parent,a)) != (b:=parent_find(parent,b)):
        parent_union(parent,a,b)
        ans+=c
        i+=1
        
print(ans)
