from sys import stdin 
from heapq import heapify,heappop

nums = list(map(int,stdin.readline().strip().split()))
alphabets = list(stdin.readline().strip())
heapify(nums)

d = {}
i = 0
while nums:
    d.update({chr(65+i):heappop(nums)})
    i+=1

answer = []
for i in alphabets:
    answer.append(d[i])

print(*answer)
