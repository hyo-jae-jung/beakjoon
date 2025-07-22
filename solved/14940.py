from sys import stdin   
from collections import deque

n,m = map(int,stdin.readline().strip().split())
graph = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append([j,i,0])
            graph[i][j] = 0
            break

ans = [[0]*m for _ in range(n)]

while q:
    x,y,d = q.popleft()

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < m and 0 <= (ny:=y+dy) < n:
            if graph[ny][nx] == 1:
                ans[ny][nx] = d+1
                q.append([nx,ny,d+1])
                graph[ny][nx]-=1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans[i][j] = -1

for i in ans:
    print(*i)
