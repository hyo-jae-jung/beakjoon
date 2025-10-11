from sys import stdin   

N = int(stdin.readline().strip())
board = [list("_"*(N+2))]
for _ in range(N):
    board.append(["_"] + list(stdin.readline().strip()) + ["_"])
board.append(list("_"*(N+2)))

def is_heart(x,y):
    global board
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx=x+dx
        ny=y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return False
        if board[ny][nx] == '_':
            return False
    return True

for i in range(N+2):
    for j in range(N+2):
        if is_heart(j,i):
            heart_x,heart_y = j,i
            break

left_arm = 1
while board[heart_y][heart_x-(1+left_arm)] == '*':
    left_arm+=1

right_arm = 1
while board[heart_y][heart_x+(1+right_arm)] == '*':
    right_arm+=1

body = 1
while board[heart_y+(1+body)][heart_x] == '*':
    body+=1

left_lag = 1
while board[heart_y+body+(1+left_lag)][heart_x-1] == '*':
    left_lag+=1

right_lag = 1
while board[heart_y+body+(1+right_lag)][heart_x+1] == '*':
    right_lag+=1

print(heart_y,heart_x)
print(left_arm,right_arm,body,left_lag,right_lag)
