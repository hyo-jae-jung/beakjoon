from sys import stdin 
from heapq import heapify,heappop 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))+[1000001]

heapify(A)

i=1
while i == heappop(A):
    i+=1

print(i)
