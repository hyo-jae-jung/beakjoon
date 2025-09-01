from sys import stdin   

N,start,end,M = map(int,stdin.readline().strip().split())
edges = []
adjacency_list = [[] for _ in range(N)]
for _ in range(M):
    s,e,c = map(int,stdin.readline().strip().split())
    edges.append((s,e,c))
    adjacency_list[s].append(e)
if N == 0:
    print('gg')
elif N > 0:
    profits = list(map(int,stdin.readline().strip().split()))

    dist = [float('inf')]*N
    dist[start] = -profits[start]

    for _ in range(N):
        for s,e,c in edges:
            if dist[e] > dist[s] + c - profits[e]:
                dist[e] = dist[s] + c - profits[e]

    dist_ans = dist.copy()

    for _ in range(N):
        for s,e,c in edges:
            if dist[e] > dist[s] + c - profits[e]:
                dist[e] = dist[s] + c - profits[e]

    if dist_ans[end] == float('inf'):
        print('gg')
    else:
        diff = []
        for i in range(N):
            if dist[i] != dist_ans[i]:
                diff.append(i)

        def dfs(n:int,graph:list,sv:int,ev:int) -> bool:
            visited = [False]*n
            visited[sv] = True
            stack = [sv]

            while stack:
                v = stack.pop()
                if v == ev:
                    return True
                for nv in graph[v]:
                    if not visited[nv]:
                        stack.append(nv)
                        visited[nv] = True

            return False

        for i in diff:
            if dfs(N,adjacency_list,i,end):
                print('Gee')
                break
        else:
            print(-dist_ans[end])
