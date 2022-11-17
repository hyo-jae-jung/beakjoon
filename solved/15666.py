import sys
from itertools import combinations_with_replacement as it

N,M =map(int,sys.stdin.readline().strip().split())
sequence =map(int,sys.stdin.readline().strip().split())

for i in it(sorted(set(sequence)),M):
    print(*i)
