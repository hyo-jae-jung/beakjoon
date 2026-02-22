from sys import stdin 
from collections import deque 

start_bin = int(stdin.readline().strip(),2)
goal_bin = int(stdin.readline().strip(),2)

q = deque()
q.append((start_bin,0))
visited = [False]*1024
visited[start_bin] = True

while q:
    b,cnt = q.popleft()
    if b == goal_bin:
        print(cnt)
        break

    if 0 < b and not visited[b-1]:
        visited[b] = True
        q.append((b-1,cnt+1))
    
    if b < 1023 and not visited[b+1]:
        visited[b] = True
        q.append((b+1,cnt+1))
    
    for i in range(len(bin(b)[2:])-1):
        sign:int
        if b & (1 << i):
            sign = -1
        else:
            sign = 1
        if not visited[(nb:=b+sign*(1<<i))]:
            visited[nb] = True
            q.append((nb,cnt+1))
            
