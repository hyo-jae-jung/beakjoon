from sys import stdin  
from bisect import bisect_left

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    _,_ = stdin.readline().strip().split()
    A = list(map(int,stdin.readline().strip().split()))
    B = sorted(list(map(int,stdin.readline().strip().split())))

    cnt = 0
    for i in A:
        cnt+=bisect_left(B,i)

    ans.append(cnt)

print(*ans,sep='\n')
