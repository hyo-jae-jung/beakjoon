import sys
from itertools import permutations as perm

N,M = map(int,sys.stdin.readline().strip().split())
sequense = map(int,sys.stdin.readline().strip().split())

answer = []

for i in sorted(set(perm(sequense,M))):
    print(*i)
    