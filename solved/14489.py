from sys import stdin 

A,B = map(int,stdin.readline().strip().split())
C = int(stdin.readline().strip())

print(A+B-2*C if A+B>=2*C else A+B)
