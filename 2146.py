import sys
sys.setrecursionlimit(10**6)
from collections import deque

N = int(sys.stdin.readline().strip())
island_map = []
for _ in range(N):
    island_map.append(list(map(int,sys.stdin.readline().strip().split())))


for i in island_map:
    print(i)
    