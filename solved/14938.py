from sys import stdin  

n,m,r = map(int,stdin.readline().strip().split())
t = list(map(int,stdin.readline().strip().split()))
graph = [[2000]*n for _ in range(n)]
for _ in range(r):
    a,b,l = map(int,stdin.readline().strip().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = 0
for i in graph:
    tmp = 0
    for j,k in enumerate(i):
        if k <= m:
            tmp+=t[j]

    ans = max(ans,tmp)

print(ans)
