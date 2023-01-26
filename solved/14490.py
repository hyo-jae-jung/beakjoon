from sys import stdin 
from math import gcd 

n,m = map(int,stdin.readline().strip().split(':'))
g = gcd(n,m)
print(':'.join([str(n//g),str(m//g)]))
