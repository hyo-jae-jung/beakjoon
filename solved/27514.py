from sys import stdin   
from heapq import heapify,heappop,heappush

_ = int(stdin.readline().strip())
A = [int(i) for i in stdin.readline().strip().split() if i != '0']
heapify(A)
N = len(A)
ans = 0
while N > 1:
    a = heappop(A)
    b = heappop(A)

    if a == b:
        heappush(A,a+b)
    else:
        heappush(A,b)
    N-=1

print(*A)
