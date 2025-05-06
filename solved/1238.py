from sys import stdin 
from heapq import heapify,heappop,heappush

N,M,X = map(int,stdin.readline().strip().split())

INF = 10**6+1
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))

def dijkstra(x):

    visited = [False] + [True]*N
    distance = [INF]*(N+1)
    distance[x] = 0
    h = list(zip(distance,range(N+1)))
    heapify(h)
    heappush(h,(0,x))

    while h:
        d,v = heappop(h)
        if not visited[v]:
            continue
        visited[v] = False
        for v2,d2 in graph[v]:
            distance[v2] = min(distance[v2],d+d2)
            heappush(h,(distance[v2],v2))

    return distance

arr = []
for i in range(1,N+1):
    arr.append(dijkstra(i)[1:])

ans = 0
for i in range(N):
    if i != X-1:
        ans = max(ans,arr[min(i,X-1)][max(i,X-1)] + arr[max(i,X-1)][min(i,X-1)])

print(ans)
