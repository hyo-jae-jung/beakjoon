from sys import stdin 
from collections import defaultdict 

N,M = map(int,stdin.readline().strip().split())
graph = defaultdict(list)

for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

seen = [False]+[True]*N
cnt = 0
i=1
while i <= N:

    if seen[i]:
        stack = [i]

        while stack:
            p = stack.pop()
            if seen[p]:
                seen[p] = False
                stack.extend(list(reversed(graph[p])))
        else:
            cnt+=1
    i+=1

print(cnt)
