from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    A,B = map(int,stdin.readline().strip().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i] = sorted(graph[i])


def dfs_with_stack(graph,v):
    d = [0]*(N+1)
    visited = [False]*(len(graph)+1)
    stack = [v]
    while stack:
        p = stack.pop()
        if not visited[p]:
            visited[p] = True
            for i in graph[p]:
                if i != v and d[i] == 0:
                    d[i] = d[p]+1
            stack.extend(list(reversed(graph[p])))
    return sum(d)

from collections import defaultdict 

dd = defaultdict(int)

for i in range(1,N+1):
    dd[i] = dfs_with_stack(graph,i)

print(sorted(dd.items(),key=lambda x:(x[1],x[0]))[0][0])
