from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
contestants = deque([[i,int(j)] for i,j in enumerate(stdin.readline().strip().split())])

cnt = 0
answer = []
while contestants:
    temp = contestants.popleft()
    if temp[1]:
        temp[1]-=1
        cnt+=1
    
    if not temp[1]:
        answer.append([temp[0],cnt])
    else:
        contestants.append(temp)

print(*sum(sorted(answer,key=lambda x:x[0]),[])[1::2])
