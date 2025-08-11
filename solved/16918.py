from sys import stdin   

R,C,N = map(int,stdin.readline().strip().split())
board = list(list(stdin.readline().strip()) for _ in range(R))

arr = []
for i in range(R):
    tmp = []
    for j in range(C):
        if board[i][j] == '.':
            tmp.append(0)
        else:
            tmp.append(3)
    arr.append(tmp)

loc = []
cnt = 0
while cnt < N:
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                arr[i][j]-=1
                if arr[i][j] == 0:
                    loc.append((j,i))
    if cnt%2 == 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 0:
                    arr[i][j] = 3
    while loc:
        x,y = loc.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < C and 0 <= (ny:=y+dy) < R:
                arr[ny][nx] = 0
    cnt+=1

ans = []
for i in range(R):
    tmp = ''
    for j in range(C):
        if arr[i][j] > 0:
            tmp+='O'
        else:
            tmp+='.'
    ans.append(tmp)

print(*ans,sep='\n')
