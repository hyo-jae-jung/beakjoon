from sys import stdin  
from bisect import bisect_left

N,K,T = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
A.sort()

t = False
stack = []
for a in A:
    if t:
        break
    if K == 0:
        break
    while a >= T:
        if stack:
            T+=stack.pop()
            K-=1
        else:
            t = True
            break
    else:
        stack.append(a)
else:
    if not t:
        for _ in range(K):
            T+=stack.pop()

print(T)
