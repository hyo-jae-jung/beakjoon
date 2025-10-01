from sys import stdin 

N = int(stdin.readline().strip())
a,b,c = 1,1,1
while N > 1:
    na = a+b+c
    nb = a+c
    nc = a+b
    a,b,c = na,nb,nc
    N-=1

print((a+b+c)%9901)
