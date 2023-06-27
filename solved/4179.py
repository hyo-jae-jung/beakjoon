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
        if chart[i][j] == 'F':
            queue.append((j,i))
        if chart[i][j] == 'J':
            temp.append((j,i))
            chart[i][j] = 0
else:
    queue.extendleft(temp)

def bfs():
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if isinstance(chart[y][x],int):
                if not all([0 <= nx < C, 0 <= ny < R]):
                    return chart[y][x] + 1
                if chart[ny][nx] == '.':
                    chart[ny][nx] = chart[y][x] + 1
                    queue.append((nx,ny))
            elif chart[y][x] == 'F':
                if all([0 <= nx < C, 0 <= ny < R]):
                    if chart[ny][nx] == '.' or isinstance(chart[ny][nx],int):
                        chart[ny][nx] = 'F'
                        queue.append((nx,ny))
    else:
        return "IMPOSSIBLE"

print(bfs())
