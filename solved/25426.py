from sys import stdin  

N = int(stdin.readline().strip())
ans = 0
A = []
for _ in range(N):
    a,b = map(int,stdin.readline().strip().split())
    ans+=b
    A.append(a)

A.sort()

for i,j in zip(A,range(1,N+1)):
    ans+=i*j

print(ans)
