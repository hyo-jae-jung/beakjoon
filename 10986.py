from sys import stdin 
from collections import deque

N,M = map(int,stdin.readline().strip().split())
A = [int(i) for i in stdin.readline().strip().split()]
D = deque([0])
answer = 0

for i in range(N):
    D.append(A[i]+D[-1])

while D:
    temp = D.popleft()
    for i in range(len(D)):
        D[i]-=temp
        if D[i]%M == 0:
            answer+=1

print(answer)
