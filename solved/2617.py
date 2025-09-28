from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
adjacency_matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    adjacency_matrix[a][b] = 1
    adjacency_matrix[b][a] = -1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if adjacency_matrix[i][j] == 0:
                if adjacency_matrix[i][k] == adjacency_matrix[k][j] == 1:
                    adjacency_matrix[i][j] = 1
                elif adjacency_matrix[i][k] == adjacency_matrix[k][j] == -1:
                    adjacency_matrix[i][j] = -1

ans = 0
for arr in adjacency_matrix:
    zero_cnt = -1
    res_cnt = 0
    for i in arr[1:]:
        if i == 0:
            zero_cnt+=1
        else:
            res_cnt+=i
    
    if abs(res_cnt) > zero_cnt:
        ans+=1

print(ans)
