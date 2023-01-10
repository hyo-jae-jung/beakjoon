from sys import stdin 
from math import gcd

au,ad = map(int,stdin.readline().strip().split())
bu,bd = map(int,stdin.readline().strip().split())

cu = au*bd+bu*ad
cd = ad*bd
g = gcd(cu,cd)
print(int(cu/g),int(cd/g))
