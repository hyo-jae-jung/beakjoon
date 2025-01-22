from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

for i,j in enumerate(range(N,0,-1)):
    if A[i] > 0:
        A[i]-=j

print(max(A))
