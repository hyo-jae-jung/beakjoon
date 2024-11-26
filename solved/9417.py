from sys import stdin  
from itertools import combinations as comb
from math import gcd

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    max_gcd = 0
    for j in comb(list(map(int,stdin.readline().strip().split())),2):
        max_gcd = max(max_gcd,gcd(*j))

    ans.append(max_gcd)

print(*ans,sep='\n')
