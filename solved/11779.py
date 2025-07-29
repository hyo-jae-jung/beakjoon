from sys import stdin  
from heapq import heapify,heappop,heappush

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))

start,end = map(int,stdin.readline().strip().split())

min_graph = [0]*(n+1)

visited = [False]*(n+1)
distance = [float('inf')]*(n+1)
distance[start] = 0
h = list(zip(distance,range(n+1)))
heapify(h)

while h:
    d,n = heappop(h)
    if visited[n]:
        continue
    visited[n] = True
    for n2,d2 in graph[n]:
        if distance[n2] > d + d2:
            distance[n2] = d + d2
            min_graph[n2] = n
        heappush(h,(distance[n2],n2))


from collections import deque
q = deque()
def find_start(min_graph,q,start,end):
    q.appendleft(end)
    while start != (e:=min_graph[end]):
        q.appendleft(e)
        end = e
    q.appendleft(start)
    return q

print(distance[end])
ans = find_start(min_graph,q,start,end)
print(len(ans))
print(*ans)
