from sys import stdin   
from collections import deque

N = int(stdin.readline().strip())
m = []
for _ in range(N):
    m.append(list(map(int,stdin.readline().strip().split())))

ans = 'Hing'
q = deque([(0,0)])

while q:
    x,y = q.popleft()

    if x == N-1 and y == N-1:
        ans = 'HaruHaru'
        break

    d = m[y][x]
    if d:
        for dx,dy in [(d,0),(0,d)]:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                m[y][x] = 0
                q.append((x+dx,y+dy))
        
print(ans)
