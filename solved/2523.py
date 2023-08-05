from sys import stdin 

N = int(stdin.readline().strip())
for i in list(range(-N+1,0))+[-i for i in range(N)]:
    print('*'*(N+i))
