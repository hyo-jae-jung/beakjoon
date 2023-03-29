from sys import stdin 
from math import factorial as f

n = int(stdin.readline().strip())
m = 0
answer = 0
while n >= 0:
    answer+=f(n+m)//(f(n)*f(m))
    n-=2
    m+=1

print(int(answer%10007))
