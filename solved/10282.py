from sys import stdin  
from heapq import heappop,heappush,heapify

ans = []
T = int(stdin.readline().strip())
for _ in range(T):
    n,d,c = map(int,stdin.readline().strip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,stdin.readline().strip().split())
        graph[b].append((a,s))
    visited = [False] + [True]*n
    distance = [n*1000+1]*(n+1)
    h = list(zip(distance,range(n+1)))
    heapify(h)
    heappush(h,(0,c))
    distance[c] = 0
    while h:
        _,v = heappop(h)
        if not visited[v]:
            continue
        visited[v] = False
        for v2,d2 in graph[v]:
            distance[v2] = min(distance[v2],distance[v]+d2)
            heappush(h,(distance[v2],v2))
    
    tmp = [i for i in distance if i < (n*1000+1)]
    ans.append((len(tmp),max(tmp)))
    
for i in ans:
    print(*i)
