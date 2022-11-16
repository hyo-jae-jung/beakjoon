import sys
from itertools import permutations as it

N,M = map(int,sys.stdin.readline().strip().split())
sequence = map(int,sys.stdin.readline().strip().split())

for i in sorted(set([tuple(sorted(i)) for i in it(sequence,M)])):
    print(*i)
