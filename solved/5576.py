from sys import stdin 
from heapq import heappush,heappop

W,K = [],[]
for _ in range(10):
    heappush(W,-int(stdin.readline().strip()))
for _ in range(10):
    heappush(K,-int(stdin.readline().strip()))

w_sum,k_sum = 0,0
for _ in range(3):
    w_sum-=heappop(W)
    k_sum-=heappop(K)

print(w_sum,k_sum)
