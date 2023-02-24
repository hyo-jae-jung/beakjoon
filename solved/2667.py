from sys import stdin 

N = int(stdin.readline().strip())

graph = []
for i in range(N):
    graph.append(list(map(int,stdin.readline().strip())))

def dfs(i,j):
    if i<=-1 or i>=N or j<=-1 or j>=N:
        return False
    if graph[i][j] == 1:
        graph[i][j] = 0
        global home_size
        home_size+=1
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False


homes_cnt = 0
homes_size = []
for i in range(N):
    for j in range(N):
        home_size = 0
        if dfs(i,j) == True:
            homes_cnt+=1
            homes_size.append(home_size)

print(homes_cnt)
print(*sorted(homes_size),sep='\n')
