from sys import stdin 

N = int(stdin.readline().strip())
for i in list(range(1,N+1)) + list(range(N-1,0,-1)):
    print(('*'*i).rjust(N,' '))
