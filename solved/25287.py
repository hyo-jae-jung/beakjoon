def solution(arr,N):
    arr[0] = min(arr[0],N-arr[0]+1)
    for i in range(1,N):
        a,b = min(arr[i],N-arr[i]+1),max(arr[i],N-arr[i]+1)
        if arr[i-1] <= a:
            arr[i] = a
        elif arr[i-1] <= b:
            arr[i] = b
        else:
            return 'NO'
    return 'YES'

from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split()))
    ans.append(solution(arr,N))

print(*ans,sep='\n')
