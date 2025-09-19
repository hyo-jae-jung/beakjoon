from sys import stdin  
from collections import deque  

H,W = map(int,stdin.readline().strip().split())
board = [list(stdin.readline().strip()) for _ in range(H)]
visited = [[float('inf')]*W for _ in range(H)]

d = deque()

for i in range(H):
    if d:
        break
    for j in range(W):
        if board[i][j] == 'S':
            d.append((j,i,0))
            visited[i][j] = 0
            break

def is_next_to_wall(arr,x,y)->bool:
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if arr[y+dy][x+dx] == '#':
            return True
    return False

while d:
    x,y,t = d.popleft()
    if board[y][x] == 'E':
        print(t)
        break 

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if board[(ny:=y+dy)][(nx:=x+dx)] != '#':
            if is_next_to_wall(board,x,y) and is_next_to_wall(board,nx,ny):
                if visited[ny][nx] > t:
                    d.appendleft((nx,ny,t))
                    visited[ny][nx] = t
            else:
                if visited[ny][nx] > t+1:
                    d.append((nx,ny,t+1))
                    visited[ny][nx] = t+1            
