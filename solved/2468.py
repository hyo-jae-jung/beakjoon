import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())
maps = []
max_level = 0
min_level = 0
for _ in range(N):
    temp = [int(i) for i in sys.stdin.readline().strip().split()]
    maxl = max(temp)
    minl = min(temp)
    if maxl > max_level:
        max_level = maxl
    if minl < min_level:
        min_level = minl
    maps.append(temp)

def dfs(i,j):
    if i<=-1 or i>=N or j<=-1 or j>=N:
        return False
    if graph[i][j] > temp_level:
        graph[i][j] = 0
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False

answer = []
for temp_level in range(min_level,max_level+1):

    result = 0
    graph = []
    for i in maps:
        graph.append(i.copy())

    for i in range(N):
        for j in range(N):
            if dfs(i,j) == True:
                result+=1

    answer.append(result)

print(max(answer))
