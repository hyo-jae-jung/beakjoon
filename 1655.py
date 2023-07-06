from sys import stdin 
from heapq import heappop,heappush,heapify

beak = list()
younger_bro = list()
N = int(stdin.readline().strip())

for i in range(N):
    spare = []
    said = int(stdin.readline().strip())
    heappush(beak,said)
    for j in range(i//2+1):
        spare.append(heappop(beak))
    else:
        younger_bro.append(spare[-1])
        beak+=spare
        heapify(beak)

print(*younger_bro,sep='\n')
