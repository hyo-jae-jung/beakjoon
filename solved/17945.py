from sys import stdin   

A,B = map(int,stdin.readline().strip().split())

x1 = int((-2*A+((2*A)**2-4*B)**0.5)//2)
x2 = int((-2*A-((2*A)**2-4*B)**0.5)//2)


print(min(x1,x2),max(x1,x2)) if x1 != x2 else print(x1)
