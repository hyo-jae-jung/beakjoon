def dfs(graph,x,y,f,num):
    global N,M
    result = [(x,y)]
    stack = [(x,y)]
    graph[y][x] = num

    while stack:
        x,y = stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < M and 0 <= (ny:=y+dy) < N:
                if graph[ny][nx] == f:
                    graph[ny][nx] = num
                    stack.append((nx,ny))
                    result.append((nx,ny))
    
    return result

def identify_island(graph):
    global N,M
    result = {}
    num = 2
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                result.update({num:dfs(graph,j,i,1,num)})
                num+=1
    return result

from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
adjacency_matrix = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

islands = identify_island(adjacency_matrix)

def find_bridge(graph,x,y):
    global edges,N,M
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        time = 1
        while True:
            ny = y+dy*time
            nx = x+dx*time
            if any([not (0 <= ny < N),not (0 <= nx < M)]):
                break

            if graph[ny][nx] == graph[y][x]:
                break

            if graph[ny][nx] > 0:
                if time > 2:
                    tmp = [time-1] + sorted([(x,y),(nx,ny)])
                    edges.add(tuple(tmp))
                break

            if graph[ny][nx] == 0:
                time+=1
                continue

edges = set()
for value in islands.values():
    for x,y in value:
        find_bridge(adjacency_matrix,x,y)

edges = sorted(list(edges))
parent = list(range(len(islands)+2))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

ans = 0
bridge_cnt = 0
for d,loc1,loc2 in edges:
    x1,y1 = loc1
    x2,y2 = loc2
    if (a:=find_parent(parent,adjacency_matrix[y1][x1])) != (b:=find_parent(parent,adjacency_matrix[y2][x2])):
        ans+=d
        bridge_cnt+=1
        union_parent(parent,a,b)

if bridge_cnt == len(islands.keys()) - 1:
    print(ans)
else:
    print(-1)
