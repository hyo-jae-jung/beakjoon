from sys import stdin 
from heapq import heapify,heappop

K = int(stdin.readline().strip())
for _ in range(K):
    arr = list(map(int,stdin.readline().strip().split()))
    heapify(arr)
    min=100
    max=0
    diff=0
    while arr:
        