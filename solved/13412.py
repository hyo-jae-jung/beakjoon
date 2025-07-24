def gcd(a,b):
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    cnt = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            if gcd(i,N//i) == 1:
                cnt+=1
    ans.append(cnt)

print(*ans,sep='\n')
