import sys
from itertools import combinations_with_replacement as cwr

N,M = map(int,sys.stdin.readline().strip().split())
sequence = map(int,sys.stdin.readline().strip().split())

for i in cwr(sorted(sequence),M):
    print(*i)
