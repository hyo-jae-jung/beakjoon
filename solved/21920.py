from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
X = int(stdin.readline().strip())

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

s = 0
cnt = 0

for i in A:
    if gcd(X,i) == 1:
        s+=i
        cnt+=1

print(s/cnt)
