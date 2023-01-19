from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
q = deque()
answer = deque()
for _ in range(N):
    temp = stdin.readline().strip().split()
    if temp[0] == 'push':
        q.append(temp[1])
    elif temp[0] == 'pop':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q.popleft())
    elif temp[0] == 'size':
        answer.append(len(q))
    elif temp[0] == 'empty':
        if len(q) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif temp[0] == 'front':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q[0])
    elif temp[0] == 'back':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q[-1])

for i in answer:
    print(i)
