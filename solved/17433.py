from sys import stdin 
from math import gcd

answer = []
T = int(stdin.readline().strip())
for _ in range(T):
    N = int(stdin.readline().strip())
    A = list(map(int,stdin.readline().strip().split()))
    diff = []
    for i in range(1,N):
        temp = A[i] - A[i-1]
        if temp:
            diff.append(temp)
    if diff:
        answer.append(gcd(*diff))
    else:
        answer.append('INFINITY')

print(*answer,sep='\n')
