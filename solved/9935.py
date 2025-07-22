from sys import stdin 
from collections import deque 

S = deque(stdin.readline().strip())
B = stdin.readline().strip()

l = len(B)
stack = []

while S:

    s = S.popleft()
    stack.append(s)

    if len(stack) < l:
        continue
    
    for i in range(1,l+1):
        if stack[-i] != B[-i]:
            break
    else:
        for _ in range(l):
            stack.pop()
    
if stack:
    print(''.join(stack))
else:
    print('FRULA')
