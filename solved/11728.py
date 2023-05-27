from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
A = [int(i) for i in stdin.readline().strip().split()]
B = [int(i) for i in stdin.readline().strip().split()]
A.sort()
B.sort()
answer = []
i,j = 0,0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        answer.append(A[i])
        i+=1
    else:
        answer.append(B[j])
        j+=1
else:
    if i == len(A):
        answer.extend(B[j:])
    else:
        answer.extend(A[i:])
        
print(*answer)
    