from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    graph = []
    for _ in range(2):
        graph.append(list(map(int,stdin.readline().strip().split())))
    
    for i in range(1,n):
        if i == 1:
            graph[0][i]+=graph[1][i-1]
            graph[1][i]+=graph[0][i-1]
        else:
            graph[0][i]+=max(graph[1][i-1],graph[0][i-2],graph[1][i-2])
            graph[1][i]+=max(graph[0][i-1],graph[0][i-2],graph[1][i-2])

    answer.append(max(graph[0][n-1],graph[1][n-1]))

print(*answer,sep='\n')
