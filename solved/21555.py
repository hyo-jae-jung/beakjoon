from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

for i in range(1,N):
    A[i]+=min(A[i-1],B[i-1]+K)
    B[i]+=min(A[i-1]+K,B[i-1])

print(min(A[-1],B[-1]))
