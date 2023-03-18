from sys import stdin 

N = int(stdin.readline().strip())
k = int(stdin.readline().strip())

print((k//N+1)*(k%N+1))
