from sys import stdin 

N,M,K = map(int,stdin.readline().strip().split())
print(K//M,K%M)
