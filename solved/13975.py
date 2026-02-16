from sys import stdin  
from heapq import heapify,heappop,heappush

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    K = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split()))
    heapify(arr)
    cost = 0
    for _ in range(K-1):
        a = heappop(arr)
        b = heappop(arr)
        cost+=a+b
        heappush(arr,a+b)
    ans.append(cost)

print(*ans,sep='\n')
