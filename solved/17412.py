from sys import stdin   
from collections import deque  

N,P = map(int,stdin.readline().strip().split())
adjacency_matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(P):
    start,end = map(int,stdin.readline().strip().split())
    adjacency_matrix[start][end] = 1

max_flow = 0

while True:

    q = deque([1])
    parent = [-1]*(N+1)
    parent[1] = 1

    while q:
        u = q.popleft()
        for v in range(1,N+1):
            if parent[v] == -1 and adjacency_matrix[u][v] > 0:
                parent[v] = u
                q.append(v)

    if parent[2] == -1:
        break

    path_flow = float('inf')

    v = 2
    while v != 1:
        u = parent[v]
        path_flow = min(path_flow,adjacency_matrix[u][v])
        v = u

    max_flow+=path_flow

    v = 2
    while v != 1:
        u = parent[v]
        adjacency_matrix[u][v]-=path_flow
        adjacency_matrix[v][u]+=path_flow
        v = u

print(max_flow)
