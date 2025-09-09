from sys import stdin  
from heapq import heappop,heappush

N,D = map(int,stdin.readline().strip().split())
h = []
arr = set([0,D])
adjacency_list = {}
for _ in range(N):
    start,end,dist = map(int,stdin.readline().strip().split())
    if end <= D and dist < end - start:
        if not adjacency_list.get(start):
            adjacency_list.update({start:[]})
        adjacency_list[start].append((end,dist))
        arr.add(end)
        arr.add(start)

arr = sorted(list(arr))
for i in range(1,len(arr)):
    if not adjacency_list.get(arr[i-1]):
            adjacency_list.update({arr[i-1]:[]})
    adjacency_list[arr[i-1]].append((arr[i],arr[i] - arr[i-1]))

h = [(0,0)]
dist = {0:0}

while h:
    d,u = heappop(h)
    if u == D:
        print(d)
        break

    for v,d2 in adjacency_list[u]:
        if not dist.get(v):
            dist.update({v:float('inf')})
        if dist[v] > d + d2:
            dist[v] = d + d2
            heappush(h,(dist[v],v))
