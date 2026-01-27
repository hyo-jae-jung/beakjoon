from sys import stdin  
from math import log2

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
A.sort()
cut = N//2 + (1 if N%2 > 0 else 0)
left = list(map(lambda x:int(log2(x)),A[:cut]))

print(sum(left)+1)
