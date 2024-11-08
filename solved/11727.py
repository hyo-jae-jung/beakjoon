import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
memo = defaultdict(bool)
ans = 0


