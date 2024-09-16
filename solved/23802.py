from sys import stdin 

N = int(stdin.readline().strip())

for _ in range(N):
    print('@'*5*N)
for _ in range(4*N):
    print('@'*N)
    