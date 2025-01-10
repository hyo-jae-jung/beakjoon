from sys import stdin  

T = int(stdin.readline().strip())
ans = []

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

for _ in range(T):
    n = int(stdin.readline().strip())
    A = list(map(int,stdin.readline().strip().split()))

    max_handsome_gcd = 0

    for i in range(n-1):
        tmp = A[i]
        for j in range(1+i,n):
            tmp = gcd(tmp,A[j])
            max_handsome_gcd = max(tmp*(j-i+1),max_handsome_gcd)

    ans.append(max_handsome_gcd)

print(*ans,sep='\n')
