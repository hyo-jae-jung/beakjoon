from sys import stdin 
from math import ceil

N = [int(i) for i in stdin.readline().strip()]

d = dict.fromkeys([0,1,2,3,4,5,7,8,69],0)

for i in N:
    if i in [6,9]:
        d[69]+=0.5
    else:
        d[i]+=1

print(ceil(sorted(d.items(),key=lambda x:x[1],reverse=True)[0][1]))