from sys import stdin
from collections import deque

T = int(stdin.readline().strip())

answer = []

for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    importence = map(int,stdin.readline().strip().split())
    idx_importence = deque()
    tc = []
    for i,j in enumerate(importence):
        idx_importence.append((i,j))
    while len(idx_importence) > 1:
        k=1
        while len(idx_importence) > k:
            if idx_importence[0][1] >= idx_importence[k][1]:
                k+=1
            else:
                idx_importence.rotate(-1)
                k=1
        else:
            tc.append(idx_importence.popleft())
    else:
        tc.append(*idx_importence)
    
    answer.append((tc,M))

for j in answer:
    l,m = j
    for i in range(len(l)):
        if l[i][0] == m:
            print(i+1)
            break
