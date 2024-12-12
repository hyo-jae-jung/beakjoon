from sys import stdin  

N = int(stdin.readline().strip())

def binomial(n,r):
    ans = 1
    for i in range(n,n-r,-1):
        ans*=i

    for j in range(1,r+1):
        ans/=j

    return int(ans)

print(binomial(N,5))
