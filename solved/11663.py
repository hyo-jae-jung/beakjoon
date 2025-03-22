from sys import stdin   
from bisect import bisect_left, bisect_right

N,M = map(int,stdin.readline().strip().split())
loc = list(map(int,stdin.readline().strip().split()))
loc.sort()
ans = []
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    ans.append(bisect_right(loc,b) - bisect_left(loc,a))

print(*ans,sep='\n')

