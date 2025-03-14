import sys
from collections import deque 

N,K = map(int, sys.stdin.readline().strip().split())
visited_time = [1e6]*100001
visited_time[N] = 0
max_time = 1e6
q = deque([(N,0)])

while q:
    x,sec = q.popleft()
    
    if x == K:
        max_time = sec

    if visited_time[x] < max_time:
        if x-1 >=0 and visited_time[x]+1 < visited_time[x-1]:
            visited_time[x-1] = visited_time[x]+1
            q.append((x-1,sec+1))
        if x+1 <=100000 and visited_time[x]+1 < visited_time[x+1]:
            visited_time[x+1] = visited_time[x]+1
            q.append((x+1,sec+1))
        if 0 < x <= K and x*2 <= 100000 and visited_time[x] < visited_time[2*x]:
            visited_time[2*x] = visited_time[x]
            q.append((2*x,sec))

print(visited_time[K])
