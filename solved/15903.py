from sys import stdin   
from heapq import heapify,heappop,heappush

n,m = map(int,stdin.readline().strip().split())
arr = list(map(int,stdin.readline().strip().split()))

heapify(arr)

for _ in range(m):
    x = heappop(arr)
    y = heappop(arr)
    heappush(arr,x+y)
    heappush(arr,x+y)

print(sum(arr))
