from sys import stdin 
from collections import deque 

s,t = map(int,stdin.readline().strip().split())
visited = set()
queue = deque([(s,'')])
visited.add(s)

while queue:
    ns,codes = queue.popleft()
    if ns == t:
        print(codes if codes else 0)
        break

    if ns*ns <= t and ns*ns not in visited:
        visited.add(ns*ns)
        queue.append((ns*ns,codes+'*'))

    if ns+ns <= t and ns+ns not in visited:
        visited.add(ns+ns)
        queue.append((ns+ns,codes+'+'))

    if 1 not in visited:
        visited.add(1)
        queue.append((1,codes+'/'))
else:
    print(-1)

