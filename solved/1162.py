from sys import stdin 
from heapq import heappop,heappush

N,M,K = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,t = map(int,stdin.readline().strip().split())
    adjacency_list[u].append((t,v))
    adjacency_list[v].append((t,u))

distance = [[float('inf')]*(N+1) for _ in range(K+1)]
priority_queue = [(0,1,K)]
distance[K][0] = 0
ans = float('inf')

while priority_queue:
    st,u,k = heappop(priority_queue)

    if st > distance[k][u]:
        continue

    if u == N:
        ans = min(ans,st)
        continue

    for t,v in adjacency_list[u]:
        if distance[k][v] > (nt:=t+st):
            distance[k][v] = nt
            heappush(priority_queue,(nt,v,k))
        
        if k > 0:
            if distance[k-1][v] > st:
                distance[k-1][v] = st
                heappush(priority_queue,(st,v,k-1))

print(ans)
