from sys import stdin
from collections import deque 

A,B = map(int,stdin.readline().strip().split())
m = int(stdin.readline().strip())
As = list(map(int,stdin.readline().strip().split()))

decimal = 0

for i,j in zip(As,range(m-1,-1,-1)):
    decimal+=i*(A**j)

answer = deque()
while decimal > 0:
    answer.appendleft(decimal%B)
    decimal = decimal//B

print(*answer)

