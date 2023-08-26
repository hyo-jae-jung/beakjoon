from sys import stdin 
from heapq import heapify,heappop 

N,L = map(int,stdin.readline().strip().split())
H = list(map(int,stdin.readline().strip().split()))

heapify(H)

while H:
    tmp = heappop(H)
    if tmp <= L:
        L+=1
    else:
        break

print(L)
