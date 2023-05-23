from sys import stdin 
from heapq import heappop,heappush


N = int(stdin.readline().strip())

cards = []
for _ in range(N):
    heappush(cards,int(stdin.readline().strip()))
answer = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)
    answer+=a+b
    heappush(cards,a+b)
else:
    print(answer)
