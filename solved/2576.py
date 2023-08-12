from sys import stdin 
from heapq import heappush

nums = []
for _ in range(7):
    if (tmp := int(stdin.readline().strip()))%2 == 1:
        heappush(nums,tmp)

print(sum(nums),nums[0],sep='\n') if nums else print(-1)
