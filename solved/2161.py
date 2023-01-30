from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())

cards = deque(range(1,N+1))
answer = deque()

while cards:
    answer.append(cards.popleft())
    if not cards:
        break
    cards.append(cards.popleft())

print(*answer)
