from sys import stdin  

A,B,C = map(int,stdin.readline().strip().split())
print(max(A+C,B))
