from sys import stdin  
from collections import deque  

N,M = map(int,stdin.readline().strip().split())
y1,x1,y2,x2 = map(int,stdin.readline().strip().split())
class_room = [list(stdin.readline().strip()) for _ in range(N)]

d = deque([(x1-1,y1-1,0)])
class_room[y1-1][x1-1] = 'v'

while d:
    x,y,c = d.popleft()
    if x == x2-1 and y == y2-1:
        print(c)
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
            if class_room[ny][nx] == '0':
                d.appendleft((nx,ny,c))
            elif class_room[ny][nx] == '1' or class_room[ny][nx] == '#':
                d.append((nx,ny,c+1))
            class_room[ny][nx] = 'v'
