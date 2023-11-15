from sys import stdin 

N = int(stdin.readline().strip())

for j in range(N):
    print(''.join(' ' if (i+j%2)%2 else '*' for i in range(2*N)))
