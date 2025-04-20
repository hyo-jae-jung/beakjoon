from sys import stdin  

N,M,K = map(int,stdin.readline().strip().split())
items = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]

dp = [[[-1]*(K+1) for _ in range(M+1)] for _ in range(N)]

def top_down(i=0,m=0,k=0):

    if i == N:
        return 0
    
    if dp[i][m][k] != -1:
        return dp[i][m][k]
    
    if m > M or k > K:
        return 0
    result = top_down(i+1,m,k)

    if m+items[i][0] <= M and k+items[i][1] <= K:
        result = max(result,top_down(i+1,m+items[i][0],k+items[i][1])+1)
    dp[i][m][k] = result

    return result

print(top_down())
