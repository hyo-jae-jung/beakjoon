from sys import stdin  

A,B = map(int,stdin.readline().strip().split())
print(min(A//2,B))
