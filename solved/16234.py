from sys import stdin   

N,L,R = map(int,stdin.readline().strip().split())
land = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[-1]*N for _ in range(N)]
    k = 0
    u = {}
    for i in range(N):
        for j in range(N):
            if visited[i][j] < 0:
                
                stack_loc = [(i,j)]
                stack_val = [land[i][j]]
                visited[i][j] = k

                while stack_loc:

                    y,x = stack_loc.pop()
                    
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < N:
                            if visited[ny][nx] != k:
                                if L <= abs(land[y][x] - land[ny][nx]) <= R:
                                    stack_loc.append((ny,nx))
                                    stack_val.append(land[ny][nx])
                                    visited[ny][nx] = k

                u.update({k:sum(stack_val)//len(stack_val)})
                k+=1
    
    if k == N**2:
        break
    
    for i in range(N):
        for j in range(N):
            land[i][j] = u[visited[i][j]]
    ans+=1

print(ans)
