from sys import stdin  
from collections import deque  

N,M = map(int,stdin.readline().strip().split())
adjacency_list = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int,stdin.readline().strip().split())
    adjacency_list[s].append((e,t))
    adjacency_list[e].append((s,t))

A,B = map(int,stdin.readline().strip().split())
d = deque([(A,2,0)])
visited = [[float('inf')]*(N+1) for _ in range(2)]
visited[0][A] = 0
visited[1][A] = 0

while d:
    s,t,c = d.popleft()
    if s == B:
        print(c)
        break
    for e,t2 in adjacency_list[s]:
        if (t3:=t+t2) == 0 or t3 >= 2:
            if visited[t2][e] > c:
                d.appendleft((e,t2,c))
                visited[t2][e] = c
        elif t3 == 1:
            if visited[t2][e] > c+1:
                d.append((e,t2,c+1))
                visited[t2][e] = c+1
