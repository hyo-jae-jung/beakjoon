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

import sys
sys.setrecursionlimit(10**6)

V,E = map(int,sys.stdin.readline().strip().split())

from heapq import heappop,heappush
h = []
for _ in range(E):
    A,B,C = map(int,sys.stdin.readline().strip().split())
    heappush(h,(C,A,B))

ans = 0
i = 0
parent = list(range(V+1))

while h and i < V:
    cost,a,b = heappop(h)
    if (a:=parent_find(parent,a)) != (b:=parent_find(parent,b)):
        parent_union(parent,a,b)
        ans+=cost
        i+=1

print(ans)
