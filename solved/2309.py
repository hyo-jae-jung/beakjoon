import sys
from itertools import combinations as comb

for i in next(iter(sorted(i) for i in comb((int(sys.stdin.readline().strip()) for _ in range(9)),7) if sum(i)==100)):
    print(i)
