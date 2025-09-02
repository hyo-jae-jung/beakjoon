from sys import stdin   
from collections import deque

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    adjacency_matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,stdin.readline().strip().split())
        adjacency_matrix[x][y] = 1
    
    max_flow = 0

    while True:

        q = deque([1])
        parent = [-1]*(N+1)
        parent[1] = 1

        while q:
            v = q.popleft()
            for i in range(1,N+1):
                if parent[i] == -1 and adjacency_matrix[v][i]:
                    parent[i] = v
                    q.append(i)

        if parent[N] == -1:
            break

        path_flow = float('inf')

        u = N
        while u != 1:
            v = parent[u]
            path_flow = min(path_flow,adjacency_matrix[v][u])
            u = v

        max_flow+=path_flow

        u = N
        while u != 1:
            v = parent[u]
            adjacency_matrix[v][u]-=path_flow
            adjacency_matrix[u][v]+=path_flow
            u = v

    ans.append(max_flow)

print(*ans,sep='\n')
