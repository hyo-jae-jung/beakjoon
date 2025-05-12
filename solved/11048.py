from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
graph = [[0]*(M+1)]
for _ in range(N):
    graph.append([0] + list(map(int,stdin.readline().strip().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        graph[i][j]+=max(graph[i-1][j],graph[i][j-1])

print(graph[N][M])

