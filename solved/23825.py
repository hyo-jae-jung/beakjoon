from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
print(min(N,M)//2)
