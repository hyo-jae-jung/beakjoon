from sys import stdin 

N = int(stdin.readline().strip())

for i,j in zip(range(N-1,-2,-1),range(1,2*N,2)):
    print(i*' ' + ''.join(["*" if i%2==0 else " " for i in range(j)]))
