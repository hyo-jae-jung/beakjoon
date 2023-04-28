from sys import stdin 
from bisect import bisect_left 

N = int(stdin.readline().strip())
lines = map(int,stdin.readline().strip().split())
B = []
for i in lines:
    try:B[bisect_left(B,i)] = i
    except:B.append(i)

print(N-len(B))
