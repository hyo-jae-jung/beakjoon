from sys import stdin  
from heapq import heappop,heappush


scores = []
N = int(stdin.readline().strip())

for _ in range(N):
    heappush(scores,float(stdin.readline().strip()))

for _ in range(7):
    print(f"{heappop(scores):.3f}")
