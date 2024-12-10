from sys import stdin 
from math import lcm 

N = int(stdin.readline().strip())
T = list(map(int,stdin.readline().strip().split()))
print(lcm(*T))
