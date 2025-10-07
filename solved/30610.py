from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
places = [list(stdin.readline().strip()) for _ in range(N)]

ans = []
def dfs(x,y):

    global places
    stack = [(x,y)]
    places[y][x] = '0'
    result = 1

    while stack:
        x,y = stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
                if places[ny][nx] == '1':
                    stack.append((nx,ny))
                    places[ny][nx] = '0'
                    result+=1

    return result

for i in range(N):
    for j in range(M):
        if places[i][j] == '1':
            ans.append(dfs(j,i))

print(len(ans))
print(*sorted(ans))
