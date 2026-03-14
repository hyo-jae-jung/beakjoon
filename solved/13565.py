from sys import stdin  

M,N = map(int,stdin.readline().strip().split())
fiber = [list(stdin.readline().strip()) for _ in range(M)]

stack = []
for i in range(N):
    if fiber[0][i] == '0':
        stack.append((i,0))

ans = 'NO'

while stack:
    x,y = stack.pop()

    if y == M-1:
        ans = 'YES'
        break

    if fiber[y][x] == '1':
        continue
    fiber[y][x] = '1'

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < M and fiber[ny][nx] == '0':
            stack.append((nx,ny))

print(ans)
