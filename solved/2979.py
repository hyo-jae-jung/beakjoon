from sys import stdin 
from collections import defaultdict

A,B,C = map(int,stdin.readline().strip().split())
schedule = defaultdict(int)
for _ in range(3):
    start,end = map(int,stdin.readline().strip().split())
    for i in range(start,end):
        schedule[i]+=1
ans = 0
for i,j in schedule.items():
    if j == 1:
        ans+=A
    elif j == 2:
        ans+=B*2
    else:
        ans+=C*3

print(ans)
