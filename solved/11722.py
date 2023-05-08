from sys import stdin 

N = int(stdin.readline().strip())
A = [0] + list(reversed([int(i) for i in stdin.readline().strip().split()]))

D = [0]
for i in range(1,len(A)):
    D.append(1)
    for j in range(1,i):
        if A[i] > A[j]:
            D[i] = max(D[i],D[j]+1)

print(max(D))
