import sys
sys.setrecursionlimit(10**5)

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

la,lb,lc = len(A),len(B),len(C)
dp = [[[0]*(la+1) for _ in range(lb+1)] for _ in range(lc+1)]
visited = [[[False]*(la+1) for _ in range(lb+1)] for _ in range(lc+1)]

def lcs(i=la,j=lb,k=lc):
    if i == 0 or j == 0 or k == 0:
        return 0
    
    if visited[k][j][i]:
        return dp[k][j][i]
    
    if A[i-1] == B[j-1] == C[k-1]:
        dp[k][j][i] = lcs(i-1,j-1,k-1) + 1
    elif A[i-1] == B[j-1]:
        dp[k][j][i] = max(lcs(i,j,k-1),lcs(i-1,j-1,k))
    elif A[i-1] == C[k-1]:
        dp[k][j][i] = max(lcs(i,j-1,k),lcs(i-1,j,k-1))
    elif B[j-1] == C[k-1]:
        dp[k][j][i] = max(lcs(i-1,j,k),lcs(i,j-1,k-1))
    else:
        dp[k][j][i] = max(lcs(i-1,j,k),lcs(i,j-1,k),lcs(i,j,k-1))
    visited[k][j][i] = True
    return dp[k][j][i]

print(lcs())
