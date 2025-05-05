from sys import stdin  
from heapq import heappop,heappush,heapify

N,M,K,X = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    graph[A].append(B)

visited = [False] + [True]*N
distance = [1000001]*(N+1)
h = list(zip(distance,range(N+1)))
heapify(h)
heappush(h,(0,X))
distance[X] = 0

while h:
    d,v = heappop(h)
    if not visited[v]:
        continue
    visited[v] = False
    for i in graph[v]:
        distance[i] = min(distance[i],d+1)
        heappush(h,(distance[i],i))

ans = []
for i,j in enumerate(distance):
    if j == K:
        ans.append(i)

if ans:
    print(*ans,sep='\n')
else:
    print(-1)
    