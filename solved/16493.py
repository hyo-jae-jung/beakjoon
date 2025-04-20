from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
date_page = [tuple(map(int,stdin.readline().strip().split())) for _ in range(M)]

dp = [[-1]*(N+1) for _ in range(M)]

def top_down(i=0,d=0):

    if i == M:
        return 0 
    
    if dp[i][d] != -1:
        return dp[i][d]
    
    result = top_down(i+1,d)

    if d + date_page[i][0] <= N:
        result = max(result,top_down(i+1,d + date_page[i][0]) + date_page[i][1])

    dp[i][d] = result
    return result 

print(top_down())
