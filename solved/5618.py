from sys import stdin 
from math import gcd 

n = int(stdin.readline().strip())
minimum = gcd(*list(map(int,stdin.readline().strip().split())))

def cd(m):
    d = 2
    ans = set([1,minimum])
    for i in range(1,int(minimum**(1/2)+2)):
        if minimum%i == 0:
            ans.add(i)
            ans.add(minimum//i)
    return ans

print(*sorted(cd(minimum)),sep='\n')
