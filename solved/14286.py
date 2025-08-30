from sys import stdin   

n,m = map(int,stdin.readline().strip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

s,t = map(int,stdin.readline().strip().split())

from collections import deque  

max_flow = 0

while True:

    q = deque([s])
    parent = [-1]*(n+1)
    parent[s] = s

    while q:
        v = q.popleft()
        for u in range(n+1):
            if parent[u] == -1 and graph[v][u] > 0:
                parent[u] = v
                q.append(u)

    if parent[t] == -1:
        break

    path_flow = float('inf')

    v = t
    while v != s:
        u = parent[v]
        path_flow = min(path_flow,graph[u][v])
        v = u

    max_flow+=path_flow

    v = t 
    while v != s:
        u = parent[v]
        graph[u][v]-=path_flow
        graph[v][u]+=path_flow
        v = u

print(max_flow)
    