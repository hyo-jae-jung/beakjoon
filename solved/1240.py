from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def distence(start,end,dist=0):
    global dist_min
    visited[start] = False
    for i,j in graph[start]:
        if i == end:
            dist_min = min(dist_min,dist+j)
        elif visited[i]:
            distence(i,end,dist+j)

answer = []
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    visited = [True]*(N+1)
    dist_min = 1e9
    distence(a,b)
    answer.append(dist_min)

print(*answer,sep='\n')
