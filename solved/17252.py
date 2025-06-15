import sys
from collections import deque 

N = int(sys.stdin.readline().strip())

ans = 'NO'

arr = []
for i in range(20):
    arr.append(3**i)

q = deque([(0,0)])

while q and N > 0:
    n,v = q.popleft()

    if v > N:
        continue
    if v == N:
        ans = 'YES'
        break
    if n < 20:
        q.append((n+1,v))
        q.append((n+1,v+arr[n]))

print(ans)
