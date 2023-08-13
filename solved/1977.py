from sys import stdin 
from heapq import heappush 

M = int(stdin.readline().strip())
N = int(stdin.readline().strip())

nums = []

for i in range(M,N+1):
    if str(i**0.5).split('.')[1] == '0':
        heappush(nums,i)

print(sum(nums),nums[0],sep='\n') if nums else print(-1)
