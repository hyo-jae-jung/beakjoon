from sys import stdin  
from collections import deque 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))
M = int(stdin.readline().strip())
C = list(map(int,stdin.readline().strip().split()))

ans = []
for i in range(N-1,-1,-1):
    if A[i] == 0:
        ans.append(B[i])

print(*(ans + C)[:M])
