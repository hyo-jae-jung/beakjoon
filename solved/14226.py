from sys import stdin 
from collections import deque 

S = int(stdin.readline().strip())
visited = [[False]*(S+1) for _ in range(S+1)]
queue = deque([(0,1,0)])
visited[1][0] = True

while queue:
    t,s,c = queue.popleft()

    if s == S:
        print(t)
        break

    if not visited[s][s]:
        visited[s][s] = True
        queue.append((t+1,s,s))

    if c > 0 and s+c <= S and not visited[s+c][c]:
        visited[s+c][c] = True
        queue.append((t+1,s+c,c))

    if s > 0 and not visited[s-1][c]:
        visited[s-1][c] = True
        queue.append((t+1,s-1,c))

