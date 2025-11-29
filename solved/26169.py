from sys import stdin 

board = [list(map(int,stdin.readline().strip().split())) for _ in range(5)]
r,c = map(int,stdin.readline().strip().split())

ans = 0

def solution(x,y,move_cnt=0,apple=0):
    global board,ans
    if apple > 1:
        ans = 1
        return
    
    if move_cnt == 3:
        return
    
    if ans == 0:
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < 5 and 0 <= (ny:=y+dy) < 5 and board[ny][nx] >= 0:
                    tmp = board[ny][nx]
                    board[ny][nx] = -1
                    solution(nx,ny,move_cnt+1,apple+tmp)
                    board[ny][nx] = tmp

tmp = board[r][c]
board[r][c] = -1
solution(c,r,move_cnt=0,apple=tmp)
print(ans)
