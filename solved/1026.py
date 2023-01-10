from sys import stdin 

N = int(stdin.readline().strip())
A = map(int,stdin.readline().strip().split())
B = map(int,stdin.readline().strip().split())

print(sum([i*j for i,j in zip(sorted(A),sorted(B,reverse=True))]))
