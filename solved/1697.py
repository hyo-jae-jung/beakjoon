from sys import stdin 
from collections import deque 

N,K = map(int, stdin.readline().strip().split())

locations = [0]*(100001*2)

def bfs(graph,n,k):
    queue = deque([n])
    seen = set([n])
    while queue:
        p = queue.popleft()

        if p == k:
            return graph[p]

        for i in range(3):
            if i == 0:next_p = p-1
            elif i == 1:next_p = p+1
            else:next_p = p*2

            if next_p < 0 or next_p > 100001:continue 
            elif next_p in seen:continue 
            else:
                queue.append(next_p)
                graph[next_p] = graph[p] + 1
                seen.add(next_p)

print(bfs(locations,N,K))
