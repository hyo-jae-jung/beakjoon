from sys import stdin 
from math import ceil
N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
B,C = map(int,stdin.readline().strip().split())

print(sum(ceil((i-B if i>=B else 0)/C)+1 for i in A))
