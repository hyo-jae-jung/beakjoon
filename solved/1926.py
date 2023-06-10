import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().strip().split())
paper = []
for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().strip().split())))

def dfs(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    
    if paper[y][x] == 1:
        paper[y][x] = 0
        global area
        area+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
space,cnt = 0,0

for i in range(n):
    for j in range(m):
        area = 0
        if dfs(j,i) == True:
            cnt+=1
            space = max(space,area)
            
print(cnt,space,sep='\n')
