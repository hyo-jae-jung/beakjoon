from sys import stdin  
from collections import deque 

N,E = map(int,stdin.readline().strip().split())
adjaceney_list = [[[] for _ in range(N)] for _ in range(2)]
for _ in range(E):
    u,v,b = map(int,stdin.readline().strip().split())
    adjaceney_list[b][u].append(v)
    adjaceney_list[b][v].append(u)

visited = [[-1]*N for _ in range(2)]
queue = deque([(0,0),(0,1)])
visited[0][0] = 0
visited[1][0] = 0

ans = -1
while queue:   
    u,ub = queue.popleft()
    cnt = visited[ub][u]
    if u == N-1:
        ans = cnt
        break
    vb = (ub+1)%2
    for v in adjaceney_list[ub][u]:
        if visited[vb][v] == -1 or visited[vb][v] > cnt+1:
            visited[vb][v] = cnt+1
            queue.append((v,vb))

print(ans)
