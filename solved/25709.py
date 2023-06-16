from sys import stdin 
from collections import deque

N = deque(stdin.readline().strip())

answer = 0

for _ in range(len(N)):
    temp=N.popleft()
    if temp == '1':
        answer+=1
    else:
        N.append(temp)
else:
    N = list(map(int,list(str(int(''.join(N if N else ['0']))))))

if len(N) > 1:
    for i in range(-1,-1*len(N),-1):
        if N[i] <= 0:
            N[i-1]-=1
            N[i]+=10

answer+=sum(N)
print(answer)
