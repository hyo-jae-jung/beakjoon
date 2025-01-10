import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
memo = defaultdict(int)
memo['0'] = 1
memo['1'] = 2
memo['2'] = 2
ans = 0

def recursion(l):
    if memo[l]:
        if memo[l]+2 <= n:
            