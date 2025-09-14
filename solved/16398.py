from sys import stdin  
from heapq import heappop, heappush

N = int(stdin.readline().strip())
adjacency_matrix = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

ans = 0
start = 0
visited = set()
h = [(0,start)]
VG = set(range(N))

while h or VG - visited:
    w,u = heappop(h)

    if u in visited:
        continue

    ans+=w
    visited.add(u)

    for v in range(N):
        if adjacency_matrix[u][v] and v not in visited:
            heappush(h,(adjacency_matrix[u][v],v))

print(ans)
