import sys
from collections import deque

N,K = map(int,sys.stdin.readline().strip().split())
A = deque()

for _ in range(N):
    A.appendleft(int(sys.stdin.readline().strip()))

cnt = 0
value = 0
for i in A:
    if i <= K:
        cnt+=K//i
        K=K%i

print(cnt)
