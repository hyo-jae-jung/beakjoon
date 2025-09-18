from sys import stdin 
from collections import deque  

H,W = map(int,stdin.readline().strip().split())
sea = [list(stdin.readline().strip()) for _ in range(H)]
visited = [[float('inf')]*W for _ in range(H)]

d = deque()
for i in range(H):
    for j in range(W):
        if sea[i][j] == "K":
            starting_point = (j,i,0)
            visited[i][j] = 0
        elif sea[i][j] == "*":
            end_point = (j,i)

d.append(starting_point)
ans = -1
while d:
    x,y,c = d.popleft()

    if sea[y][x] == "*":
        ans = c
        break

    for dx,dy in [(1,-1),(1,0),(1,1)]:
        if 0 <= (nx:=x+dx) < W and 0 <= (ny:=y+dy) < H and visited[ny][nx] > c:
            if sea[ny][nx] != '#':
                d.appendleft((nx,ny,c))
                visited[ny][nx] = c

    for dx,dy in [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]:
        if 0 <= (nx:=x+dx) < W and 0 <= (ny:=y+dy) < H and visited[ny][nx] > c+1:
            if sea[ny][nx] != '#':
                d.append((nx,ny,c+1))
                visited[ny][nx] = c+1

print(ans)
