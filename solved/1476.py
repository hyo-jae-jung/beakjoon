import sys
from itertools import cycle

E,S,M = map(int,sys.stdin.readline().strip().split())

e = cycle(range(1,16))
s = cycle(range(1,29))
m = cycle(range(1,20))
year=1

for ee,ss,mm in zip(e,s,m):
    if ee == E and ss == S and mm == M:break
    year+=1
    
print(year)
