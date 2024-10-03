from sys import stdin  

A,B,C,M = map(int,stdin.readline().strip().split())

t,f,w = 0,0,0

while t < 24:

    if f + A <= M:
        f+=A
        w+=B
    else:
        f-=C
        if f < 0:
            f = 0
    t+=1

print(w)
