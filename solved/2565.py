from sys import stdin 
from bisect import bisect_left 

n = int(stdin.readline().strip())
A = []
for _ in range(n):
    A.append(tuple(map(int,stdin.readline().strip().split())))

A.sort(key=lambda x:x[0])

B = [0]
for _,j in A:
    B.append(j)

D = [0]
for i in B:
    try:D[bisect_left(D,i)] = i
    except:D.append(i)

print(n-len(D)+1)
