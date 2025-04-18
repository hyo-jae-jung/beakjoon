from sys import stdin  
from bisect import bisect_left

N,M = map(int,stdin.readline().strip().split())
A = []
for _ in range(N):
    A.append(int(stdin.readline().strip()))

A.sort()
ans = []
for _ in range(M):
    i = bisect_left(A,n:=int(stdin.readline().strip()))
    if i >= N or n != A[i]:
        ans.append(-1)
    else:
        ans.append(i)

print(*ans,sep='\n')
