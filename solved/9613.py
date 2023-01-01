from math import gcd
import sys
from itertools import combinations as comb

t = int(sys.stdin.readline().strip())
box = []
for _ in range(t):
    box.append(list(map(int,sys.stdin.readline().strip().split())))

answer = []
for i in box:
    n_sum = 0
    for j in comb(i[1:],2):
        n_sum+=gcd(*j)
    answer.append(n_sum)

for i in answer:
    print(i)
