from sys import stdin   
from collections import deque  

N,M,T = map(int,stdin.readline().strip().split())
m = []
for _ in range(N):
    m.append(list(map(int,stdin.readline().strip().split())))

mm = []
for _ in range(N):
    mm.append([True]*M)

q = deque([(0,0)])
gram = 10001
no_gram = 'Fail'

while q:
    x,y = q.popleft()
    mm[y][x] = False

    if x == M-1 and y == N-1:
        no_gram = -m[y][x]
        break

    if -m[y][x] >= T:
        break

    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0 <= x+dx < M and 0 <= y+dy < N:
            
            if m[y+dy][x+dx] == 0 and mm[y+dy][x+dx]:
                m[y+dy][x+dx] = m[y][x]-1
                mm[y+dy][x+dx] = False
                q.append((x+dx,y+dy))

            elif m[y+dy][x+dx] == 2:
                m[y+dy][x+dx] = m[y][x]-1
                gram = -m[y+dy][x+dx] + N-1-(y+dy) + M-1-(x+dx)
                break

if no_gram == 'Fail':
    if gram <= T:
        ans = gram
    else:
        ans = no_gram
else:
    if no_gram <= T and gram <= T:
        ans = min(no_gram,gram)
    elif no_gram <= T and gram > T:
        ans = no_gram
    elif no_gram > T and gram <= T:
        ans = gram
    else:
        ans = 'Fail'

print(ans)
