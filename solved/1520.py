import sys
sys.setrecursionlimit(10**6)

M,N = map(int,sys.stdin.readline().strip().split())
graph = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]

def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= (nx:=x+dx) < N and 0 <= (ny:=y+dy) < M and graph[y][x] > graph[ny][nx]:
            dp[y][x]+=dfs(nx,ny)

    return dp[y][x]

print(dfs(0,0))
