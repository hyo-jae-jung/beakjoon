import sys
from collections import deque

N,K = map(int,sys.stdin.readline().strip().split())

start = deque(range(1,N+1))
end = deque()

while start:
    for i in range(K):
        if i != K-1:
            start.append(start.popleft())
        else:
            end.append(str(start.popleft()))

print("<{}>".format(', '.join(end)))
