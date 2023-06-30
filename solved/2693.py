from sys import stdin 
from heapq import heapify,heappop

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    arr = [-i for i in map(int,stdin.readline().strip().split())]
    heapify(arr)
    heappop(arr)
    heappop(arr)
    answer.append(-heappop(arr))

print(*answer,sep='\n')
