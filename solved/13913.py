import sys
from collections import deque 

N,K = map(int, sys.stdin.readline().strip().split())
visited_time = [1e6]*100001
visited_time[N] = 0
max_time = 1e6
q = deque([([N],0)])
ans = []
while q:
    X,sec = q.popleft()
    
    if X[sec] == K:
        ans = X
        max_time = sec

    if X[sec] > K and max_time > sec+(X[-1]-K):
        ans = X + list(range(X[-1]-1,K-1,-1))
        max_time = sec+(X[-1]-K)
        continue

    if sec < max_time:
        if 0 < X[-1] <= K and X[-1]*2 <= 100000:
            if visited_time[X[-1]*2] > visited_time[X[-1]] and visited_time[X[-1]*2] > sec:
                visited_time[X[-1]*2] = sec+1
                q.append((X+[X[-1]*2],sec+1))
        if X[-1]-1 >= 0 and visited_time[X[-1]-1] > visited_time[X[-1]] and visited_time[X[-1]-1] > sec:
            visited_time[X[-1]-1] = sec+1
            q.append((X+[X[-1]-1],sec+1))
        if X[-1]+1 <= 100000 and visited_time[X[-1]+1] > visited_time[X[-1]] and visited_time[X[-1]+1] > sec:
            visited_time[X[-1]+1] = sec+1
            q.append((X+[X[-1]+1],sec+1))

print(max_time)
print(*ans)
