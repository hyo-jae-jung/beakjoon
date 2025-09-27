from sys import stdin  
from copy import deepcopy

N,M = map(int,stdin.readline().strip().split())
board = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

def melt_cheese(board):
    visited = [[False]*M for _ in range(N)]
    board_sample = deepcopy(board)

    stack = [(0,0)]
    visited[0][0] = True

    while stack:
        x,y = stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and not visited[ny][nx]:
                if board_sample[ny][nx] == 1:
                    board_sample[ny][nx] = 0
                else:
                    stack.append((nx,ny))
                visited[ny][nx] = True

    return board_sample

def dose_cheese_exist(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                return True
    return False

time = 0
if not dose_cheese_exist(board):
    print(0)
    print(0)
else:
    while dose_cheese_exist(new_board:=melt_cheese(board)):
        board = deepcopy(new_board)
        time+=1
    else:
        time+=1
        def dfs(x,y):
            cnt = 1
            stack = [(x,y)]
            board[y][x] = 0

            while stack:
                x,y = stack.pop()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
                        if board[ny][nx] == 1:
                            board[ny][nx] = 0
                            stack.append((nx,ny))
                            cnt+=1
            return cnt
        
        ans = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    ans+=dfs(j,i)
                    
    print(time)
    print(ans)
