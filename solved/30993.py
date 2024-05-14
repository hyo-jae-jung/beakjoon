from sys import stdin  
from math import factorial as f  

N,A,B,C = map(int,stdin.readline().strip().split())
print(f(N)//(f(A)*f(B)*f(C)))
