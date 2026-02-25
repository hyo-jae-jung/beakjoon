def S(d,n):
    return d*n*(n+1)//2

from sys import stdin  
T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N,K = map(int,stdin.readline().strip().split())

    left,right = 0,N//K
    while left <= right:
        mid = (left+right)//2
        if S(K,mid) < N:
            left = mid + 1
        else:
            right = mid - 1
    i = right
    val = S(K,i)
    loc = K*(i//2+i%2)*(1 if i%2 else -1)
    ans.append(str(loc + (N - 1 - val)*(-1 if i%2 else 1)) + " " + ('L' if i%2 else 'R'))

print(*ans,sep='\n')
