import sys 
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline().strip())
graph = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

ans = 0
def dfs(x=1,y=0,s=1):
    
    if x == N-1 and y == N-1:
        global ans
        ans+=1
        return True
    
    if x+1 < N and y+1 < N and graph[y][x+1] == 0 and graph[y+1][x] == 0 and graph[y+1][x+1] == 0:
        dfs(x+1,y+1,3)

    if s == 1 or s == 3:
        if x+1 < N and graph[y][x+1] == 0:
            dfs(x+1,y,1)

    if s == 2 or s == 3:
        if y+1 < N and graph[y+1][x] == 0:
            dfs(x,y+1,2)

dfs()
print(ans)
