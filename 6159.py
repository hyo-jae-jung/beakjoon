from sys import stdin 
from collections import defaultdict

N,S = map(int,stdin.readline().strip().split())
ans = 0

cows = defaultdict(int)
for _ in range(N):
    cows[int(stdin.readline().strip())]+=1

j = 0
list(cows.keys())



