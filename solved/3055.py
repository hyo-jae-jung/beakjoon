from sys import stdin
from collections import deque 

R,C = map(int,stdin.readline().strip().split())
chart = []
for _ in range(R):
    chart.append(list(stdin.readline().strip()))

queue = deque()

temp = deque()
for i in range(R):
    for j in range(C):
        if chart[i][j] == '*':
            queue.append((j,i))
        if chart[i][j] == 'S':
            chart[i][j] = 0
            temp.append((j,i))
else:
    queue.extendleft(temp)

def bfs():
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < C and 0 <= ny < R:
                if chart[y][x] == '*':
                    if chart[ny][nx] not in ['X','D','*']:
                        chart[ny][nx] = '*'
                        queue.append((nx,ny))
                elif isinstance(chart[y][x],int):
                    if chart[ny][nx] == 'D':
                        return chart[y][x]+1
                    if chart[ny][nx] == '.':
                        chart[ny][nx] = chart[y][x] + 1
                        queue.append((nx,ny))          
    else:
        return 'KAKTUS'
        
print(bfs())
