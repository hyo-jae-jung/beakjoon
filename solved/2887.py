from sys import stdin   
from heapq import heappop,heappush

N = int(stdin.readline().strip())

X,Y,Z = [],[],[]
for i in range(N):
    x,y,z = map(int,stdin.readline().strip().split())
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))

X.sort()
Y.sort()
Z.sort()

h = []

for i in range(1,N):
    heappush(h,(abs(X[i][0] - X[i-1][0]),X[i][1],X[i-1][1]))
    heappush(h,(abs(Y[i][0] - Y[i-1][0]),Y[i][1],Y[i-1][1]))
    heappush(h,(abs(Z[i][0] - Z[i-1][0]),Z[i][1],Z[i-1][1]))

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

parent = list(range(N+1))
c = 0
ans = 0
while h and c < N:
    d,a,b = heappop(h)
    if (a:=parent_find(parent,a)) != (b:=parent_find(parent,b)):
        parent_union(parent,a,b)
        ans+=d
        c+=1
        
print(ans)
