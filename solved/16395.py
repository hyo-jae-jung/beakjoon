from sys import stdin 

n,k = map(int,stdin.readline().strip().split())
memo = [[0]*31 for _ in range(31)]

def C(n,k):

    if memo[n][k]:
        return memo[n][k]

    if k == 1 or n==k:
        memo[n][k] = 1
        return 1
    
    if not memo[n-1][k]:
        memo[n-1][k] = C(n-1,k)
    if not memo[n-1][k-1]:
        memo[n-1][k-1] = C(n-1,k-1)
    
    return memo[n-1][k] + memo[n-1][k-1]

print(C(n,k))
