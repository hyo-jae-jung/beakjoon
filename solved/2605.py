from sys import stdin 
from collections import deque 

n = int(stdin.readline().strip())
nums = map(int,stdin.readline().strip().split())

answer = deque()
for i,j in enumerate(nums,1):
    temp = deque()
    cnt = j
    while cnt:
        temp.appendleft(answer.pop())
        cnt-=1
    answer.append(i)
    if temp:
        answer.extend(temp)

print(*answer)
