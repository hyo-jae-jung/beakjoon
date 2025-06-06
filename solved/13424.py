from sys import stdin  
from heapq import heapify,heappop,heappush

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b,c = map(int,stdin.readline().strip().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    K = int(stdin.readline().strip())
    friends = map(int,stdin.readline().strip().split())

    each_min_len = {}
    for friend in friends:

        visited = [True] + [False]*N
        INF = N*1000+1
        distance = [INF]*(N+1)
        distance[friend] = 0

        h = list(zip(distance,range(N+1)))
        heapify(h)

        while h:
            d,v = heappop(h)
            if visited[v]:
                continue
            visited[v] = True
            for v2,d2 in graph[v]:
                distance[v2] = min(distance[v2],d+d2)
                heappush(h,(distance[v2],v2))

        for i,j in enumerate(distance[1:],1):
            if not each_min_len.get(i):
                each_min_len.update({i:0})
            each_min_len[i]+=j
            
    ans.append(sorted(each_min_len.items(),key=lambda x:(x[1],x[0]))[0][0])

print(*ans,sep='\n')
