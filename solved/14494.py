import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().strip().split())

memo = [[0]*(max(n,m)+1) for _ in range(min(n,m)+1)]
memo[1][1] = 1

def recursion(n,m):

    i = min(n,m)
    j = max(n,m)

    if memo[i][j]:
        return memo[i][j]
    
    if i < 1 or j < 1:
        return 0

    if memo[i-1][j]:
        a = memo[i-1][j]
    else:
        a = recursion(i-1,j)
        memo[i-1][j] = a

    if memo[i][j-1]:
        b = memo[i][j-1]
    else:
        b = recursion(i,j-1)
        memo[i][j-1] = b

    if memo[i-1][j-1]:
        c = memo[i-1][j-1]
    else:
        c = recursion(i-1,j-1)
        memo[i-1][j-1] = c

    return a+b+c

print(recursion(n,m)%(10**9+7))
