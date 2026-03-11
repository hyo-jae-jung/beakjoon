from sys import stdin 
from collections import deque 

board = [[0]*501 for _ in range(501)]

N = int(stdin.readline().strip())
for _ in range(N):
    X1,Y1,X2,Y2 = map(int,stdin.readline().strip().split())
    minx,maxx = min(X1,X2),max(X1,X2)
    miny,maxy = min(Y1,Y2),max(Y1,Y2)

    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            board[y][x] = 1

M = int(stdin.readline().strip())
for _ in range(M):
    X1,Y1,X2,Y2 = map(int,stdin.readline().strip().split())
    minx,maxx = min(X1,X2),max(X1,X2)
    miny,maxy = min(Y1,Y2),max(Y1,Y2)

    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            board[y][x] = 2

ans = -1    
queue = deque([(0,0,0)])
board[0][0] = 2

while queue:
    x,y,life = queue.popleft()

    if x == 500 and y == 500:
        ans = life
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) <= 500 and 0 <= (ny:=y+dy) <= 500 and board[ny][nx] != 2:
            if board[ny][nx] == 0:
                queue.appendleft((nx,ny,life))
            elif board[ny][nx] == 1:
                queue.append((nx,ny,life+1))
            board[ny][nx] = 2

print(ans)
