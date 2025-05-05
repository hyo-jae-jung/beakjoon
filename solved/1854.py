from sys import stdin  
from heapq import heappop,heappush

n,m,k = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))

h = []
heappush(h,(0,1))
distance_list = [[] for _ in range(n+1)]
heappush(distance_list[1],0)
visited = [0]*(n+1)
while h:
    d,v = heappop(h)
    if visited[v] > k:
        continue
    visited[v]+=1
    for v2,d2 in graph[v]:
        heappush(distance_list[v2],d+d2)
        heappush(h,(d+d2,v2))

for i in range(1,n+1):
    if len(distance_list[i]) >= k:
        j = 0
        while j < k:
            ans = heappop(distance_list[i])
            j+=1
        print(ans)
    else:
        print(-1)
