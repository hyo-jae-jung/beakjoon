from sys import stdin  
from itertools import combinations as comb
from functools import reduce

A,B,C = map(int,stdin.readline().strip().split())
odd = []
even = []

for j in range(1,4):
    for i in comb([A,B,C],j):
        val = reduce(lambda x,y: x*y,i)
        if val%2 == 0:
            even.append(val)
        else:
            odd.append(val)

print(max(odd) if odd else max(even))
