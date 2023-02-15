from sys import stdin 
from collections import defaultdict, deque 

N,M,V = map(int,stdin.readline().strip().split())

temp_list = []
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    temp_list.append((a,b))
    temp_list.append((b,a))

temp_list.sort(key=lambda x:(x[0],x[1]))

hash = defaultdict(list)
for i,j in temp_list:
    hash[i].append(j)

def dfs(graph,v):
    answer = []
    visited = [False]*(N+1)
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            answer.append(v)
            stack.extend(list(reversed(graph[v])))
    return answer
    
def bfs(graph,v):
    answer = []
    visited = [False]*(N+1)
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            answer.append(v)
            queue.extend(graph[v])
    return answer

print(*dfs(hash,V))
print(*bfs(hash,V))
