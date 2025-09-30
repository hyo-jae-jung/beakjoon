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

n,m = map(int,stdin.readline().strip().split())
ans = 0
parent = list(range(n))
for i in range(1,m+1):
    a,b = map(int,stdin.readline().strip().split())
    if ans == 0:
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
        else:
            ans = i

print(ans)
