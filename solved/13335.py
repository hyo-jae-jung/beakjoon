from sys import stdin  
from collections import deque  

n,w,L = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

t = 0
i = 0
q = deque([0]*w)

while i < n:
    tw = q.popleft()
    L+=tw

    if A[i] <= L:
        q.append(A[i])
        L-=A[i]
        i+=1
        if i == n:
            t+=w+1
            break
    else:
        q.append(0)
    t+=1

print(t)
