from sys import stdin
from itertools import product

N = int(stdin.readline().strip())
P = [int(i) for i in stdin.readline().strip().split()]

prod = product(*[range(int(N/i)+1) for i in range(1,N+1)])

answer = []

for i in prod: 
    if sum(map(lambda x,y:x*y,range(1,N+1),i)) == N:
        temp = list(map(lambda x,y:x*y,i,P))
        answer.append(sum(temp))

print(max(answer))
