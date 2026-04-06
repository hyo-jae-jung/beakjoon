from sys import stdin 
from math import comb

R,C,W = map(int,stdin.readline().strip().split())

ans = 0
for i in range(1,W+1):
    for j in range(i):
        ans+=comb(R-2+i,C-1+j)

print(ans)
