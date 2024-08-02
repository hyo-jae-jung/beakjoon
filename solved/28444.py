from sys import stdin  

H,I,A,R,C = map(int,stdin.readline().strip().split())
print(H*I-A*R*C)
