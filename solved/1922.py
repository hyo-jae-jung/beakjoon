from sys import stdin  
from heapq import heappop,heappush

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
h = []
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    heappush(h,(c,a,b))

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

parent = list(range(N+1))
ans = 0

while N > 1:
    cost,u,v = heappop(h)
    if (a:=find_parent(parent,u)) != (b:=find_parent(parent,v)):
        union_parent(parent,a,b)
        ans+=cost
        N-=1

print(ans)
