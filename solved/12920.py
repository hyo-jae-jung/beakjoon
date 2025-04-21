import sys

N,M = map(int,sys.stdin.readline().strip().split())
items = []

def div_bin(n):
    t,i = 0,0
    ans = []
    while n > 0:
        while n >= t + 2**i:
            ans.append(i)
            t+=2**i
            i+=1
        n-=t
        t,i = 0,0
    return ans

for _ in range(N):
    v,c,k = map(int,sys.stdin.readline().strip().split())
    for i in div_bin(k):
        items.append((v*(2**i),c*(2**i)))

dp = [0]*(M + 1)

for weight, value in items:
    for w in range(M, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(max(dp))
