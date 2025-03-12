import sys
sys.setrecursionlimit(10**5)

N,M,K = map(int,sys.stdin.readline().strip().split())
m = []
for _ in range(N):
    m.append([0 for _ in range(M)])

for _ in range(K):
    r,c = map(int,sys.stdin.readline().strip().split())
    m[r-1][c-1] = 1


def dfs(x,y):

    if m[y][x] == 0:
        return False
    
    global cnt
    
    cnt+=1
    m[y][x] = 0

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= x+dx < M and 0 <= y+dy < N:
            dfs(x+dx,y+dy)

ans = 0

for i in range(N):
    for j in range(M):
        cnt = 0
        if m[i][j] == 1:
            dfs(j,i)
            ans = max(ans,cnt)

print(ans)
