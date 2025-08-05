from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    graph[A].append(B)
    indegree[B]+=1

h = []
for i,j in enumerate(indegree[1:],1):
    if j == 0:
        heappush(h,i)

ans = []
while h:
    n = heappop(h)
    ans.append(n)

    for v in graph[n]:
        indegree[v]-=1
        if indegree[v] == 0:
            heappush(h,v)

print(*ans)
