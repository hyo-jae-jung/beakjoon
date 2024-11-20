from sys import stdin  
from collections import defaultdict

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
nums = list(map(int,stdin.readline().strip().split()))

d = defaultdict(int)
for i in nums:
    d[i]+=1

ans = 0

while nums:
    tmp = nums.pop()
    d[tmp]-=1
    if d[M-tmp]:
        d[M-tmp]-=1
        ans+=1
    
print(ans)
