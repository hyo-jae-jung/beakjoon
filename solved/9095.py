from itertools import product
from sys import stdin
from math import factorial as f

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    p = product(range(n+1),range(int(n/2)+1),range(int(n/3)+1))
    cnt = 0
    for i in p:
        x,y,z = i
        if x+2*y+3*z == n:
            cnt+=f(x+y+z)/(f(x)*f(y)*f(z))
    answer.append(int(cnt))

for i in answer:
    print(i)
