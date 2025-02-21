from sys import stdin   
from heapq import heappop, heappush 

N,M,R = map(int,stdin.readline().strip().split())
graph = {}
for _ in range(M):
    u,v = map(int,stdin.readline().strip().split())

    if graph.get(u):
        heappush(graph[u],v)
    else:
        graph.update({u:[v]})

    if graph.get(v):
        heappush(graph[v],u)
    else:
        graph.update({v:[u]})

ans = [-1]*(N+1)
stack = [(R,0)]
i = 1

while stack:
    v,r = map(int,stack.pop())
    if ans[v] == -1:
        ans[v] = r*i
        print(r,i)
        i+=1
    
    while graph.get(v):
        stack.append((heappop(graph[v]),r+1))

print(sum(i if i != -1 else 0 for i in ans))
