import sys
from collections import deque 

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))

ans = deque()
stack = []
while A:
    a = A.pop()
    while stack:
        if stack[-1] > a:
            ans.appendleft(stack[-1])
            stack.append(a)
            break
        else:
            stack.pop()
    else:
        stack.append(a)
        ans.appendleft(-1)

print(*ans)
