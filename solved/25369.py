from sys import stdin  
import math

n = int(stdin.readline().strip())
A = math.prod(map(int,stdin.readline().strip().split()))

ans = [-1]
arr = []
def solution(N=n,val=1):
    global A,arr,ans
    if N == 0:
        if A < val:
            ans = arr.copy()
        return
    
    for i in range(1,10):
        if ans == [-1] and val*i*(9**(N-1)) > A:
            arr.append(i)
            solution(N-1,val*i)
            arr.pop()
        
solution()
print(*ans)
