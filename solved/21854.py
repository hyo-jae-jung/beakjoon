import sys

n = int(sys.stdin.readline().strip())
K = map(int,sys.stdin.readline().strip().split())

def power(x,n):
    a,b = 1,x
    while n > 0:
        if n%2 == 1:
            a=(a*b)%(10**9+7)
        b=(b*b)%(10**9+7)
        n = n//2
    return a%(10**9+7)

ans = 0
for k in K:
    ans+=power(2,k)
print(ans%(10**9+7))
