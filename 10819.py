from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
A = deque(map(int,stdin.readline().strip().split()))
A.sort()
answer = deque()
n = 0
while A:
    if n%2 == 0:
        answer.append(A.pop())
    else:
        answer.append(A.popleft())
