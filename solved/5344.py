from sys import stdin  
from math import gcd 

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
     ans.append(gcd(*list(map(int,stdin.readline().strip().split()))))

print(*ans,sep='\n')
