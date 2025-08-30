from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
edges = list(tuple(map(int,stdin.readline().strip().split())) for _ in range(M))

dist = [float('inf')]*(N+1)
dist[1] = 0

for _ in range(N-1):
    for A,B,C in edges:
        if dist[B] > dist[A] + C:
            dist[B] = dist[A] + C

dist_ans = dist.copy()

for A,B,C in edges:
    if dist[B] > dist[A] + C:
        dist[B] = dist[A] + C
    
cycle = False
for i in range(N+1):
    if dist[i] != dist_ans[i]:
        cycle = True 
        break

if cycle:
    print(-1)
else:
    for i in dist_ans[2:]:
        print(i if i != float('inf') else -1)
