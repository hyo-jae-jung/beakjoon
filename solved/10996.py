from sys import stdin 

N = int(stdin.readline().strip())

for i in range(2*N):
    tmp = ''
    for j in range(N):
        if (i+j)%2 == 0:
            tmp+='*'
        else:
            tmp+=' '
    print(tmp)
    