from sys import stdin  

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
adjacency_matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    adjacency_matrix[a][b] = 1
    adjacency_matrix[b][a] = -1

for i in range(1,N+1):
    adjacency_matrix[i][i] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if adjacency_matrix[i][j] == 0:
                if adjacency_matrix[i][k] == adjacency_matrix[k][j] == 1:
                    adjacency_matrix[i][j] = 1
                elif adjacency_matrix[i][k] == adjacency_matrix[k][j] == -1:
                    adjacency_matrix[i][j] = -1
                
for i in range(1,N+1):
    print(adjacency_matrix[i].count(0)-1)
    