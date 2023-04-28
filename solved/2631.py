from sys import stdin 
from bisect import bisect_left 

N = int(stdin.readline().strip())
children = []
for _ in range(N):
    children.append(int(stdin.readline().strip()))

B = []
for i in children:
    try:B[bisect_left(B,i)] = i
    except:B.append(i)

print(B)
print(N-len(B))
