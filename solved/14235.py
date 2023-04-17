from sys import stdin 
from heapq import heappop, heappush

n = int(stdin.readline().strip())

sled = []
answer = []

for _ in range(n):
    seq = list(map(int,stdin.readline().strip().split()))
    temp = seq[0]
    if temp == 0:
        try:
            answer.append(heappop(sled)[1])
        except:
            answer.append(-1)
    else:
        for i in seq[1:]:
            heappush(sled,(-i,i))
        
print(*answer,sep='\n')
