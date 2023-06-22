from sys import stdin 
from collections import deque 

M,N,H = map(int,stdin.readline().strip().split())

box = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int,stdin.readline().strip().split())))
    box.append(temp)

def check_riped(arr,x,y,z):
    for i in range(z):
        for j in range(y):
            for k in range(x):
                if arr[i][j][k] == 0:
                    return False
    return True

def start_riped(arr,x,y,z):
    answer = deque()
    for i in range(z):
        for j in range(y):
            for k in range(x):
                if arr[i][j][k] == 1:
                    answer.append((k,j,i,0))
    return answer

answer = 0

def bfs():
    queue = start_riped(box,M,N,H)
    global answer
    directions = [(-1,0,0),
    (0,-1,0),
    (0,0,-1),
    (1,0,0),
    (0,1,0),
    (0,0,1),]
    while queue:
        x,y,z,cnt = queue.popleft()
        if cnt > answer:
            answer = cnt
        for dx,dy,dz in directions:
            nx = x+dx
            ny = y+dy
            nz = z+dz
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1
                queue.append((nx,ny,nz,cnt+1))

bfs()
print(answer if check_riped(box,M,N,H) else -1)
