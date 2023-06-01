from sys import stdin 
from collections import deque 

N,M,R = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    
arr = []
answer = [0]*(N+1)

def bfs(graph,start):
    visited = [False]*(N+1)
    queue = deque() 
    queue = deque([start])  
    visited[start] = True
    while queue:
        v = queue.popleft()
        arr.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,R)

for i,j in enumerate(arr,1):
    answer[j] = i

print(*answer[1:],sep='\n')
