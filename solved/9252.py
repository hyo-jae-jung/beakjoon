import sys
sys.setrecursionlimit(10**5)

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

la,lb = len(A),len(B)
dp = [[0]*(la+1) for _ in range(lb+1)]
visited = [[False]*(la+1) for _ in range(lb+1)]

def lcs(i=la,j=lb):

    if i == 0 or j == 0:
        return 0
    
    if visited[j][i]:
        return dp[j][i]
    
    if A[i-1] == B[j-1]:
        dp[j][i] = lcs(i-1,j-1) + 1
    else:
        dp[j][i] = max(lcs(i-1,j),lcs(i,j-1))
    visited[j][i] = True
    return dp[j][i]

print(n:=lcs())
if n > 0:
    s = ''
    def solution(i=la,j=lb):
        global s
        if i == 0 or j == 0:
            return s
        
        if A[i-1] == B[j-1]:
            s = A[i-1] + s
            solution(i-1,j-1)
        else:
            if dp[j][i-1] > dp[j-1][i]:
                solution(i-1,j)
            else:
                solution(i,j-1)

    solution()
    print(s)
