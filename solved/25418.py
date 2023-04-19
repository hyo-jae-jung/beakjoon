from sys import stdin 
from collections import deque 

A,K = map(int,stdin.readline().strip().split())

memo = [0]*(2000001)

queue = deque([A])

def append_condition(before,next):
    if memo[next] == 0 or (memo[before]+1 < memo[next]):
        memo[next] = memo[before]+1
        queue.append(next)

while queue:
    temp = queue.popleft()
    
    if temp == K:
        break

    temp1 = temp+1
    append_condition(temp,temp1)
    
    if temp <= 500000:
        temp2 = temp*2
        append_condition(temp,temp2)

print(memo[K])
