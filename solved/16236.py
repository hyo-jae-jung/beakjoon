from sys import stdin   
from collections import deque
from heapq import heappush,heappop
from copy import deepcopy

N = int(stdin.readline().strip())
space = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
visited = [[False]*(N) for _ in range(N)]

feeds = []
baby_shark_loc = deque()

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby_shark_loc.append((i,j,0))
            space[i][j] = 0
            break

baby_shark_size = 2
baby_shark_score = 0
ans = 0

while baby_shark_loc:
    sample_visited = deepcopy(visited)
    move = deque()
    a = baby_shark_loc.popleft()
    move.append(a)
    feeds = []

    while move:
        y,x,t = move.popleft()
        for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < N:
                if not sample_visited[ny][nx]:
                    if space[ny][nx] == 0 or space[ny][nx] == baby_shark_size:
                        move.append((ny,nx,t+1))
                    elif space[ny][nx] < baby_shark_size:
                        heappush(feeds,(t+1,ny,nx))
                    sample_visited[ny][nx] = True

    if feeds:
        t,y,x = heappop(feeds)
        space[y][x] = 0
        ans = t
        baby_shark_loc.append((y,x,t))
        baby_shark_score+=1
        if baby_shark_size == baby_shark_score:
            baby_shark_size+=1
            baby_shark_score = 0

print(ans)
