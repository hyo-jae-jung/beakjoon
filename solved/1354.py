from sys import stdin 
from collections import defaultdict 

N,P,Q,X,Y = map(int,stdin.readline().strip().split())
memo = defaultdict(int)

def dfs(n):

    if n <= 0:
        memo[0] = 1
        return 1

    if not memo[n]:
        memo[n] = dfs(n//P - X) + dfs(n//Q - Y)
    
    return memo[n]

print(dfs(N))
