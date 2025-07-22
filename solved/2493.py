from sys import stdin 
from collections import deque

N = int(stdin.readline().strip())
tops = deque(map(int,stdin.readline().strip().split()))
stack = []
ans = []

i = 1
while tops:
    top = tops.popleft()

    while stack:
        if stack[-1][0] > top:
            ans.append(stack[-1][1])
            stack.append((top,i))
            break
        stack.pop()

    if not stack:
        stack.append((top,i))
        ans.append(0)
    i+=1

print(*ans)
