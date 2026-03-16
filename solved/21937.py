from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,stdin.readline().strip().split())
    adjacency_list[v].append(u)

start = int(stdin.readline().strip())

stack = [start]
visited = [False]*(N+1)
visited[start] = True

while stack:
    u = stack.pop()
    for v in adjacency_list[u]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)

print(sum(visited)-1)
