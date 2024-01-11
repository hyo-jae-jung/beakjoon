from sys import stdin 
from heapq import heapify,heappop
A,B,C = map(int,stdin.readline().strip().split()) 

loc = [A,B,C]
heapify(loc)

left = heappop(loc)
mid = heappop(loc)
right = heappop(loc)

print(max(right-mid,mid-left)-1)
