from sys import stdin  
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
S,E = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(N+1)
visited[S] = True
q = deque([(S,0)])

while q:
    s,t = q.popleft()
    
    if s == E:
        print(t)
        break

    for ss in graph[s]:
        if not visited[ss]:
            q.append((ss,t+1))
            visited[ss] = True

    for ds in [-1,1]:
        if 1 <= (ns:=s+ds) <= N and not visited[ns]:
            q.append((ns,t+1))
            visited[ns] = True
