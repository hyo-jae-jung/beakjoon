from sys import stdin  

N = int(stdin.readline().strip())
graph =[[501]*N for _ in range(N)]
while (t:=stdin.readline().strip()) != '-1 -1':
    a,b = map(int,t.split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

l = []
for i in graph:
    l.append(max(i))

m = min(l)
ans = []
for i,j in enumerate(l,1):
    if j == m:
        ans.append(i)

print(m,len(ans))
print(*ans)
