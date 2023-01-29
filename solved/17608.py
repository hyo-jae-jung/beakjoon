from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
bars = deque()
for _ in range(N):
    bars.appendleft(int(stdin.readline().strip()))

max_bar = 0
bar_cnt = 0
for i in bars:
    if i > max_bar:
        bar_cnt+=1
        max_bar = i

print(bar_cnt)
