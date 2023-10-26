from sys import stdin 
from heapq import heappush,heappop

N = int(stdin.readline().strip())
degrees = list(map(int,stdin.readline().strip().split()))
K = int(stdin.readline().strip())
n = 2
j = 1
while N//n >= K:
    h = []
    for i in range(0,N,n):

        for k in range(i,n+i):
            heappush(h,degrees[k])
        
        for l in range(i,n+i):
            degrees[l] = heappop(h)

    n*=2

print(*degrees)
