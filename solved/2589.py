from sys import stdin  
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
island_map = [list(stdin.readline().strip()) for _ in range(N)]

def bfs(x,y):
    global island_map,N,M
    result = 0
    visited = [[2501]*M for _ in range(N)]
    q = deque([(x,y,0)])
    visited[y][x] = 0

    while q:
        x,y,d = q.popleft()
        result = max(result,d)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and visited[ny][nx] > d+1 and island_map[ny][nx] == 'L':
                visited[ny][nx] = d+1
                q.append((nx,ny,d+1))

    return result

ans = 0
for i in range(N):
    for j in range(M):
        if island_map[i][j] == 'L':
            ans = max(ans,bfs(j,i))

print(ans)
