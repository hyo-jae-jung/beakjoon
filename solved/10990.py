from sys import stdin 

N = int(stdin.readline().strip())

for i in range(N):
    print(' '*(N-i-1)+'*'+(' '*(2*i-1)+'*' if i else ''))
