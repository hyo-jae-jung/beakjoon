from sys import stdin 

N,W,H,L = map(int,stdin.readline().strip().split())

print(min(N,(W//L)*(H//L)))
