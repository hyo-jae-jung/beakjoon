from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    graph = [[] for _ in range(N+1)]
    visited = [True]*(N+1)
    min_cnt = 0
    for _ in range(M):
        a,b = map(int,stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)


def dfs(a):
    visited[a] = False
    for i in graph[a]:
        