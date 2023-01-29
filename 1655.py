from sys import stdin 
from collections import deque 
from bisect import bisect_left

beak = deque()
younger_bro = deque()
N = int(stdin.readline().strip())

answer = []
for i in range(N):
    said = int(stdin.readline().strip())
    beak.insert(bisect_left(beak,said),said)
    answer.append(beak[i//2])

print(answer,sep='\n')

## 시간초가고 heap 활용이 팀인거 같음...

