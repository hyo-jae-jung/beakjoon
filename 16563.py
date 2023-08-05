from sys import stdin 

N = int(stdin.readline().strip())
K = map(int,stdin.readline().strip().split())

memo = [False]*(10*6+1)

def dfs(n,d=2):

    if memo[n]:
        return memo[n]
    
    answer = []

    while n > d:
        if n%d == 0:
            n = n//d
            if memo[n]:
                answer+=[d] + memo[n]
            else:
                answer+=[d] + dfs(n)
        else:
            dfs(n,d+1)
    else:
        return answer
    
print(dfs(N))
