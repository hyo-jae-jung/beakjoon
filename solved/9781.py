from sys import stdin 
from collections import deque

n,m = map(int,stdin.readline().strip().split())
board = [list(stdin.readline().strip()) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'K':
            board[i][j] = '#'
            q.append((j,i,0))
            break

ans = -1
while q:
    if ans != -1:
        break

    x,y,cnt = q.popleft()

    for dx,dy in [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]:
        if 0 <= (nx:=x+dx) < m and 0 <= (ny:=y+dy) < n:
            if board[ny][nx] == 'X':
                ans = cnt+1
                break

            if board[ny][nx] == ".":
                board[ny][nx] = '#'
                q.append((nx,ny,cnt+1))

print(ans)
