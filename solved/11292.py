from sys import stdin 
from collections import defaultdict

ans = []
while N := int(stdin.readline().strip()):
    max_height = 0
    data = defaultdict(list)
    for _ in range(N):
        name, height = stdin.readline().strip().split()
        data[float(height)].append(name)
        max_height = max(max_height,float(height))
    ans.append(data[max_height])

for i in ans:
    print(*i)
