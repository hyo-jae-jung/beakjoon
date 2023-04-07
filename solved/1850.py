from sys import stdin 
from math import gcd

A,B = map(int,stdin.readline().strip().split())
print(gcd(A,B)*'1')
