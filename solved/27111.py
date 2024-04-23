from sys import stdin  
from collections import defaultdict 

N = int(stdin.readline().strip())
ans = 0
d = defaultdict(int)
for _ in range(N):
    a,b = map(int,stdin.readline().strip().split())
    if bool(d[a]) == False and b == 1:
        d[a]+=1
    elif bool(d[a]) == True and b == 0:
        d[a]-=1
    else:
        ans+=1

print(sum(d.values())+ans)
        