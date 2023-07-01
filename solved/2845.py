from sys import stdin 

L,P = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
num = L*P
print(*[i-num for i in A])
