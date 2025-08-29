from sys import stdin  

N = int(stdin.readline().strip())
graph = [[0]*52 for _ in range(52)]

def change_c_to_idx(x):
    if ord(x) >= 97:
        x = 26 + ord(x) - 97
    else:
        x = ord(x) - 65
    return x

for _ in range(N):
    a,b,f = stdin.readline().strip().split()
    graph[change_c_to_idx(a)][change_c_to_idx(b)] += int(f)
    graph[change_c_to_idx(b)][change_c_to_idx(a)] += int(f)

source = 0
sink = 25

from collections import deque 

max_flow = 0

while True:
    q = deque([source])
    parent = [-1]*52
    parent[source] = source

    while q:
        v = q.popleft()
        for u in range(52):
            if parent[u] == -1 and graph[v][u] > 0:
                parent[u] = v
                q.append(u)

    if parent[sink] == -1:
        break
    
    path_flow = float('inf')

    v = sink
    while v != source:
        u = parent[v]
        path_flow = min(path_flow,graph[u][v])
        v = u

    max_flow+=path_flow

    v = sink 
    while v != source:
        u = parent[v]
        graph[u][v]-=path_flow
        graph[v][u]+=path_flow
        v = u

print(max_flow)
