from sys import stdin 
from math import ceil,floor

a,b = map(int,stdin.readline().strip().split())
x,y = map(int,stdin.readline().strip().split())

if x == 0:
    print('Unknwon Number')
else:
    a,b = min(a,b),max(a,b)
    A = ceil((a-y)/x)
    B = floor((b-y)/x)

    if abs(x) <= y:
        print('Unknwon Number')
    elif A == B:
        print(x*A+y)
    else:
        print('Unknwon Number')
