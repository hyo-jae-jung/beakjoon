from sys import stdin

N,M = map(int,stdin.readline().strip().split())
adjacency_matrix = [[10**7]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    adjacency_matrix[a][b] = c
    adjacency_matrix[b][a] = c

for i in range(1,N+1):
    adjacency_matrix[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if adjacency_matrix[i][j] > adjacency_matrix[i][k] + adjacency_matrix[k][j]:
                adjacency_matrix[i][j] = adjacency_matrix[i][k] + adjacency_matrix[k][j]

arr = []
for i in range(1,N+1):
    arr.append((sum(adjacency_matrix[i]),i))

arr.sort(key=lambda x:(x[0],x[1]))
print(arr[0][1])
