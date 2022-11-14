import sys
from itertools import combinations_with_replacement as comb_w_r

N,M = map(int,sys.stdin.readline().strip().split())

for i in comb_w_r(range(1,N+1),M):
    print(*i)
