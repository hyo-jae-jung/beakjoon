from sys import stdin  
from decimal import Decimal as d

A,B = stdin.readline().strip().split()
print(d(A)/d(B))
