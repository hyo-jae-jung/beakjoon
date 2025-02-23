from sys import stdin  
from collections import defaultdict 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
d = defaultdict(int)

ans = 0
for i in A:
    if d[i] < 2:
        ans+=1
        d[i]+=1

print(ans)
