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

n = int(stdin.readline().strip())
stars = []
for i in range(n):
    x,y = map(float,stdin.readline().strip().split())
    stars.append((i,x,y))

arr = []
for i in range(1,n):
    for j in range(i):
        arr.append((((stars[j][1]-stars[i][1])**2 + (stars[j][2]-stars[i][2])**2)**0.5,stars[j][0],stars[i][0]))

arr.sort()
parent = list(range(n))
cost = 0
for d,a,b in arr:
    if (a:=find_parent(parent,a)) != (b:=find_parent(parent,b)):
        cost+=d
        union_parent(parent,a,b)

print(int((cost+0.005)*100)/100)
