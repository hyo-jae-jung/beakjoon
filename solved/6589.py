from sys import stdin 
from heapq import heappop,heappush

ans = []
i = 1
while (I:=stdin.readline().strip()) != '0 0':
    n,r = map(int,I.split())
    graph = {}
    keys = set()
    for _ in range(r):
        s,d,w = stdin.readline().strip().split()
        if not graph.get(s):
            graph.update({s:[]})
        graph[s].append((d,int(w)))
        if not graph.get(d):
            graph.update({d:[]})
        graph[d].append((s,int(w)))
        
        keys.add(s)
        keys.add(d)

    visited = {}
    for key in keys:
        visited.update({key:0})
    
    start,end = stdin.readline().strip().split()
    priority_queue = [(-float('inf'),start)]
    visited[start] = float('inf')

    while priority_queue:
        tons,u = heappop(priority_queue)
        if u == end:
            ans.append(f"Scenario #{i}\n{-tons} tons\n")
            break

        for v,t in graph[u]:
            if (m:=min(t,-tons)) > visited[v]:
                visited[v] = m
                heappush(priority_queue,(-m,v))
    i+=1

print(*ans,sep='\n')
