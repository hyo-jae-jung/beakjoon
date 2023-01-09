from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
A = deque(sorted(map(int,stdin.readline().strip().split())))

arrange = deque()

i=0
while len(A)>1:
    if i%4 == 0:
        arrange.appendleft(A.popleft())
    elif i%4 == 1:
        arrange.append(A.pop())
    elif i%4 == 2:
        arrange.appendleft(A.pop())
    else:
        arrange.append(A.popleft())
    i+=1
else:
    if abs(arrange[0]-A[0]) >= abs(arrange[-1]-A[0]):
        arrange.appendleft(A.pop())
    else:
        arrange.append(A.pop())

answer = 0

for i in range(len(arrange)-1):
    answer+=abs(arrange[i]-arrange[i+1])

print(answer)
