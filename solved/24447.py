from sys import stdin  
from collections import deque  

N,M,R = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,stdin.readline().strip().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

visited = [True] + [False]*N
d = [-1]*(N+1)
t = [0]*(N+1)
q = deque([(R,0)])
visited[R] = True
idx = 0
while q:
    idx+=1
    u,depth = q.popleft()
    t[u] = idx
    d[u] = depth
    for v in sorted(adjacency_list[u]):
        if not visited[v]:
            q.append((v,depth+1))
            visited[v] = True

print(sum(map(lambda x:x[0]*x[1],zip(t,d))))
