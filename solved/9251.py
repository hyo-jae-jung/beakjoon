import sys
sys.setrecursionlimit(10**5)

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

l_a,l_b = len(A),len(B)
dp = [[0]*(l_a+1) for _ in range(l_b+1)]
visited = [[False]*(l_a+1) for _ in range(l_b+1)]

def lcs(i=l_a,j=l_b):

    if i == 0 or j == 0:
        return 0
    
    if visited[j][i]:
        return dp[j][i]
    
    if A[i-1] == B[j-1]:
        dp[j][i] = lcs(i-1,j-1) + 1
    else:
        dp[j][i] = max(lcs(i,j-1),lcs(i-1,j))

    visited[j][i] = True
    return dp[j][i]
    
print(lcs())
