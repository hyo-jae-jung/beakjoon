from sys import stdin   
from math import lcm

a,b,L = map(int,stdin.readline().strip().split())

if L%a == 0 and L%b == 0:
    s = (L//a)*(L//b)

    i = 1

    while s//i > 0:
        if s%i == 0:
            if lcm(a,b,s//i) == L:
                ans = s//i
        i+=1
    else:
        print(ans)
else:
    print(-1)
