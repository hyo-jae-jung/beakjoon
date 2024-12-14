from sys import stdin  

R,C,N = map(int,stdin.readline().strip().split())

print((R//N + (1 if R%N > 0 else 0))*(C//N + (1 if C%N > 0 else 0)))
