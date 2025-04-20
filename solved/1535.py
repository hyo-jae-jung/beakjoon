from sys import stdin  

N = int(stdin.readline().strip())
L = list(map(int,stdin.readline().strip().split()))
J = list(map(int,stdin.readline().strip().split()))

dp = [[-1]*101 for _ in range(N+1)]

def top_down(i=0,h=100):

    if i == N:
        return 0
    
    if dp[i][h] != -1:
        return dp[i][h]

    result = top_down(i+1,h)

    if h-L[i] > 0:
        result = max(result,top_down(i+1,h-L[i]) + J[i])
        
    dp[i][h] = result
    return result

print(top_down())

