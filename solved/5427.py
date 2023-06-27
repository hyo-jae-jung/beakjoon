from sys import stdin 
from collections import deque 

T = int(stdin.readline().strip())
answer = []

def bfs():
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if isinstance(chart[y][x],int):
                if not all([0 <= nx < w, 0 <= ny < h]):
                    return chart[y][x] + 1
                if chart[ny][nx] == '.':
                    chart[ny][nx] = chart[y][x] + 1
                    queue.append((nx,ny))
            elif chart[y][x] == '*':
                if all([0 <= nx < w, 0 <= ny < h]):
                    if chart[ny][nx] == '.' or isinstance(chart[ny][nx],int):
                        chart[ny][nx] = '*'
                        queue.append((nx,ny))
    else:
        return "IMPOSSIBLE"
    
for _ in range(T):
    w,h = map(int,stdin.readline().strip().split())
    chart = []
    for _ in range(h):
        chart.append(list(stdin.readline().strip()))

    queue = deque()
    temp = deque()
    for i in range(h):
        for j in range(w):
            if chart[i][j] == '*':
                queue.append((j,i))
            if chart[i][j] == '@':
                temp.append((j,i))
                chart[i][j] = 0
    else:
        queue.extendleft(temp)

    answer.append(bfs())

print(*answer,sep='\n')
