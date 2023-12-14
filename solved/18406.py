from sys import stdin 

N = list(map(int,stdin.readline().strip()))
if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
    print('LUCKY')
else:
    print('READY')
    