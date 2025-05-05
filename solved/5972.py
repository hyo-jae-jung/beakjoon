from sys import stdin  
from heapq import heapify,heappop,heappush

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,stdin.readline().strip().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

visited = [False] + [True]*N
distance = [5*10**7+1]*(N+1)
h = list(zip(distance,range(N+1)))
heapify(h)
heappush(h,(0,1))

while h:
    d,v = heappop(h)
    if not visited[v]:
        continue
    visited[v] = False
    for v2,d2 in graph[v]:
        distance[v2] = min(distance[v2],d+d2)
        heappush(h,(distance[v2],v2))

print(distance[N])
