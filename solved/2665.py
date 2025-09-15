from sys import stdin  
from collections import deque 

n = int(stdin.readline().strip())
rooms = [list(map(int,list(stdin.readline().strip()))) for _ in range(n)]
check_cnt = [[float('inf')]*n for _ in range(n)]

q = deque()
q.append((0,0,0)) # x,y,break_cnt
ans = float('inf')

while q:
    x,y,break_cnt = q.popleft()
    if x == n-1 and y == n-1:
        ans = min(ans,break_cnt)
        continue

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < n and 0 <= (ny:=y+dy) < n:
            if check_cnt[ny][nx] > (b:=break_cnt + (1 if rooms[ny][nx] == 0 else 0)):
                q.append((nx,ny,b))
                check_cnt[ny][nx] = b
            
print(ans)
