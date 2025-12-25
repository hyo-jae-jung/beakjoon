from sys import stdin  
from bisect import bisect_right 

N,K = map(int,stdin.readline().strip().split())
X = list(map(int,stdin.readline().strip().split()))

ans = 0
idx = 0

while idx < N:
    x = X[idx]
    idx = bisect_right(X,x+K)
    ans+=1

print(ans)
