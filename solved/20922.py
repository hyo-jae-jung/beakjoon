from sys import stdin  
from collections import deque 

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

nums_cnt = [0]*100001
q = deque()
ans = 1
for a in A:
    if nums_cnt[a] < K:
        q.append(a)
        nums_cnt[a]+=1
        continue
    ans = max(ans,len(q))

    while nums_cnt[a] == K:
        b = q.popleft()
        nums_cnt[b]-=1
    else:
        nums_cnt[a]+=1
        q.append(a)
else:
    ans = max(ans,len(q))

print(ans)
