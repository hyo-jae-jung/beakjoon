from sys import stdin   
from collections import deque

N = int(stdin.readline().strip())
ans = -1
cnt = 0

d = deque([str(i) for i in range(10)])
while d:
    u = d.popleft()
    cnt+=1
    if N == cnt:
        ans = u
        break

    for i in range(10):
        if int(u[-1]) > i:
            d.append(u+str(i))

print(ans)
