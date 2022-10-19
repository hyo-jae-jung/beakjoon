import sys

M,N = map(int,sys.stdin.readline().split())

T_or_F = [False]*2+[True]*len(range(2,N+1))

for i in range(len(T_or_F)):
    if T_or_F[i]:
        for j in range(i*2,N+1,i):
            T_or_F[j] = False

for i in range(M,N+1):
    if T_or_F[i]:
        print(i)