from sys import stdin 
from heapq import heappop,heappush

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))

start,end = map(int,stdin.readline().strip().split())

INF = int(1e9)
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))

dijkstra(start)
print(distance[end])
        