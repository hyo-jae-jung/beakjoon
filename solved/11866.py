from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().strip().split())
s = deque(range(1,N+1))
josephus =deque()
while s:
    s.rotate(-K+1)
    josephus.append(s.popleft())

print('<'+', '.join(map(str,josephus))+'>')
