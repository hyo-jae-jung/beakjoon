from sys import stdin 

n,m =map(int,stdin.readline().strip().split())

u = set(range(m+1,n+1))
d = set(range(1,n-m+1))

a = u-d
b = d-u

U = 1
D = 1

for i in a:
    U*=i

for i in b:
    D*=i

print(U//D)

