from sys import stdin 

A,B,N = map(int,stdin.readline().strip().split())

cnt = 0
while cnt < N:
    A = (A%B)*10
    cnt+=1

print(A//B)
