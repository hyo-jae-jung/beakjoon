from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
graph = [[0]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and graph[i][k] > 0 and graph[k][j] > 0:
                graph[i][j] = 1

ans = 0
for j in range(N):
    if sum(graph[j]) + sum(graph[i][j] for i in range(N)) == N-1:
        ans+=1

print(ans)
