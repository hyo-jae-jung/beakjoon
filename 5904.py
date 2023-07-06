from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())
memo = defaultdict(int)
memo[1] = 3

def Moo(n):

    if memo[n]:
        return memo[n]
    
    memo[n] = Moo(n-1) + 3+n + Moo(n-1)
    return memo[n]

print(Moo(2))
