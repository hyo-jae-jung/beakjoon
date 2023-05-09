from sys import stdin 

N = int(stdin.readline().strip())
A = [0]+[int(i) for i in stdin.readline().strip().split()]
D = [0]

for i in range(1,len(A)):
    D.append(A[i])
    temp = D[-1]
    for j in range(i,0,-1):
        if A[j] < temp:
            D[i]+=A[j]
            temp = A[j]

print(max(D))
