from sys import stdin  

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
graph = [[100000*n+1]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a-1][b-1] = min(c,graph[a-1][b-1])

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 100000*n+1:
            graph[i][j] = 0

for i in graph:
    print(*i)
