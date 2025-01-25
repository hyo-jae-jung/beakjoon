from sys import stdin  
from collections import defaultdict

N = int(stdin.readline().strip())
arr = list(stdin.readline().strip().split())
info = stdin.readline().strip()

d = defaultdict(int)
for i in arr:
    d[i]+=1

print(d[info])
