from sys import stdin  
from bisect import bisect_left

T = int(stdin.readline().strip())
ans = []
for c in range(1,T+1):
    N,K = map(int,stdin.readline().strip().split())
    arr = list(map(int,stdin.readline().strip().split()))

    tmp = []
    for i in arr:
        idx = bisect_left(tmp,i)
        if len(tmp) == idx:
            tmp.append(i)
        else:
            tmp[idx] = i
    
    if len(tmp) >= K:
        ans.append(f"Case #{c}\n1")
    else:
        ans.append(f"Case #{c}\n0")

print(*ans,sep='\n')
