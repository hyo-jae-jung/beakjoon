import sys,heapq

N,M,X = map(int,sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]
distance = [0]+[101]*N

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(X,distance)

for i in range(1,N+1):
    temp_distance = [0]+[101]*N
    if i == X:
        continue
    dijkstra(i,temp_distance)
    distance[i]+=temp_distance[X]

print(max(distance))
