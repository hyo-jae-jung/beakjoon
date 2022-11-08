import sys
from collections import deque

N = int(sys.stdin.readline().strip())
d = deque()
p = deque()
for _ in range(N):
    order = sys.stdin.readline().strip().split()
    if order[0] == 'push_front':
        d.appendleft(int(order[-1]))
    elif order[0] == 'push_back':
        d.append(int(order[-1]))
    elif order[0] == 'size':
        p.append(len(d))
    elif order[0] == 'pop_front':
        if len(d)==0:
            p.append(-1)
        else:
            p.append(d.popleft())
    elif order[0] == 'pop_back':
        if len(d)==0:
            p.append(-1)
        else:
            p.append(d.pop())
    elif order[0] == 'front':
        if len(d)==0:
            p.append(-1)
        else:
            p.append(d[0])
    elif order[0] == 'back':
        if len(d)==0:
            p.append(-1)
        else:
            p.append(d[-1])
    elif order[0] == 'empty':
        if len(d)==0:
            p.append(1)
        else:
            p.append(0)

for i in p:
    print(i)
