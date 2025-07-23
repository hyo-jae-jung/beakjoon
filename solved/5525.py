from sys import stdin   
from collections import deque

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
S = deque(stdin.readline().strip())

def solution(p_len,n):
    pn = p_len//2
    if pn >= n:
        return pn - n + 1
    else:
        return 0

ans = 0
stack = []
while S:
    s = S.popleft()

    if not stack:
        if  s == 'I':
            stack.append(s)
        continue

    if stack[-1] != s:
        stack.append(s)
        continue

    if s == 'O':
        stack.pop()
    p_len = len(stack)
    ans+=solution(p_len,N)
    stack = []
    if s == 'I':
        stack.append(s)
else:
    if stack:
        if stack[-1] == 'O':
            stack.pop()
        p_len = len(stack)
        ans+=solution(p_len,N)

print(ans)
