from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
graph = [[0]*(N+1)]
for _ in range(N):
    temp= [0] + list(map(int,stdin.readline().strip().split()))
    graph.append([i+j for i,j in zip(graph[-1],temp)])
    
for i in range(1,N+1):
    for j in range(1,N+1):
        graph[i][j]+=graph[i][j-1]
        
answer = []
for _ in range(M):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    answer.append(graph[x2][y2]-graph[x1-1][y2]-graph[x2][y1-1]+graph[x1-1][y1-1])

print(*answer,sep='\n')
