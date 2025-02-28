from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

save = []

for i in range(1,len(A)):
    for j in range(i,0,-1):
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
        else:
            break

