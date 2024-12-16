from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
P = []
total_profit = 0
A = 0
for i in range(M):
    P.append(int(stdin.readline().strip()))

P.sort()

for i in range(M):
    if P[i]*(min(M-i,N)) > total_profit:
        total_profit = P[i]*(min(M-i,N))
        A = P[i]

print(A,total_profit)
