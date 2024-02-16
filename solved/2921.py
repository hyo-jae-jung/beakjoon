from sys import stdin 

N = int(stdin.readline().strip())
print(N*(N*(N+1)//2) + N*(N+1))
