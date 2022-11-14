import sys
from itertools import combinations as comb

N,M = map(int,sys.stdin.readline().strip().split())

for i in comb(range(1,N+1),M):
    print(*i)
