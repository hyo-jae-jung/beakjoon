from sys import stdin  

n,m = map(int,stdin.readline().strip().split())
edges = []
adjacency_list = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,stdin.readline().strip().split())
    edges.append((u,v,w))
    adjacency_list[u].append(v)

dist = [-float('inf')]*(n+1)
dist[1] = 0
parent = [-1]*(n+1)
parent[1] = 1

for _ in range(n-1):
    for u,v,w in edges:
        if dist[v] < dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u

ref_dist = dist.copy()

for u,v,w in edges:
    if dist[v] < dist[u] + w:
        dist[v] = dist[u] + w

diff_idx = []
for i in range(1,n+1):
    if dist[i] > ref_dist[i]:
        diff_idx.append(i)

def dfs(n,graph,a,b):
    stack = [a]
    visited = [False]*(n+1)
    visited[a] = True
    while stack:
        u = stack.pop()
        if u == b:
            return True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
    return False

arr = []
for i in diff_idx:
    arr.append(dfs(n,adjacency_list,i,n))

if ref_dist[n] == -float('inf'):
    print(-1)
elif any(arr):
    print(-1)
else:
    from collections import deque 
    ans = deque()
    ans.appendleft(n)
    while n != 1:
        n = parent[n]
        ans.appendleft(n)
    print(*ans)
