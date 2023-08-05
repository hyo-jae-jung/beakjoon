from sys import stdin 
from heapq import heappop,heappush

younger_bro = list()
N = int(stdin.readline().strip())
answer = []
for i in range(N):
    spare = []
    said = int(stdin.readline().strip())
    heappush(younger_bro,said)
    print(younger_bro)
    answer.append(younger_bro[i//2])

print(*answer,sep='\n')
