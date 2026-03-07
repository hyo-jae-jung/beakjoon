from sys import stdin  

n,m,Q = map(int,stdin.readline().strip().split())
cnt = n*m
ground = [[True]*m for _ in range(n)]
ans = []
for _ in range(Q):
    I = list(map(int,stdin.readline().strip().split()))
    if I[0] == 3:
        ans.append(cnt)
    elif I[0] == 2:
        if ground[I[1]-1][I[2]-1]:
            ans.append(0)
        else:
            ans.append(1)
    elif I[0] == 1:
        x,y = I[4]-1,I[3]-1
        dx,dy = I[2],I[1]
        
        if ground[y][x]:
            ground[y][x] = False
            cnt-=1

            while (nx:=x+dx) >= 0 and (nx:=x+dx) < m and (ny:=y+dy) >= 0 and (ny:=y+dy) < n and ground[ny][nx]:
                ground[ny][nx] = False
                cnt-=1
                x,y = nx,ny

print(*ans,sep='\n')
