from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())

graph = [[] for i in range(N+1)]
for _ in range(N-1):
    node1,node2 = map(int,stdin.readline().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

answer = [[] for _ in range(N+1)]
visited = [False]*(N+1)
queue = deque([1])
while queue:
    parent = queue.popleft()
    if not visited[parent]:
        visited[parent] = True
        children = graph[parent]
        for child in children:
            if not visited[child]:
                answer[child] = parent
                queue.append(child)

print(*answer[2:],sep='\n')
