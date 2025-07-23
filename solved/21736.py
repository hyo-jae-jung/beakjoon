from sys import stdin   
from collections import deque 

N,M = map(int,stdin.readline().strip().split())
campus = [list(stdin.readline().strip()) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            q.append((i,j))

ans = 0

while q:
    y,x = q.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
            if campus[ny][nx] == 'P':
                ans+=1
            if campus[ny][nx] != 'X':
                campus[ny][nx] = 'X'
                q.append((ny,nx))

print(ans if ans > 0 else 'TT')
