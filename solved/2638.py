from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
board = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
board_air = [[0]*M for _ in range(N)]

def air(stack):
    global board,board_air,N,M
    while stack:
        x,y = stack.pop()
        board_air[y][x] = 2
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N and board[ny][nx] == 0 and board_air[ny][nx] == 0:
                board_air[ny][nx] = 2
                stack.add((nx,ny))

# find_cheese
cheese = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese.add((j,i))

def find_exposed_cheese():
    global board_air,cheese
    d_stack = set()

    def delete_cheese(x,y):
        air_cnt = 0
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if board_air[y+dy][x+dx] == 2:
                air_cnt+=1
        if air_cnt > 1:
            d_stack.add((x,y))

    for x,y in cheese:
        delete_cheese(x,y)

    return d_stack

ans = 0
air(set([(0,0)]))

while cheese:
    exposed_cheese = find_exposed_cheese()
    cheese-=exposed_cheese
    air(exposed_cheese)
    ans+=1

print(ans)
