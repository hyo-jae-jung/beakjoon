from sys import stdin  
from heapq import heappush,heappop

N = int(stdin.readline().strip())
candies = list(map(int,stdin.readline().strip().split()))
ans = 0
h = []
for i in candies:
    if i%2==0:
        ans+=i
    else:
        heappush(h,i)

if len(h)%2 != 0:
    heappop(h)

print(ans+sum(h))
