from sys import stdin 
from collections import deque 

M,N = map(int,stdin.readline().strip().split())
box = []
for _ in range(N):
    box.append(list(map(int,stdin.readline().strip().split())))

def check_riped(arr,x,y):
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 0:
                return False
    return True

def start_riped(arr,x,y):
    answer = deque()
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1:
                answer.append((j,i,0))
    return answer

answer = 0
def bfs():
    queue = start_riped(box,M,N)
    global answer
    
    while queue:
        x,y,cnt = queue.popleft()
        if cnt > answer:
            answer = cnt
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                box[ny][nx] = 1
                queue.append((nx,ny,cnt+1))

bfs()
print(answer if check_riped(box,M,N) else -1)
