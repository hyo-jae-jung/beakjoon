from sys import stdin 

N,M,K = map(int,stdin.readline().strip().split())

print(min(M,K)+N-max(M,K))
