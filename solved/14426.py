from sys import stdin  
from bisect import bisect_left,bisect_right

N,M = map(int,stdin.readline().strip().split())

S = [stdin.readline().strip() for _ in range(N)]
S.sort()
arr = [stdin.readline().strip() for _ in range(M)]

ans = 0
for i in range(M):
    if bisect_right(S,arr[i]+'z'*(500-len(arr[i]))) > bisect_left(S,arr[i]):
        ans+=1

print(ans)
