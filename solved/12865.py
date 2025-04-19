from sys import stdin  

N,K = map(int, stdin.readline().split())
items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(K+1)]

def top_down(i=0,w=0):

    if i == N:
        return 0
    
    if dp[w][i] != -1:
        return dp[w][i]
    
    result = top_down(i+1,w)
    
    if w + items[i][0] <= K:
        result = max(result,top_down(i+1,w + items[i][0]) + items[i][1])
    dp[w][i] = result
    
    return result

print(top_down())
