import sys
from collections import deque

sentence = deque(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
moving_sentence = deque([])
for _ in range(N):
    order = sys.stdin.readline().strip()
    if order[0] == 'L' and len(sentence) != 0:
        moving_sentence.appendleft(sentence.pop())
    elif order[0] == 'D' and len(moving_sentence) != 0:
        sentence.append(moving_sentence.popleft())

    elif order[0] == 'B' and len(sentence) != 0:
        sentence.pop()
    elif order[0] == 'P':
        sentence.append(order.split()[-1])

print(''.join(sentence+moving_sentence))

""" false 1
sentence = input()
sentence=list(sentence)
N = len(sentence)
command_cnt = int(input())
command_list = (input() for _ in range(command_cnt))
cursor_position = N
for i in command_list:
    if i[0] == 'L' and cursor_position != 0: cursor_position-=1
    elif i[0] == 'D' and cursor_position != N: cursor_position+=1
    elif i[0] == 'B' and cursor_position != 0: 
        sentence.pop(cursor_position-1)
        N-=1
        cursor_position-=1
    elif i[0] =='P':
        sentence.insert(cursor_position,i[-1])
        N+=1
        cursor_position+=1

print(''.join(sentence))
"""

