from sys import stdin 

N = int(stdin.readline().strip())
A,B = [],[]
for _ in range(N):
    a,b = map(int,stdin.readline().strip().split())
    A.append(a)
    B.append(b)

print(sorted([i-j for i,j in zip(A,B)]))
