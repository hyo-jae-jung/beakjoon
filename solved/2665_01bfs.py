from sys import stdin  
from collections import deque  

n = int(stdin.readline().strip())
rooms = [list(stdin.readline().strip()) for _ in range(n)]

d = deque()
d.appendleft((0,0,0))
ans = float('inf')
while d:
    x,y,c = d.popleft()

    if x == n-1 and y == n-1:
        print(c)
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < n and 0 <= (ny:=y+dy) < n:
            if rooms[ny][nx] == '1':
                d.appendleft((nx,ny,c))
            elif rooms[ny][nx] == '0':
                d.append((nx,ny,c+1))
            rooms[ny][nx] = 2
