from sys import stdin  
from collections import deque 

S = deque(list(stdin.readline().strip()))
stack = []
ans = 0
while S:
    s = S.popleft()
    if s == '(':
        stack.append(s)
    else:
        if stack:
            stack.pop()
        else:
            ans+=1

print(ans + len(stack))
        