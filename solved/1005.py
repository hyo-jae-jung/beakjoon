def dfs(graph,v,n):
    visited = [True]+[False]*n
    stack = [v]
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        for v2 in graph[v]:
            if not visited[v2]:
                stack.append(v2)
    return visited

import sys

T = int(sys.stdin.readline().strip())
ans = []
for _ in range(T):
    N,K = map(int,sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N+1)]
    graph_rev = [[] for _ in range(N+1)]
    D = [0] + list(map(int,sys.stdin.readline().strip().split()))
    indegree = [0]*(N+1)
    for _ in range(K):
        X,Y = map(int,sys.stdin.readline().strip().split())
        graph[X].append(Y)
        graph_rev[Y].append(X)
        indegree[Y]+=1
    W = int(sys.stdin.readline().strip())    
    able_nodes = dfs(graph_rev,W,N)

    for i in range(1,N+1):
        if indegree[i] == 0 :
            graph[0].append(i)
            indegree[i] = 1

    stack = [(0,0)]
    value_stack = [[0] for _ in range(N+1)]
    
    while stack:
        node,value = stack.pop()
        if not able_nodes[node]:
            continue
        if node == W:
            ans.append(value)
            break
        for node2 in graph[node]:
            indegree[node2]-=1
            if indegree[node2]:
                value_stack[node2].append(value)
            else:
                stack.append((node2,max(*value_stack[node2],value) + D[node2]))

print(*ans,sep='\n')
