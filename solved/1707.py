from sys import stdin  

K = int(stdin.readline().strip())

ans = []
for _ in range(K):
    V,E = map(int,stdin.readline().strip().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False]*(V+1)
    stack = list(range(1,V+1))
    visited[V] = 'r'
    tmp_ans = 'YES'
    while stack and tmp_ans == 'YES':
        v = stack.pop()
        for v2 in graph[v]:
            if visited[v2] == False:
                if visited[v] == 'r':
                    visited[v2] = 'b'
                else:
                    visited[v2] = 'r'
                stack.append(v2)
            elif visited[v2] == visited[v]:
                tmp_ans = 'NO'
                break
    ans.append(tmp_ans)

print(*ans,sep='\n')
