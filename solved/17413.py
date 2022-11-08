import sys
from collections import deque

switch ='off'
S = list(sys.stdin.readline().strip())
answer = deque()
temp = deque()
for i in S:

    if i == '<':
        switch = 'on'
        answer.extend(temp)
        temp = deque()
    elif i == '>':
        switch = 'off'

    if switch == 'on':
        answer.append(i)
    elif switch == 'off':
        if i == ' ':
            answer.extend(temp)
            answer.append(i)
            temp = deque()
        elif i == '>':
            answer.append(i)
        else:
            temp.appendleft(i)

if temp:
    answer.extend(temp)

print(''.join(answer))
