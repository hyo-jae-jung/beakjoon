from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
tops = deque([int(i) for i in stdin.readline().strip().split()])

answer = deque()
i = len(tops)-1
while i >= 0:
    j = i-1
    while j >= 0:
        if tops[j] > tops[i]:
            answer.appendleft(j+1)
            i-=1
            break 
        else:
            j-=1
    else:
        answer.appendleft(0)
        i-=1
    

print(*answer)
