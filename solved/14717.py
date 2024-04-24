from sys import stdin 
from itertools import combinations as comb
from collections import defaultdict, deque

A,B = map(int,stdin.readline().strip().split())
d = defaultdict(list)

def loc(a,b):
    if a==b:
        return 10-a
    else:
        return 19-int(str(a+b)[-1])

deq = deque([1,2,3,4,5,6,7,8,9,10]*2)
deq.remove(A)
deq.remove(B)

for i,j in comb(deq,2):
    if i==j:
        d[10-i].append((i,j))
    else:
        d[19-int(str(i+j)[-1])].append((i,j))

ans = 0
loc = loc(A,B)

for i,j in d.items():
    if i > loc:
        ans+=len(j)

print(f"{ans/153:.3f}")
