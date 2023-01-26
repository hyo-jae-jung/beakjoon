from sys import stdin 
from collections import deque 

A,B = [deque(i) for i in stdin.readline().strip().split()]

diff = []

while len(A) <= len(B):
    temp_cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            temp_cnt+=1
    B.popleft()
    diff.append(temp_cnt)

print(min(diff))
