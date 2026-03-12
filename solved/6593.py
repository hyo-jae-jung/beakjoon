from sys import stdin 
from collections import deque

ans = []
while (I:=stdin.readline().strip()) != '0 0 0':
    L,R,C = map(int,I.split())
    
    # build building
    building = []
    for _ in range(L):
        tmp = []
        for _ in range(R):
            tmp.append(list(stdin.readline().strip()))
        building.append(tmp)
        stdin.readline().strip()

    # find S,E
    queue = deque()
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    end = []

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    queue.append((k,j,i,0))
                    visited[i][j][k] = True
                    continue

                if building[i][j][k] == 'E':
                    building[i][j][k] = '.'
                    end.append(k)
                    end.append(j)
                    end.append(i)

    # escape building
    while queue:
        x,y,z,minute = queue.popleft()
        if end[0] == x and end[1] == y and end[2] == z:
            ans.append(f"Escaped in {minute} minute(s).")
            break

        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if 0 <= (nx:=x+dx) < C and 0 <= (ny:=y+dy) < R and 0 <= (nz:=z+dz) < L \
                and visited[nz][ny][nx] == False and building[nz][ny][nx] == '.':
                visited[nz][ny][nx] = True
                queue.append((nx,ny,nz,minute+1))
    else:
        ans.append("Trapped!")

print(*ans,sep='\n')
