from sys import stdin   
from math import factorial as f

C = int(stdin.readline().strip())
ans = []
d = {
    'O(N)':lambda x:x,
    'O(N^2)':lambda x:x**2,
    'O(N^3)':lambda x:x**3,
    'O(2^N)':lambda x:2**x,
    'O(N!)':lambda x:f(x),
    }
for _ in range(C):
    S,N,T,L = stdin.readline().strip().split()
    if d[S](int(N))*int(T) <= (10**8)*int(L):
        ans.append("May Pass.")
    else:
        ans.append("TLE!")

print(*ans,sep='\n')
