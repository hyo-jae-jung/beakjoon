from sys import stdin 
from heapq import heapify, heappop

nums = list(map(int,stdin.readline().strip().split()))
heapify(nums)

a = heappop(nums)
b = heappop(nums)
c = heappop(nums)
diff1 = b-a
diff2 = c-b

if diff1 == diff2:
    print(c+diff1)
elif diff1 > diff2:
    print(a+diff2)
elif diff1 < diff2:
    print(b+diff1)
