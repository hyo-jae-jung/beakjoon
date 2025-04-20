from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
v_t = [tuple(map(int,stdin.readline().strip().split())) for _ in range(K)]

dp = [[-1]*(N+1) for _ in range(K)]

def top_down(i=0,t=0):

    if i == K:
        return 0
    
    if dp[i][t] != -1:
        return dp[i][t]
    
    result = top_down(i+1,t)

    if t + v_t[i][1] <= N:
        result = max(result,top_down(i+1,t+v_t[i][1]) + v_t[i][0])

    dp[i][t] = result 
    return result

print(top_down())
