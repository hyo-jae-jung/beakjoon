from sys import stdin 
from math import lcm

s = stdin.readline().strip()
t = stdin.readline().strip()

lcm_st = lcm(len(s),len(t))

S = s*(lcm_st//len(s))
T = t*(lcm_st//len(t))

print(1 if S==T else 0)
