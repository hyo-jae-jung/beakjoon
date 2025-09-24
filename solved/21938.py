from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
image = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
T = int(stdin.readline().strip())

ans = 0
def dfs(x,y):

    global image,T
    stack = [(x,y)]
    image[y][x] = 0
    image[y][x+1] = 0
    image[y][x+2] = 0

    while stack:
        x,y = stack.pop()
        for dx,dy in [(-3,0),(3,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < 3*M-2 and 0 <= (ny:=y+dy) < N:
                if (image[ny][nx]+image[ny][nx+1]+image[ny][nx+2])/3 >= T:
                    stack.append((nx,ny))
                    image[ny][nx] = 0
                    image[ny][nx+1] = 0
                    image[ny][nx+2] = 0
                    
for i in range(N):
    for j in range(0,M*3,3):
        if (image[i][j] + image[i][j+1] + image[i][j+2])/3 >= T:
            ans+=1
            dfs(j,i)

print(ans)
