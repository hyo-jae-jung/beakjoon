import sys
from collections import deque 
sys.setrecursionlimit(10**5)

S = deque(sys.stdin.readline().strip())

def solution(s):
    
    left = deque([s.popleft()])
    while s:
        if left[-1] == s[0]:
            left.append(s.popleft())
        else:
            break
    if s:
        right = deque([s.pop()])
    else:
        if len(left) > 1:
            return len(left) + 1
        else:
            return 0
        
    while s:
        if right[0] == s[-1]:
            right.appendleft(s.pop())
        else:
            break
    
    if left[0] != right[0]:
        return 0
    
    if len(left)+len(right) < 3:
        return 0

    return solution(s)

print(solution(S))
