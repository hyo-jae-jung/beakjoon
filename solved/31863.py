from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
board = [list(stdin.readline().strip()) for _ in range(N)]
building_cnt = 0
stack = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            board[i][j] = 0
        elif board[i][j] == '*':
            board[i][j] = 1
            building_cnt+=1
        elif board[i][j] == '#':
            board[i][j] = 2
            building_cnt+=1
        elif board[i][j] == '|':
            board[i][j] = -1
        elif board[i][j] == '@':
            start = (j,i)
            board[i][j] = 0

for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
    for d in range(1,3):
        if 0 <= (nx:=start[0]+dx*d) < M and 0 <= (ny:=start[1]+dy*d) < N:
            if board[ny][nx] > 0:
                stack.append((nx,ny))
            elif board[ny][nx] == 0:
                continue
            else:
                break

break_cnt = 0
while stack:
    x,y = stack.pop()

    if board[y][x] > 0:
        board[y][x]-=1

        if board[y][x] == 0:
            break_cnt+=1

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and board[ny][nx] > 0:
                    stack.append((nx,ny))

print(break_cnt,building_cnt-break_cnt)
