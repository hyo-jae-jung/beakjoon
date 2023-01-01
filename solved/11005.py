import sys
from collections import deque

N,B = map(int,sys.stdin.readline().strip().split())
answer = ''
temp = deque()
d = dict()
for i,j in enumerate(list(range(10,36))):
    d[j]=chr(65+i)

while N > 0:
    temp.appendleft(N%B)
    N=N//B

for i in temp:
    answer+= str(i) if i < 10 else d[i]

print(answer)
