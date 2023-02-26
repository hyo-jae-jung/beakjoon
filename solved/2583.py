import sys
sys.setrecursionlimit(10**6)
M,N,K = map(int,sys.stdin.readline().strip().split())

graph = []
for _ in range(M):
    graph.append([0]*N)

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().strip().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i] = 1

def dfs(x,y):
    if x<=-1 or x>=M or y<=-1 or y>=N:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        global cnt
        cnt+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
answer = []
for i in range(M):
    for j in range(N):
        cnt = 0
        if dfs(i,j) == True:
            result+=1
            answer.append(cnt)

print(result)
print(*sorted(answer))

