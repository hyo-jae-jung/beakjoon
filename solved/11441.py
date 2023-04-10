from sys import stdin 

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
M = int(stdin.readline().strip())
acumA = [A[0]]
for i in range(1,len(A)):
    acumA.append(acumA[i-1]+A[i])
answer = []
for _ in range(M):
    i,j = map(int,stdin.readline().strip().split())
    answer.append(acumA[j-1]-(acumA[i-2] if i > 1 else 0))
    
print(*answer,sep='\n')
