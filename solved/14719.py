from sys import stdin  
from collections import deque 

H,W = map(int,stdin.readline().strip().split())
blocks = list(map(int,stdin.readline().strip().split()))

ans = 0
d = deque()
for block in blocks:
    if d:
        if d[0] <= block:
            left_block = d.popleft()
            while d:
                another_block = d.popleft()
                ans+=left_block - another_block
        
    d.append(block)
            
right_block = d.pop()
while d:
    another_block = d.pop()
    if right_block > another_block:
        ans+=right_block - another_block
    else:
        right_block = another_block

print(ans)
