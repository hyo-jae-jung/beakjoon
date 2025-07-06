from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

A.sort()
B.sort()

i,j = 0,0
cnt = 0
while i < N and j < N:
    if A[i] == B[j]:
        cnt+=1
        i+=1
        j+=1
    elif A[i] > B[j]:
        j+=1
    elif A[i] < B[j]:
        i+=1

print(N - cnt)
