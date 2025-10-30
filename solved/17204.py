from sys import stdin   

N,K = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N)]
for i in range(N):
    adjacency_list[i].append(int(stdin.readline().strip()))

def dfs(graph,start=0,end=K):
    depth = 0
    visited = [False]*N
    stack = [start]
    while stack:
        u = stack.pop()
        if u == K:
            return depth
        
        visited[u] = True
        for v in adjacency_list[u]:
            if not visited[v]:
                stack.append(v)
                depth+=1
        
    return -1

print(dfs(adjacency_list,0,K))
