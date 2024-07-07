from sys import stdin  

N = int(stdin.readline().strip())

while N%2 == 0:
    N=N//2

print(1 if N == 1 else 0)
