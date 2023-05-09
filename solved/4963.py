import sys
sys.setrecursionlimit(10**7)

def dfs(x,y,w,h):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y,w,h)
        dfs(x-1,y-1,w,h)
        dfs(x,y-1,w,h)
        dfs(x+1,y-1,w,h)
        dfs(x+1,y,w,h)
        dfs(x+1,y+1,w,h)
        dfs(x,y+1,w,h)
        dfs(x-1,y+1,w,h)
        return True
    
    return False

answer = []

while (temp:=sys.stdin.readline().strip()) != '0 0':
    w,h = map(int,temp.split())
    graph = []
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().strip().split())))
    
    result = 0

    for i in range(w):
        for j in range(h):
            if dfs(i,j,w,h) == True:
                result+=1
    
    answer.append(result)

print(*answer,sep='\n')
