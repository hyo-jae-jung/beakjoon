from sys import stdin 

N = int(stdin.readline().strip())
A,B = map(int,stdin.readline().strip().split())

print(min(N,A//2+B))
