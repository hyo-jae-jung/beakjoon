from sys import stdin 

N = int(stdin.readline().strip())
A = map(int,stdin.readline().strip().split())

AB = [(j,i) for i,j in enumerate(A)]

print(AB)

AB.sort(key=lambda x:(-x[0],-x[1]))

print(AB)