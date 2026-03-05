from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,stdin.readline().strip().split())
    adjacency_list[A].append((C,B))
    adjacency_list[B].append((C,A))
start,end = map(int,stdin.readline().strip().split())

priority_queue = []
heappush(priority_queue,(-float('inf'),start))
weight = [0]*(N+1)

while priority_queue:
    m,u = heappop(priority_queue)

    if u == end:
        print(-m)
        break

    for c,v in adjacency_list[u]:
        if weight[v] < c:
            weight[v] = c
            heappush(priority_queue,(max(-c,m),v))

