from sys import stdin 
from math import gcd

n = int(stdin.readline().strip())
N = list(map(int,stdin.readline().strip().split()))

diff = []
for i in range(1,n):
    temp = N[i] - N[i-1]
    if temp:
        diff.append(temp)

print(gcd(*diff))
