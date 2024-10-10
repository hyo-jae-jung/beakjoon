from sys import stdin  

A,B,C = map(int,stdin.readline().strip().split())

for i in range(C%2):
    A = A ^ B

print(A)
