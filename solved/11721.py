from sys import stdin 
from collections import deque 
word = deque(stdin.readline().strip())
answer = ''
while word:
    answer+=word.popleft()
    if len(answer) == 10:
        print(answer)
        answer = ''
else:
    print(answer)
    