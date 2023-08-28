from sys import stdin 
from heapq import heapify, heappop

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

heapify(arr)
answer = []
while arr:
    answer.append(heappop(arr))

print(*answer)
