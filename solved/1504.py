from sys import stdin  
from heapq import heapify,heappop,heappush

def djikstra(v,n,graph):
    visited = [False] + [True]*n
    distance = [INF]*(n+1)
    distance[v] = 0
    h = list(zip(distance,range(n+1)))
    heapify(h)

    while h:
        d,v = heappop(h)
        if not visited[v]:
            continue
        visited[v] = False
        for v2,d2 in graph[v]:
            distance[v2] = min(distance[v2],d+d2)
            heappush(h,(distance[v2],v2))
    
    return distance

N,E = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1000*E+1

v1,v2 = map(int,stdin.readline().strip().split())

front = djikstra(1,N,graph)
mid = djikstra(v1,N,graph)
end = djikstra(v2,N,graph)

a = [front[v1],mid[v2],end[N]]
b = [front[v2],end[v1],mid[N]]

print(min(sum(a),sum(b)) if INF not in a+b else -1)

