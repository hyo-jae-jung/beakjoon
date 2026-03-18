import sys 

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
sidewalk_block = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
X = int(sys.stdin.readline().strip())

stack = [(0,0)]
start_color = sidewalk_block[0][0]
sidewalk_block[0][0] = (start_color+1)%2
ans = 'DEAD'

def jump(x,y,d):
    global sidewalk_block,stack
    cnt = 1
    while cnt <= d:
        nx = x+cnt
        ny = y
        for dx,dy in [(-1,1),(-1,-1),(1,-1),(1,1)]:
            for _ in range(1,cnt+1):
                nx+=dx
                ny+=dy
                if 0 <= nx < M and 0 <= ny < N and sidewalk_block[ny][nx] == start_color:
                    sidewalk_block[ny][nx] = (sidewalk_block[ny][nx]+1)%2
                    stack.append((nx,ny))
        cnt+=1

while stack:
    x,y = stack.pop()
    if x == M-1 and y == N-1:
        ans = 'ALIVE'
        break
    jump(x,y,X)

print(ans)
