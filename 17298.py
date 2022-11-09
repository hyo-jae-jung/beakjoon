import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = deque(map(int,sys.stdin.readline().strip().split()))



"""false 2 : time over
NGE = deque([-1])

for _ in range(len(A)-1):
    temp = A.pop()
    if A[-1] < temp:
        NGE.appendleft(temp)
    else:
        if A[-1] > max(NGE):
            NGE.appendleft(-1)
        else:
            for i in NGE:
                if A[-1] < i:
                    NGE.appendleft(i)
                    break

print(' '.join(map(str,NGE)))"""

"""false 1 : time over

NGE = deque()

for _ in range(N):
    temp = A.popleft()
    for i in A:
        if temp < i:
            NGE.append(i)
            break
    else:
        NGE.append(-1)

print(' '.join(map(str,NGE)))

"""