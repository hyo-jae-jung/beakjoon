from sys import stdin
from collections import deque, defaultdict 

N = int(stdin.readline().strip())
queue = deque([[N,0]])
answer = 0

memo = defaultdict(bool)

while queue:
    
    temp = queue.popleft()

    if temp[0] == 1:
        answer = temp[1]
        break

    if temp[0]%2 == 0:
        loc = temp[0]//2
        if not memo[loc]:
            queue.append([loc,temp[1]+1])
            memo[loc] = True

    if temp[0]%3 == 0:
        loc = temp[0]//3
        if not memo[loc]:
            queue.append([loc,temp[1]+1])
            memo[loc] = True

    if temp[0] > 1:
        loc = temp[0]-1
        if not memo[loc]:
            queue.append([loc,temp[1]+1])
            memo[loc] = True

print(answer)
