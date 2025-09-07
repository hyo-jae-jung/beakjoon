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
ans = []

while (t:=stdin.readline().strip()) != '0 0':
    m,n = map(int,t.split())
    h = []
    total = 0
    for _ in range(n):
        x,y,z = map(int,stdin.readline().strip().split())
        heappush(h,(z,x,y))
        total+=z

    parent = list(range(m+1))
    use = 0
    while m > 1:
        dist,x,y = heappop(h)
        if (a:=find_parent(parent,x)) != (b:=find_parent(parent,y)):
            union_parent(parent,a,b)
            use+=dist
            m-=1

    ans.append(total - use)

if ans:
    print(*ans,sep='\n')
