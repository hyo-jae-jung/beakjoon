from sys import stdin  

G = int(stdin.readline().strip())
P = int(stdin.readline().strip())
gs = [int(stdin.readline().strip()) for _ in range(P)]

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

parent = list(range(G+1))
ans = 0

for g in gs:
    if find_parent(parent,g) > 0:
        union_parent(parent,g,parent[g]-1)
        ans+=1
    else:
        break

print(ans)
