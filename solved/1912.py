from sys import stdin 
from collections import deque 

n = int(stdin.readline().strip())
nums = deque([int(i) for i in stdin.readline().strip().split()])
answer = deque()

if sum([True if i >=0 else False for i in nums]) != 0:
    buff = 0
    while nums:
        temp = nums.popleft()
        if temp < 0:
            answer.append(buff)
            if buff + temp < 0:
                buff = 0
            else:
                buff+=temp
        else:
            buff+=temp
    else:
        answer.append(buff)
else:
    answer = nums

print(max(answer))
        