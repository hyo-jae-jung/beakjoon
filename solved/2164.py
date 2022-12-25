import sys
from collections import deque

N = int(sys.stdin.readline().strip())
cards = deque(range(1,N+1))
while len(cards) > 1:
    cards.popleft()
    t = cards.popleft()
    cards.append(t)

print(*cards)
