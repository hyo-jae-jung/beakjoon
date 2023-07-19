from sys import stdin 
from math import gcd 

N = int(stdin.readline().strip())
A = []
for _ in range(N):
    A.append(int(stdin.readline().strip()))
    
diff = []
for i in range(1,N):
    tmp = A[i] - A[i-1]
    if tmp:
        diff.append(tmp)
        
max_M = gcd(*diff)
answer = set()

for i in range(2,int(max_M**0.5+1)):
    if max_M%i == 0:
        answer.add(i)
        answer.add(max_M//i)
else:
    answer.add(max_M)
    
print(*sorted(list(answer)))
