from sys import stdin    
from collections import deque  

N,M = map(int,stdin.readline().strip().split())
graph = [stdin.readline().strip() for _ in range(N)]

def bfs(x,y):
    global N,M,graph
    visited = [[float('inf')]*M for _ in range(N)]
    q = deque([(x,y,1)])
    visited[y][x] = 1

    while q:
        x,y,d = q.popleft()

        if graph[y][x] == '0':
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
                    if visited[ny][nx] == float('inf') or visited[ny][nx] > d + 1:
                        visited[ny][nx] = d + 1
                        if graph[ny][nx] == '0':
                            q.append((nx,ny,d+1))
    return visited

ans = float('inf')
v1 = bfs(0,0)
v2 = bfs(M-1,N-1)

for i in range(N):
    for j in range(M):
        ans = min(ans,v1[i][j] + v2[i][j] - 1)

print(ans if ans != float('inf') else -1)


""" 
6 5
00000
11110
00000
01111
01011
10000
"""
