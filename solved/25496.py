from sys import stdin 
from heapq import heapify,heappop

P,N = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
heapify(A)
ans = 0
while P < 200 and bool(A):
    P += heappop(A)
    ans+=1

print(ans)
