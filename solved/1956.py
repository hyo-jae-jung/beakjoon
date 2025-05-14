from sys import stdin  

V,E = map(int,stdin.readline().strip().split())
graph = [[4000001]*V for _ in range(V)]

for _ in range(E):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = 4000001
for i in range(V):
    for j in range(V):
            if i != j:
                ans = min(ans,graph[i][j] + graph[j][i])
            else:
                ans = min(ans,graph[i][j])

print(ans if ans < 4000001 else -1)
