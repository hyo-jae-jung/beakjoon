import sys
from itertools import combinations as comb

N,M = map(int,sys.stdin.readline().strip().split())
progression = map(int,sys.stdin.readline().strip().split())

for i in sorted(comb(sorted(progression),M)):
    print(*i)
