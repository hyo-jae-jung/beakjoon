from sys import stdin
from math import factorial as f
from heapq import heapify,heappop,heappush

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

def solution(arr,i):
    heapify(arr)
    C = []
    j = 1
    while arr:
        b = heappop(arr)
        if i == j:
            ans = b
        else:
            heappush(C,b)
        j+=1
    return C,ans

l = list(range(1,N+1))
if arr[0] == 1:
    k = int(arr[1]) - 1
    ans = []
    F = f(N)
    B = list(range(1,N+1))
    for i in range(N,0,-1):        
        F = F//i
        B,a = solution(B,k//F+1)
        ans.append(a)
        k = k%F
    print(*ans)

else:
    ans = 1
    A,B = arr[1:].copy(),arr[1:].copy()
    heapify(B)
    C = []
    for k,j in enumerate(A,1):
        i = 0
        while B:
            n = heappop(B)
            if j == n:
                ans+=i*f(N-k)
            else:
                heappush(C,n)
                i+=1
        B = C
        C = []

    print(ans)
