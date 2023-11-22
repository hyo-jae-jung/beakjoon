from sys import stdin 
from heapq import heappop, heappush

s = []
for _ in range(4):
    heappush(s,int(stdin.readline().strip()))
heappop(s)
h = []
for _ in range(2):
    heappush(h,int(stdin.readline().strip()))
heappop(h)
print(sum(s+h))
