import sys
sys.setrecursionlimit(10**5)

M,N = map(int,sys.stdin.readline().strip().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,sys.stdin.readline().strip().split())))
    
answer = 0

def bfs(x=0,y=0,val=10000):
    if x == N-1 and y == M-1:
        global answer
        answer+=1
        return True
    
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < M and val > arr[ny][nx]:
            bfs(nx,ny,arr[ny][nx])
     
bfs()       
print(answer)
