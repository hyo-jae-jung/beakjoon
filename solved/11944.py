from sys import stdin 

N,M = stdin.readline().strip().split()

l = len(N)

v = int(M)//l
r = int(M)%l

print(N*int(N) if len(N*int(N)) <= int(M) else N*v+N[:r])
