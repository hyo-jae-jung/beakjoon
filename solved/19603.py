from sys import stdin  

P = int(stdin.readline().strip())
N = int(stdin.readline().strip())
R = int(stdin.readline().strip())

i = 0

if R == 1:
    print(P//N)
else:
    while N*(R**(i+1)-1)//(R-1) <= P:
        i+=1
    print(i)
