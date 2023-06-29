from sys import stdin 
from collections import deque

N,K = map(int, stdin.readline().strip().split())
answer = 0
time = 1e6
queue = deque([(N,0)])
visited_cnt = [1e6]*100001
while queue:
    soobin,sec = queue.popleft()

    if soobin == K:
        if time == 1e6:
            time = sec
        if time == sec:
            answer+=1
        continue

    if time >= sec and visited_cnt[soobin] >= sec:
        visited_cnt[soobin] = sec
        sec+=1
        if 0 <= soobin-1 <= 100000:queue.append((soobin-1,sec))
        if 0 <= soobin+1 <= 100000:queue.append((soobin+1,sec))
        if 0 <= soobin*2 <= 100000:queue.append((soobin*2,sec))

print(time,answer,sep='\n')
