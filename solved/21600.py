from sys import stdin  
from collections import deque 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
queue = deque()
cnt = 0
ans = 0
for i in range(N):

    while cnt > 0 and A[i] <= cnt:
        queue.popleft()
        cnt-=1

    if A[i] > cnt:
        queue.append(A[i])
        cnt+=1
        ans = max(ans,cnt)
        continue

print(ans)
