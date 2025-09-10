def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
h = []
total_cost = 0
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    total_cost+=c
    heappush(h,(c,a,b))

use_cost = 0
parent = list(range(N+1))

while N > 1 and h:
    c,a,b = heappop(h)
    if (a:=find_parent(parent,a)) != (b:=find_parent(parent,b)):
        union_parent(parent,a,b)
        use_cost+=c
        N-=1

for i in range(1,len(parent)):
    if find_parent(parent,i) != 1:
        print(-1)
        break
else:
    print(total_cost - use_cost)
