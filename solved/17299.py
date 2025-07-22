from sys import stdin   
from collections import deque 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

F = {}
for i in A:
    if not F.get(i):
        F.update({i:0})
    F[i]+=1

stack = []
ans = deque()

while A:
    a = A.pop()

    while stack:

        if F[stack[-1]] <= F[a]:
            stack.pop()
            continue
        
        ans.appendleft(stack[-1])
        stack.append(a)
        break
    
    if not stack:
        ans.appendleft(-1)
        stack.append(a)
        continue

print(*ans)
