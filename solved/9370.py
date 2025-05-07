from sys import stdin  
from heapq import heapify,heappop,heappush

def djikstra(v,n,graph,inf):
    visited = [False] + [True]*n 
    distance = [inf]*(n+1)
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
ans = []
T = int(stdin.readline().strip())
for _ in range(T):
    n,m,t = map(int,stdin.readline().strip().split())
    s,g,h = map(int,stdin.readline().strip().split())
    graph = [[] for _ in range(n+1)]
    INF = 1000*n+1
    for _ in range(m):
        a,b,d = map(int,stdin.readline().strip().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    backup = []
    for _ in range(t):
        backup.append(int(stdin.readline().strip()))

    front = djikstra(s,n,graph,INF)
    second = djikstra(g,n,graph,INF)
    third = djikstra(h,n,graph,INF)

    backup_min = []
    for i in backup:
        backup_min.append(front[i])

    tmp_ans = []
    for i,j in zip(backup,backup_min):
        a = [front[g],second[h],third[i]]
        b = [front[h],third[g],second[i]]
        if min(sum(a),sum(b)) <= j:
            tmp_ans.append(i)
        
    ans.append(sorted(tmp_ans))

for i in ans:
    print(*i)
