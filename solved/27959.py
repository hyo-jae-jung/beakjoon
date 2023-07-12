from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
print('Yes' if 100*N >= M else 'No')
