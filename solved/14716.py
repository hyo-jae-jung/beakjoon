import sys
sys.setrecursionlimit(10**7)

M,N = map(int,sys.stdin.readline().strip().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,sys.stdin.readline().strip().split())))

def dfs(x,y):

    if x < 0 or y < 0 or x >= N or y >= M:
        return False

    if arr[y][x] == 0:    
        return False
    
    if arr[y][x]:
        arr[y][x] = 0
        dfs(x-1,y-1)
        dfs(x,y-1)
        dfs(x+1,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x-1,y+1)
        dfs(x,y+1)
        dfs(x+1,y+1)
        return True
    return False

ans = 0
for i in range(M):
    for j in range(N):
        if dfs(j,i):
            ans+=1

print(ans)
