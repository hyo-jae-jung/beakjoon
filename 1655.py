from sys import stdin 
import heapq

beak = list()
younger_bro = list()
N = int(stdin.readline().strip())

for i in range(N):
    said = int(stdin.readline().strip())
    heapq.heappush(beak,said)
    younger_bro.append(heapq.nsmallest(i//2+1,beak)[-1])

print(younger_bro,sep='\n')
