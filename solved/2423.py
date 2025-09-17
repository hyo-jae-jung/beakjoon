from sys import stdin 
from collections import deque  

N,M = map(int,stdin.readline().strip().split())
lines = [list(stdin.readline().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

if N%2 == M%2:
    d = deque([(0,0,(0 if lines[0][0] == "\\" else 1))])
    lines[0][0] = "\\"
    visited[0][0] = True
    while d:
        x,y,c = d.popleft()
        if x == M-1 and y == N-1:
            print(c)
            break
        # \
        if lines[y][x] == '\\':
            for dx,dy in [(1,1),(-1,-1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
                    if lines[ny][nx] == '\\':
                        d.appendleft((nx,ny,c))
                    else:
                        d.append((nx,ny,c+1))
                        lines[ny][nx] = '\\'
                    visited[ny][nx] = True
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
                    if lines[ny][nx] == '/':
                        d.appendleft((nx,ny,c))
                    else:
                        d.append((nx,ny,c+1))
                        lines[ny][nx] = '/'
                    visited[ny][nx] = True
        # /
        else:
            for dx,dy in [(-1,1),(1,-1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
                    if lines[ny][nx] == '/':
                        d.appendleft((nx,ny,c))
                    else:
                        d.append((nx,ny,c+1))
                        lines[ny][nx] = '/'
                    visited[ny][nx] = True
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
                    if lines[ny][nx] == '\\':
                        d.appendleft((nx,ny,c))
                    else:
                        d.append((nx,ny,c+1))
                        lines[ny][nx] = '\\'
                    visited[ny][nx] = True

else:
    print("NO SOLUTION")

