from sys import stdin   
from bisect import bisect_left

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
tracking = [-1]*N

arr = []
arr_idx = []
for i in range(N):
    idx = bisect_left(arr,A[i])
    if arr.__len__() == idx:
        arr.append(A[i])
        arr_idx.append(i)

    else:
        arr[idx] = A[i]
        arr_idx[idx] = i
    
    tracking[i] = arr_idx[idx-1] if idx > 0 else -1

from collections import deque 

ans = deque()
e = arr_idx[-1]
ans.appendleft(A[e])
while tracking[e] != -1:
    ans.appendleft(A[tracking[e]])
    e = tracking[e]

print(len(ans))
print(*ans)
