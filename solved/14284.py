from sys import stdin   

n,m = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    adjacency_list[a].append((b,c))
    adjacency_list[b].append((a,c))

s,t = map(int,stdin.readline().strip().split())

from heapq import heappop,heappush

dist = [float('inf')]*(n+1)
dist[s] = 0
h = [(0,s)]

while h:
    d,n = heappop(h)

    if n == t:
        print(d)
        break 

    for n2,d2 in adjacency_list[n]:
        if dist[n2] > d + d2:
            dist[n2] = d + d2
            heappush(h,(dist[n2],n2))

