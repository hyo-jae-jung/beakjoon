from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
r1,c1,r2,c2 = map(int,stdin.readline().strip().split())
visited = [[False]*N for _ in range(N)]

q = deque([(c1,r1,0)])
visited[r1][c1] = True

ans = -1

while q:
    x,y,cnt = q.popleft()
    if x == c2 and y == r2:
        ans = cnt
        break

    for dx,dy in [(-1,-2),(1,-2),(-2,0),(2,0),(-1,2),(1,2)]:
        if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
            visited[ny][nx] = True
            q.append((nx,ny,cnt+1))

print(ans)
