import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().strip().split())
parent = list(range(n+1))

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

ans = []
for _ in range(m):
    act,a,b = map(int,sys.stdin.readline().strip().split())
    if act == 0:
        parent_union(parent,a,b)
    else:
        if parent_find(parent,a) == parent_find(parent,b):
            ans.append('YES')
        else:
            ans.append('NO')

print(*ans,sep='\n')
