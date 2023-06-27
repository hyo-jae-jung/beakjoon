from sys import stdin 
from collections import deque,defaultdict

N = int(stdin.readline().strip())
K = int(stdin.readline().strip())
chart = []
for _ in range(N):
    chart.append([[0,0]]*N)
    
for _ in range(K):
    y,x = map(int,stdin.readline().strip().split())
    chart[y-1][x-1] = 'apple'

L = int(stdin.readline().strip())
direction_change_time = defaultdict(str)
for _ in range(L):
    X,C = stdin.readline().strip().split()
    direction_change_time[int(X)] = C
chart[0][0] = [1,0]
directions = [(1,0),(0,1),(-1,0),(0,-1)]

queue = deque([(0,0)])
while queue:
    x,y = queue[0]
    c,d = chart[y][x]
    dx,dy = directions[d%4]
    nx = x+dx
    ny = y+dy
    if not all([0<=nx<N,0<=ny<N,(nx,ny) not in queue]):
        print(c)
        break
    
    if chart[ny][nx] == 'apple':
        queue.appendleft((nx,ny))
    else:
        queue.append((nx,ny))    
        queue.popleft()
        
    if direction_change_time[c] == 'D':
        d+=1
    elif direction_change_time[c] == 'L':
        d-=1
    chart[ny][nx] = [c+1,d]
