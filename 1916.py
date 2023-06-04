from sys import stdin 

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((b,c))

start,end = map(int,stdin.readline().strip().split())

visited = [True]*(N+1)
min_val = int(1e9)

def min_value(start,end,value=0):
    global min_val
    visited[start] = False
    for i,j in graph[start]:
        if i == end:
            min_val = min(min_val,value+j)
        elif visited[i]:
            min_value(i,end,value+j)

if start == end:
    print(0)
else:
    min_value(start,end)
    print(min_val)
