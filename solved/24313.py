from sys import stdin 

a1,a0 = map(int,stdin.readline().strip().split())
c = int(stdin.readline().strip())
n0 = int(stdin.readline().strip())

print(1 if a1 <= c and a1*n0 + a0 <= c*n0 else 0)
