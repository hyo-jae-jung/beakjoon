from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = int(stdin.readline().strip())
    coins = list(map(int,stdin.readline().strip().split()))
    dp = [1] + [0]*(M:=int(stdin.readline().strip()))

    for coin in coins:
        for i in range(coin,M+1):
            dp[i]+=dp[i-coin]
    ans.append(dp[M])

print(*ans,sep='\n')
