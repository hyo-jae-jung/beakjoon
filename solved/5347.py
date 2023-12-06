from sys import stdin 
from math import lcm

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    ans.append(lcm(*map(int,stdin.readline().strip().split())))

print(*ans, sep='\n')
