from sys import stdin 

N = int(stdin.readline().strip())
A,B,C = map(int,stdin.readline().strip().split())

print(min(N,A)+min(N,B)+min(N,C))
