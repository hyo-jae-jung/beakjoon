from sys import stdin 
from collections import defaultdict 

T = int(stdin.readline().strip())

d = defaultdict(list)
d[1].extend([1])
d[2].extend([6,2,4,8])
d[3].extend([1,3,9,7])
d[4].extend([6,4])
d[5].extend([5])
d[6].extend([6])
d[7].extend([1,7,9,3])
d[8].extend([6,8,4,2])
d[9].extend([1,9])

answer = []
for _ in range(T):
    a,b = map(int,stdin.readline().strip().split())
    A = int(str(a)[-1])
    if not A:
        answer.append(10)
    else:
        answer.append(d[A][b%len(d[A])])

print(*answer,sep='\n')
