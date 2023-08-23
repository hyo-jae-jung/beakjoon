from sys import stdin 
from heapq import heappop, heappush 

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    heappush(arr,int(stdin.readline().strip()))
    
while arr:
    print(heappop(arr))
    