from sys import stdin 
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
arr = []
for _ in range(N):
    arr.append(list(stdin.readline().strip().split()))
answer = []
directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(0,-1)]
def dfs(x,y):
    
