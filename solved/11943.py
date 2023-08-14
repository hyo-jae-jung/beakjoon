from sys import stdin 

A1,B1 = map(int,stdin.readline().strip().split())
A2,B2 = map(int,stdin.readline().strip().split())
a = A1+B2
b = A2+B1
print(a) if a <= b else print(b)
