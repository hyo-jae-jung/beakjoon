from sys import stdin
k,n,m = map(int,stdin.readline().strip().split())
print(k*n - m if k*n > m else 0)
