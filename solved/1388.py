from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
floor = []
for _ in range(N):
    floor.append(list(stdin.readline().strip()))

ans = 0
def dfs(x,y):

    tmp = floor[y][x]
    floor[y][x] = True

    if tmp == '-':
        if x+1 < M:
            if tmp == floor[y][x+1]:
                dfs(x+1,y)
                return True
            
    if tmp == '|':
        if y+1 < N:
            if tmp == floor[y+1][x]:
                dfs(x,y+1)
                return True


for i in range(N):
    for j in range(M):
        if floor[i][j] != True:
            dfs(j,i)
            ans+=1

print(ans)
