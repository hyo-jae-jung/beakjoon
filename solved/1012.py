import sys
sys.setrecursionlimit(10**7)

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    if earth[x][y] == 1:
        earth[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

answer = []

T = int(sys.stdin.readline().strip())
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().strip().split())
    earth = [[0]*M for _ in range(N)]

    for _ in range(K):
        Y,X = map(int,sys.stdin.readline().strip().split())
        earth[X][Y] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                result+=1
                
    answer.append(result)
    
print(*answer,sep='\n')
