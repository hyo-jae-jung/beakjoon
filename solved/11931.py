from sys import stdin 
from heapq import heappush, heappop

arr = []

N = int(stdin.readline().strip())
for _ in range(N):
    heappush(arr,-int(stdin.readline().strip()))

while arr:
    print(-heappop(arr))
    