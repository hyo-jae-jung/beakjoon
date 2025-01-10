from sys import stdin  
from heapq import heappop,heappush

N,M = map(int,stdin.readline().strip().split())
arr = []

for _ in range(N):
    arr.append(int(stdin.readline().strip()))

ans = []
for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    tmp = []
    for i in range(a-1,b):
        heappush(tmp,arr[i])
    ans.append(heappop(tmp))

print(*ans,sep='\n')
