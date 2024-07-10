from sys import stdin  
from collections import defaultdict 

M = 1
for _ in range(3):
    M*=int(stdin.readline().strip())

d = defaultdict(int)
for i in str(M):
    d[i]+=1

for i in range(10):
    print(d[str(i)])
    