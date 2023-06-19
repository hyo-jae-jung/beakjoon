from sys import stdin
from heapq import heappop,heappush

N,K = map(int,stdin.readline().strip().split())

jewels = []
backpacks = []

for _ in range(N):
    m,v = map(int,stdin.readline().strip().split())
    heappush(jewels,(m,v))

for _ in range(K):
    backpacks.append(int(stdin.readline().strip()))

backpacks.sort()
answer = 0

values = []

for bag in backpacks:
    while jewels and bag >= jewels[0][0]:
        heappush(values,-heappop(jewels)[1])
    if values:
        answer-=heappop(values)
    
print(answer)
