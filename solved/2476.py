from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())
answer = 0
for _ in range(N):
    temp_d = defaultdict(int)
    for i in map(int,stdin.readline().strip().split()):
        temp_d[i]+=1 
    if max(temp_d.values()) == 3:
        cg = 10000+sum(i for i in range(1,7) if temp_d[i])*1000
    elif max(temp_d.values()) == 2:
        cg = 1000+sum(i for i in range(1,7) if temp_d[i] == 2)*100
    else:
        cg = max(i for i in range(1,7) if temp_d[i])*100
    answer = max(answer,cg)

print(answer)
