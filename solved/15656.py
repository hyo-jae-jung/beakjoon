import sys
from itertools import product

N,M = map(int,sys.stdin.readline().strip().split())
sequence = map(int,sys.stdin.readline().strip().split())

for i in product(sorted(sequence),repeat=M):
    print(*i)
