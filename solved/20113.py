from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())

X = list(map(int,stdin.readline().strip().split()))

d = defaultdict(int)

for i in X:
    if i != 0:
        d[i]+=1

sorted_d = sorted(d.items(),key=lambda x:-x[1])

if len(sorted_d) == 1 or sorted_d[0][1] > sorted_d[1][1]:
    print(sorted_d[0][0])
else:
    print("skipped")

