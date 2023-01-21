from sys import stdin 
from collections import deque

N,K = map(int,stdin.readline().strip().split())
nums = deque([int(i) for i in stdin.readline().strip().split()])
answer = deque()

temp = deque()
for _ in range(K):
    temp.append(nums.popleft())
else:
    answer.append(sum(temp))

for i in range(N-K):
    temp.popleft()
    temp.append(nums.popleft())
    answer.append(sum(temp))

print(max(answer))
