from sys import stdin 
from collections import defaultdict 

n = int(stdin.readline().strip())
a,b = map(int,stdin.readline().strip().split())
m = int(stdin.readline().strip())

family = defaultdict(list)
for _ in range(m):
    x,y = map(int,stdin.readline().strip().split())
    family[x].append(y)
    