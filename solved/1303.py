import sys 
sys.setrecursionlimit(10**6)

N,M = map(int,sys.stdin.readline().strip().split())
arr = []
for _ in range(M):
    arr.append(list(sys.stdin.readline().strip()))

w,b = [],[]
cnt = 0

def dfs(x,y,s):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False

    if arr[y][x] == 'C':
        return False
    
    if arr[y][x] == s:
        arr[y][x] = 'C'
        global cnt
        cnt+=1
        dfs(x-1,y,s=s)
        dfs(x,y-1,s=s)
        dfs(x,y+1,s=s)
        dfs(x+1,y,s=s)
        return True
    return False

for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W':
            dfs(j,i,'W')
            w.append(cnt)

        elif arr[i][j] == 'B':
            dfs(j,i,'B')
            b.append(cnt)

        cnt = 0

print(sum(map(lambda x:x**2,w)),sum(map(lambda x:x**2,b)))
