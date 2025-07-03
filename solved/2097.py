from sys import stdin  

N = int(stdin.readline().strip())

a,b = 1,1
i = 0
while (a+1)*(b+1) < N:
    if i%2 == 0:
        a+=1
    else:
        b+=1
    i+=1

print(2*a+2*b)
