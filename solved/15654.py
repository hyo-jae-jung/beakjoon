import sys
from itertools import permutations as perm

N,M = map(int,sys.stdin.readline().strip().split())
progression = map(int,sys.stdin.readline().strip().split())

for i in sorted(perm(progression,M)):
    print(*i)
