from sys import stdin
from math import gcd
from collections import deque

N = int(stdin.readline().strip())

rings = deque(map(int,stdin.readline().strip().split()))

first = rings.popleft()

for i in rings:
    g = gcd(first,i)
    print('{}/{}'.format(int(first/g),int(i/g)))
