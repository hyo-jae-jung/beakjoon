from sys import stdin  

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
adjacency_matrix = [[0]*(N+1)]
for _ in range(N):
    adjacency_matrix.append([0] + list(map(int,stdin.readline().strip().split())))

plan = list(map(int,stdin.readline().strip().split()))
parent = list(range(N+1))

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

for i in range(N+1):
    for j in range(N+1):
        if adjacency_matrix[i][j]:
            union_parent(parent,i,j)

for i in range(1,M):
    if parent[plan[i]] != parent[plan[i-1]]:
        print('NO')
        break
else:
    print('YES')
