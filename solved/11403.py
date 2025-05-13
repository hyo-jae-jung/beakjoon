from sys import stdin  

N = int(stdin.readline().strip())
graph = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] > 0 and graph[k][j] > 0:
                graph[i][j] = 1

for i in graph:
    print(*i)
