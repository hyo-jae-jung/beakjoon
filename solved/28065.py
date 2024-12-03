from sys import stdin  
from collections import deque

N = int(stdin.readline().strip())
l = deque(list(range(1,N+1)))
ans = deque()
while l:
    if len(l)%2:
        ans.append(l.popleft())
    else:
        ans.append(l.pop())

print(*ans)
