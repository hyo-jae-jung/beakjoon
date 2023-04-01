from sys import stdin 
from itertools import permutations as perm
N = int(stdin.readline().strip())
for i in perm(range(1,N+1),N):
    print(*i)
    