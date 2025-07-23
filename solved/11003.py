from sys import stdin 
from collections import deque 

N,L = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
ans = []
q = deque()

for i,j in enumerate(A):

    if q and q[0] == i - L:
        q.popleft()
    
    while q and A[q[-1]] > j:
        q.pop()

    q.append(i)
    ans.append(A[q[0]])

print(*ans)
