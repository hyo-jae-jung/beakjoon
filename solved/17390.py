from sys import stdin 

N,Q = map(int,stdin.readline().strip().split())
A = [int(i) for i in stdin.readline().strip().split()]
A.sort()
acum = [A[0]]
for i in range(1,len(A)):
    acum.append(acum[i-1]+A[i])

acum = [0] + acum
answer = []

for _ in range(Q):
    a,b = map(int,stdin.readline().strip().split())
    answer.append(acum[b]-acum[a-1])

print(*answer,sep='\n')
