from sys import stdin 
from collections import defaultdict

d = defaultdict(int)
for _ in range(10):
    d[int(stdin.readline().strip())]+=1

minimum = sum(i*j for i,j in d.items())
median_idx = max(d.values())

print(minimum//10)

for i,j in d.items():
    if j == median_idx:
        print(i)
