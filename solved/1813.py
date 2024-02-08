from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())
nums = map(int,stdin.readline().strip().split())
d = defaultdict(int)
for i in nums:
    d[i]+=1

tmp = sorted(i for i,j in d.items() if i==j)

if tmp:
    print(tmp[-1])
else:
    if d[0]:
        print(-1)
    else:
        print(0)
        