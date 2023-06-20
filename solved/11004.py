from sys import stdin 
from heapq import heappop,heappush,heapify

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
heapify(A)
for _ in range(K-1):
    heappop(A)
else:
    print(heappop(A))
